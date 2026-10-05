from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "semantic"))

from local_recheck_queue import append_observation, record_failure


class LocalRecheckQueueTests(unittest.TestCase):
    def failure(self, observed_at="2026-10-05T00:00:00Z", signature="http:503|envoy:upstream-connect-before-headers"):
        return {
            "claim_id": "1234:objective_ranking_or_market_share:abcdef0123456789",
            "normalized_claim_hash": "abcdef0123456789" + "0" * 48,
            "issuer": "測試公司",
            "claim_text": "測試 claim",
            "attempted_url": "https://official.example.test/report.pdf",
            "source_host": "official.example.test",
            "failure_signature": signature,
            "semantic_consequence": "排名 qualifier 尚待可檢視的正式來源。",
            "observation": {
                "observed_at": observed_at,
                "http_status": 503,
                "response_headers": {"server": "envoy"},
                "exact_error_message": "upstream connect error before headers",
                "retrieval_environment": "codex-cloud",
            },
        }

    def test_same_claim_url_and_failure_is_idempotent_and_appends_observations(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "queue.json"
            recheck_id, added = record_failure(path, self.failure())
            self.assertTrue(added)

            same_id, added = record_failure(path, self.failure())
            self.assertEqual(same_id, recheck_id)
            self.assertFalse(added)

            _, added = record_failure(path, self.failure("2026-10-05T00:01:00Z"))
            self.assertTrue(added)
            queue = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(len(queue["items"]), 1)
            self.assertEqual(len(queue["items"][0]["observations"]), 2)
            self.assertEqual(queue["items"][0]["queue_state"], "LOCAL_RECHECK_PENDING")

    def test_different_failure_signature_is_a_distinct_recheck_entry(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "queue.json"
            first_id, _ = record_failure(path, self.failure())
            second_id, _ = record_failure(path, self.failure(signature="http:503|origin:service-unavailable"))
            self.assertNotEqual(first_id, second_id)
            queue = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(len(queue["items"]), 2)

    def test_later_home_observation_does_not_overwrite_cloud_failure(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "queue.json"
            recheck_id, _ = record_failure(path, self.failure())
            append_observation(path, recheck_id, {
                "observed_at": "2026-10-06T08:00:00+08:00",
                "http_status": 200,
                "response_headers": {"content-type": "application/pdf"},
                "exact_error_message": None,
                "retrieval_environment": "home-network",
                "result_note": "Availability observation only; no semantic decision.",
            })
            queue = json.loads(path.read_text(encoding="utf-8"))
            observations = queue["items"][0]["observations"]
            self.assertEqual([x["retrieval_environment"] for x in observations], ["codex-cloud", "home-network"])
            self.assertEqual(observations[0]["http_status"], 503)
            self.assertEqual(observations[1]["http_status"], 200)
            self.assertEqual(queue["items"][0]["queue_state"], "LOCAL_RECHECK_PENDING")


if __name__ == "__main__":
    unittest.main()
