from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import semantic_worker as worker


def make_claim(i: int) -> dict:
    return {"claim_id": f"{i}:objective_ranking_or_market_share:abcdef{i:010d}", "claim": f"claim {i}"}


def result(decision="PARTIALLY_SUPPORTED"):
    return {"decision": decision, "rationale": "checked", "evidence": [], "proposed_text": None}


class SemanticWorkerConcurrencyTests(unittest.TestCase):
    def setUp(self):
        self.state = {"schema": "semantic-worker-state-1", "results": {}, "batches": []}

    def test_duplicate_claim_is_never_submitted_twice(self):
        claims = [make_claim(1), make_claim(1), make_claim(2)]
        submitted = []
        batch = worker.process_batch(claims, self.state, lambda c: submitted.append(c["claim_id"]) or result(), lambda c: result(), 4, 4)
        self.assertEqual(len(set(batch["selected_claim_ids"])), 2)
        self.assertEqual(len(submitted), 2)

    def test_already_authored_claim_skips_author_stage(self):
        claim = make_claim(1)
        self.state["results"][claim["claim_id"]] = {"claim_id": claim["claim_id"], "author": result(), "reviewer": None, "status": "REVIEWER_PENDING", "attempts": 0}
        authors = []
        worker.process_batch([claim], self.state, lambda c: authors.append(c) or result(), lambda c: result(), 4, 4)
        self.assertEqual(authors, [])

    def test_already_reviewed_claim_skips_reviewer_stage(self):
        claim = make_claim(1)
        rec = {"claim_id": claim["claim_id"], "author": result(), "reviewer": result(), "final_state": "PARTIALLY_SUPPORTED", "status": "FINALISED", "attempts": 0}
        self.state["results"][claim["claim_id"]] = rec
        reviewers = []
        worker.process_batch([claim], self.state, lambda c: result(), lambda c: reviewers.append(c) or result(), 4, 4)
        self.assertEqual(reviewers, [])
        self.assertEqual(rec["final_state"], "PARTIALLY_SUPPORTED")

    def _assert_pool_reaches_four(self, stage):
        lock = threading.Lock()
        active = 0
        peak = 0
        def call(_claim):
            nonlocal active, peak
            with lock:
                active += 1
                peak = max(peak, active)
            time.sleep(0.05)
            with lock:
                active -= 1
            return result()
        kwargs = {"author_fn": call, "reviewer_fn": call, "author_concurrency": 4, "reviewer_concurrency": 4}
        worker.process_batch([make_claim(i) for i in range(8)], self.state, **kwargs)
        self.assertEqual(peak, 4)

    def test_four_author_tasks_execute_concurrently(self):
        self._assert_pool_reaches_four("author")

    def test_four_reviewer_tasks_execute_concurrently(self):
        claims = [make_claim(i) for i in range(8)]
        for c in claims:
            self.state["results"][c["claim_id"]] = {"claim_id": c["claim_id"], "author": result(), "reviewer": None, "status": "REVIEWER_PENDING", "attempts": 0}
        self._assert_pool_reaches_four("reviewer")

    def test_one_worker_failure_does_not_stop_unrelated_claims(self):
        def author(c):
            if c["claim_id"] == make_claim(1)["claim_id"]:
                raise RuntimeError("one claim failed")
            return result()
        batch = worker.process_batch([make_claim(i) for i in range(3)], self.state, author, lambda c: result(), 4, 4)
        self.assertEqual(batch["author_error"], 1)
        self.assertEqual(batch["reviewer_success"], 2)
        self.assertEqual(self.state["results"][make_claim(1)["claim_id"]]["status"], "AUTHOR_ERROR")

    def test_retry_statuses_and_retry_after_are_bounded(self):
        for status in (429, 503):
            exc = urllib.error.HTTPError("https://api.example", status, "retry", {"Retry-After": "999"}, None)
            self.assertEqual(worker.retry_delay(exc, 0), 60)
        self.assertIsNone(worker.retry_delay(urllib.error.HTTPError("u", 403, "no", {}, None), 0))
        self.assertLessEqual(worker.retry_delay(TimeoutError("timeout"), 20), 30)

    def test_429_and_503_retries_are_bounded(self):
        for status in (429, 503):
            calls = []
            def fail(*_args, **_kwargs):
                calls.append(status)
                raise urllib.error.HTTPError("https://api.openai.com/v1/responses", status, "temporary", {}, None)
            with patch.object(worker.urllib.request, "urlopen", side_effect=fail), patch.object(worker.time, "sleep"):
                with self.assertRaises(RuntimeError):
                    worker.call_openai("key", "model", "medium", make_claim(1), "role", retries=3)
            self.assertEqual(len(calls), 3)

    def test_state_writes_are_invoked_on_coordinator_thread_only(self):
        main_thread = threading.get_ident()
        write_threads = []
        worker.process_batch([make_claim(i) for i in range(5)], self.state, lambda c: result(), lambda c: result(), 4, 4, persist_state=lambda _: write_threads.append(threading.get_ident()))
        self.assertTrue(write_threads)
        self.assertEqual(set(write_threads), {main_thread})

    def test_rerunning_batch_selection_is_idempotent(self):
        claim = make_claim(1)
        worker.process_batch([claim], self.state, lambda c: result(), lambda c: result(), 4, 4)
        selected = worker.select_claims({"items": [claim]}, self.state, 1)
        self.assertEqual(selected, [])

    def test_historical_author_records_remain_intact(self):
        author_path = Path("audit-v5/semantic/author-011.json")
        before = hashlib.sha256(author_path.read_bytes()).hexdigest()
        author_batch = json.loads(author_path.read_text(encoding="utf-8"))
        self.assertEqual(len(author_batch["items"]), 2)
        queue_item = {"claim_id": author_batch["items"][0]["claim_id"]}
        loaded = worker.load_state({"claim_count": 0})
        self.assertIn(queue_item["claim_id"], loaded["results"])
        self.assertEqual(hashlib.sha256(author_path.read_bytes()).hexdigest(), before)

    def test_final_state_rules_are_unchanged(self):
        self.assertEqual(worker.finalise(result("ACCEPTED"), result("ACCEPTED")), ("ACCEPTED", "AUTHOR_REVIEWER_AGREE"))

    def test_disagreement_still_escalates(self):
        self.assertEqual(worker.finalise(result("ACCEPTED"), result("UNSUPPORTED")), ("ESCALATED_REVIEW_DISAGREEMENT", "AUTHOR=ACCEPTED;REVIEWER=UNSUPPORTED"))

    def test_state_json_stays_valid_after_worker_exception(self):
        path = Path(tempfile.gettempdir()) / "semantic-worker-state-test.json"
        path.unlink(missing_ok=True)
        worker.process_batch([make_claim(i) for i in range(3)], self.state, lambda c: (_ for _ in ()).throw(ValueError("boom")) if c["claim_id"] == make_claim(0)["claim_id"] else result(), lambda c: result(), 4, 4, persist_state=lambda state: worker.atomic_write_json(path, state))
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(parsed["results"][make_claim(0)["claim_id"]]["status"], "AUTHOR_ERROR")
        path.unlink()

    def test_status_report_retains_transient_recheck_queue(self):
        queue = {"issuer_count": 836, "raw_signal_count": 1410, "claim_count": 1399}
        cfg = {"batch_size": 8, "author_concurrency": 4, "reviewer_concurrency": 4, "author_model": "model", "reviewer_model": "model", "schedule": "test"}
        report = worker.render_status(queue, self.state, cfg)
        self.assertIn("Author concurrency: **4**", report)
        self.assertIn("Reviewer concurrency: **4**", report)
        self.assertIn("`LOCAL_RECHECK_PENDING` URLs: **15**", report)
        self.assertIn("HTTP/error 500: **8**", report)
        self.assertIn("HTTP/error 503: **7**", report)


if __name__ == "__main__":
    unittest.main()
