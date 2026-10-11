from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import types
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "candidate_runner_provenance_test",
    REPO / "audit-v5/semantic/candidate-rerun/run_hermes_batch.py",
)
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


def item(seq: int, ticker: str = "1234") -> dict:
    return {
        "queue_sequence": seq,
        "claim_id": f"synthetic-claim-{seq}",
        "normalized_claim_hash": f"synthetic-hash-{seq}",
        "issuer_ticker": ticker,
        "issuer_company": "合成測試公司",
        "report_path": "synthetic/report.md",
        "claim": "Synthetic original claim with period 2024.",
        "author_batch_id": "synthetic-author-batch",
        "author_batch_path": "synthetic/author.json",
        "author_batch_sha256": "synthetic-author-hash",
        "author_decision": "PARTIALLY_SUPPORTED",
    }


def source(locator="page 1", period="2024", note="table"):
    return {
        "source_title": "Synthetic PDF",
        "url": "https://example.invalid/synthetic.pdf",
        "publication_date": "2025-03-01",
        "effective_period": period,
        "locator": locator,
        "note": note,
        "source_level": 3,
    }


def payload(overall="PARTIAL", atoms=None, candidate=False, final_gate=False):
    if atoms is None:
        atoms = [{
            "text": "synthetic original atom",
            "status": "UNKNOWN",
            "period": "2024",
            "sources": [],
        }]
    return json.dumps({
        "overall": overall,
        "candidate_accepted": candidate,
        "requires_final_adjudication": final_gate,
        "atomic_claims": atoms,
        "research_exhausted": True,
        "research_stop_reason": "Synthetic fixture only.",
        "source_caveats": [],
    }).encode("utf-8")


class CandidateProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(
            prefix="candidate-provenance-", dir=os.environ["TMPDIR"]
        )
        self.base = Path(self.temp.name)
        self.root = self.base / "audit-v5/semantic/candidate-rerun"
        self.cache = self.base / "audit-v5/source-cache/candidate-rerun"

    def tearDown(self):
        self.temp.cleanup()

    def run_item(self, claim, batch, responses, budget=None, superseding=False):
        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            runner, "STOP_EVENT", threading.Event()
        ), patch.object(
            runner.subprocess, "run", side_effect=responses
        ) as run, patch.object(runner.time, "sleep"):
            kwargs = {} if budget is None else {"run_budget_seconds": budget}
            result, warning = runner.process_item(claim, len(responses), batch, superseding, **kwargs)
        return result, warning, run

    def manifest_for(self, result):
        path = self.base / result["evidence_manifest"]
        return json.loads(path.read_text(encoding="utf-8"))

    def prepare_main_fixture(self):
        base = self.base / "synthetic-project"
        root = base / "audit-v5/semantic/candidate-rerun"
        cache = base / "audit-v5/source-cache/candidate-rerun"
        root.mkdir(parents=True)
        (root / "batches").mkdir()
        queue_path = root / "queue.jsonl"
        queue_path.write_text(json.dumps(item(1), ensure_ascii=False) + "\n", encoding="utf-8")
        checkpoint_path = root / "checkpoint.json"
        checkpoint_path.write_text(json.dumps({
            "queued": 1,
            "processed": 0,
            "remaining": 1,
            "verdict_counts": {"PARTIAL": 0, "CANDIDATE_ACCEPTED": 0, "UNKNOWN": 0},
            "completed_through_sequence": 0,
            "current_rerun_batch": "rerun-001",
            "current_batch_processed": 0,
            "queue_sha256": hashlib.sha256(queue_path.read_bytes()).hexdigest(),
        }), encoding="utf-8")
        return base, root, cache, queue_path, checkpoint_path

    def run_main(self, base, root, cache, queue_path, checkpoint_path, argv, responses):
        with patch.multiple(
            runner, BASE=base, ROOT=root, CACHE=cache,
            QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path,
        ), patch.object(runner, "STOP_EVENT", threading.Event()), patch.object(
            runner.subprocess, "run", side_effect=responses
        ) as run, patch.object(
            sys, "argv", ["run_hermes_batch.py", *argv]
        ), redirect_stderr(io.StringIO()) as stderr, redirect_stdout(io.StringIO()) as stdout:
            exit_code = runner.main()
        return exit_code, stderr.getvalue(), stdout.getvalue(), run

    def test_execution_record_binds_oneshot_toolsets_and_max_turns(self):
        response = types.SimpleNamespace(returncode=0, stdout=payload(), stderr=b"")
        result, warning, run = self.run_item(item(40), "rerun-009", [response])

        self.assertIsNone(warning)
        manifest = self.manifest_for(result)
        for record in (result, manifest):
            self.assertIs(record["requested_oneshot"], True)
            self.assertEqual(record["requested_toolsets"], ["web"])
            self.assertEqual(record["requested_max_turns"], 8)
        command = run.call_args.args[0]
        self.assertIn("--oneshot", command)
        self.assertEqual(command[command.index("--toolsets") + 1], "web")
        self.assertEqual(command[command.index("--max-turns") + 1], "8")

    def test_attempt_two_manifest_binds_exact_saved_bytes_prompt_and_warning(self):
        first_bytes = b"not valid json on attempt one"
        accepted_bytes = payload()
        responses = [
            types.SimpleNamespace(returncode=0, stdout=first_bytes, stderr=b""),
            types.SimpleNamespace(
                returncode=7, stdout=accepted_bytes, stderr=b"synthetic nonzero warning"
            ),
        ]
        result, warning, run = self.run_item(item(41), "rerun-009", responses, 123)

        self.assertIsNotNone(result)
        self.assertIn("status 7", warning)
        manifest = self.manifest_for(result)
        attempt_dir = self.cache / "1234/41/rerun-009"
        stdout_path = attempt_dir / "hermes-attempt-2.stdout.txt"
        prompt_path = attempt_dir / "isolated-prompt.txt"
        self.assertEqual(Path(manifest["hermes_raw_output"]), stdout_path.relative_to(self.base))
        self.assertEqual(manifest["hermes_raw_output_sha256"], hashlib.sha256(accepted_bytes).hexdigest())
        self.assertEqual(stdout_path.read_bytes(), accepted_bytes)
        self.assertEqual(Path(manifest["prompt_path"]), prompt_path.relative_to(self.base))
        self.assertEqual(manifest["prompt_sha256"], hashlib.sha256(prompt_path.read_bytes()).hexdigest())
        self.assertEqual(manifest["execution_batch_id"], "rerun-009")
        self.assertEqual(manifest["successful_attempt"], 2)
        self.assertEqual(manifest["requested_model"], "gpt-6-luna")
        self.assertEqual(manifest["requested_reasoning"], "xhigh")
        self.assertEqual(manifest["requested_provider"], "openai-codex")
        self.assertIsNone(manifest["observed_model"])
        self.assertEqual(manifest["run_budget_seconds"], 123)
        self.assertEqual(manifest["subprocess_timeout_seconds"], 168)
        self.assertIn("status 7", result["execution_warning"])
        command = run.call_args.args[0]
        self.assertEqual(command[command.index("--provider") + 1], "openai-codex")
        self.assertEqual(command[command.index("--model") + 1], "gpt-6-luna")
        self.assertEqual(command[command.index("--reasoning") + 1], "xhigh")
        self.assertEqual(command[command.index("--toolsets") + 1], "web")
        self.assertIn("--oneshot", command)
        self.assertEqual(command[command.index("--max-turns") + 1], "8")
        self.assertEqual(command[command.index("--run-budget") + 1], "123")
        self.assertEqual(run.call_args.kwargs["timeout"], 168)

    def test_same_url_citations_keep_distinct_locator_and_period_bindings(self):
        atoms = [
            {"text": "synthetic 2024 disclosure", "status": "SUPPORTED", "period": "2024", "sources": [source("page 3, table 2", "2024")]},
            {"text": "synthetic 2025 disclosure", "status": "SUPPORTED", "period": "2025", "sources": [source("page 9, table 4", "2025")]},
        ]
        result, warning, _run = self.run_item(
            item(42), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=payload("PARTIAL", atoms), stderr=b"")]
        )
        self.assertIsNone(warning)
        manifest = self.manifest_for(result)
        self.assertEqual(len(manifest["sources"]), 2)
        self.assertNotEqual(result["atomic_claims"][0]["evidence_ids"], result["atomic_claims"][1]["evidence_ids"])
        self.assertEqual({src["locator"] for src in manifest["sources"]}, {"page 3, table 2", "page 9, table 4"})
        self.assertEqual({src["effective_period"] for src in manifest["sources"]}, {"2024", "2025"})

    def test_same_binding_keeps_distinct_stable_source_metadata_records(self):
        first = source("same page", "2024", "same note")
        second = source("same page", "2024", "same note")
        second.update({
            "source_title": "Different synthetic title",
            "source_level": 2,
            "source_sha256": "different-synthetic-hash",
            "raw_path": "synthetic/capture-two.pdf",
        })
        atoms = [
            {"text": "first synthetic atom", "status": "SUPPORTED", "period": "2024", "sources": [first]},
            {"text": "second synthetic atom", "status": "SUPPORTED", "period": "2024", "sources": [second]},
        ]
        result, warning, _run = self.run_item(
            item(48), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=payload("PARTIAL", atoms), stderr=b"")]
        )
        self.assertIsNone(warning)
        manifest = self.manifest_for(result)
        self.assertEqual(len(manifest["sources"]), 2)
        self.assertNotEqual(
            result["atomic_claims"][0]["evidence_ids"],
            result["atomic_claims"][1]["evidence_ids"],
        )
        self.assertEqual({src["title"] for src in manifest["sources"]}, {"Synthetic PDF", "Different synthetic title"})
        self.assertEqual({src["source_level"] for src in manifest["sources"]}, {2, 3})
        self.assertEqual({src["source_sha256"] for src in manifest["sources"]}, {None, "different-synthetic-hash"})
        self.assertEqual({src["raw_path"] for src in manifest["sources"]}, {None, "synthetic/capture-two.pdf"})

    def test_process_item_rejects_malformed_tickers_before_any_write_or_call(self):
        invalid_tickers = ["../123", "12/34", "/owned-outside-scratch", "12345", "１２３４", "", 1234, None]
        real_mkdir = Path.mkdir

        def mkdir_only_inside_fixture(path, *args, **kwargs):
            try:
                path.resolve().relative_to(self.base.resolve())
            except ValueError as exc:
                raise AssertionError("test guard prevented a write outside TMPDIR fixture") from exc
            return real_mkdir(path, *args, **kwargs)

        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            Path, "mkdir", new=mkdir_only_inside_fixture
        ):
            for ticker in invalid_tickers:
                with self.subTest(ticker=repr(ticker)), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run") as run:
                    with self.assertRaisesRegex(ValueError, "issuer_ticker"):
                        runner.process_item(item(49, ticker), 1, "rerun-009", False)
                    run.assert_not_called()
        self.assertFalse(list(self.base.rglob("isolated-prompt.txt")))

    def test_process_item_rejects_symlink_escape_from_cache(self):
        outside_target = self.base / "owned-outside-cache"
        outside_target.mkdir()
        ticker_dir = self.cache / "1234"
        ticker_dir.mkdir(parents=True)
        (ticker_dir / "51").symlink_to(outside_target, target_is_directory=True)
        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            runner, "STOP_EVENT", threading.Event()
        ), patch.object(runner.subprocess, "run") as run:
            with self.assertRaisesRegex(ValueError, "escapes CACHE"):
                runner.process_item(item(51), 1, "rerun-009", False)
            run.assert_not_called()
        self.assertFalse(list(outside_target.rglob("isolated-prompt.txt")))
        self.assertFalse(list(self.base.rglob("manifest.json")))

    def test_process_item_rejects_source_path_escape_before_any_write_or_call(self):
        real_mkdir = Path.mkdir

        def mkdir_only_inside_fixture(path, *args, **kwargs):
            try:
                path.resolve().relative_to(self.base.resolve())
            except ValueError as exc:
                raise AssertionError("test guard prevented a write outside TMPDIR fixture") from exc
            return real_mkdir(path, *args, **kwargs)

        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            Path, "mkdir", new=mkdir_only_inside_fixture
        ), patch.object(runner, "STOP_EVENT", threading.Event()), patch.object(
            runner.subprocess, "run"
        ) as run:
            with self.assertRaises(ValueError):
                runner.process_item(item(50), 1, "../../../../outside-scratch", False)
            run.assert_not_called()
        self.assertFalse(list(self.base.rglob("isolated-prompt.txt")))

    def test_main_failure_log_does_not_follow_known_escaped_cache_root(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        outside_cache = self.base / "outside-cache-target"
        outside_cache.mkdir()
        sentinel = outside_cache / "sentinel.txt"
        sentinel.write_bytes(b"controller-owned sentinel\n")
        cache.parent.mkdir(parents=True)
        cache.symlink_to(outside_cache, target_is_directory=True)

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            [types.SimpleNamespace(returncode=0, stdout=b"not used", stderr=b"")],
        )

        self.assertEqual(exit_code, 1)
        self.assertIn("Refusing unsafe runner failure log destination", stderr)
        run.assert_not_called()
        self.assertEqual(sentinel.read_bytes(), b"controller-owned sentinel\n")
        self.assertFalse((outside_cache / "runner-failures.jsonl").exists())

    def test_main_preflights_known_failure_log_leaf_symlink_before_request(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        cache.mkdir(parents=True)
        outside_leaf = self.base / "outside-failure-log-target.jsonl"
        outside_leaf.write_bytes(b"controller-owned sentinel\n")
        failure_path = cache / "runner-failures.jsonl"
        failure_path.symlink_to(outside_leaf)

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            [types.SimpleNamespace(returncode=0, stdout=b"not used", stderr=b"")],
        )

        self.assertEqual(exit_code, 1)
        self.assertIn("Refusing unsafe runner failure log destination", stderr)
        run.assert_not_called()
        self.assertEqual(outside_leaf.read_bytes(), b"controller-owned sentinel\n")

    def test_main_global_stop_rechecks_failure_log_leaf_replaced_during_request(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        cache.mkdir(parents=True)
        outside_leaf = self.base / "outside-global-stop-log.jsonl"
        outside_leaf.write_bytes(b"controller-owned sentinel\n")
        failure_path = cache / "runner-failures.jsonl"

        def replace_failure_log_leaf(_command, **_kwargs):
            failure_path.symlink_to(outside_leaf)
            return types.SimpleNamespace(
                returncode=0, stdout=b"HTTP 429 usage limit has been reached", stderr=b""
            )

        exit_code, stderr, stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            replace_failure_log_leaf,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(run.call_count, 1)
        self.assertIn("PAUSED seq=1: GLOBAL_STOP:", stdout)
        self.assertIn("Could not safely append runner failure log", stderr)
        self.assertEqual(outside_leaf.read_bytes(), b"controller-owned sentinel\n")
        self.assertFalse((root / "batches/batch-001.jsonl").exists())
        self.assertEqual(json.loads(checkpoint_path.read_text())["processed"], 0)

    def test_main_appends_failure_row_without_changing_existing_log_bytes(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        cache.mkdir(parents=True)
        failure_path = cache / "runner-failures.jsonl"
        prior_rows = b'{"prior":"synthetic row"}\r\n'
        failure_path.write_bytes(prior_rows)
        invalid_response = types.SimpleNamespace(returncode=0, stdout=b"invalid response", stderr=b"")

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            [invalid_response],
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(stderr, "")
        self.assertEqual(run.call_count, 1)
        self.assertTrue(failure_path.read_bytes().startswith(prior_rows))
        appended_lines = failure_path.read_bytes()[len(prior_rows):].splitlines()
        self.assertEqual(len(appended_lines), 1)
        failure_row = json.loads(appended_lines[0])
        self.assertEqual(failure_row["sequence"], 1)
        self.assertEqual(failure_row["claim_id"], item(1)["claim_id"])
        self.assertIn("required JSON object", failure_row["error"])

    def test_main_creates_missing_safe_failure_log(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        invalid_response = types.SimpleNamespace(returncode=0, stdout=b"invalid response", stderr=b"")

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            [invalid_response],
        )

        failure_path = cache / "runner-failures.jsonl"
        self.assertEqual(exit_code, 1)
        self.assertEqual(stderr, "")
        self.assertEqual(run.call_count, 1)
        self.assertTrue(failure_path.is_file())
        rows = [json.loads(line) for line in failure_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["sequence"], 1)

    def test_main_successful_real_worker_still_persists_candidate_result(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        successful_response = types.SimpleNamespace(returncode=0, stdout=payload(), stderr=b"")

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            [successful_response],
        )

        ledger_path = root / "batches/batch-001.jsonl"
        checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertEqual(run.call_count, 1)
        self.assertEqual(checkpoint["processed"], 1)
        self.assertEqual(checkpoint["remaining"], 0)
        self.assertEqual(len(ledger_path.read_text(encoding="utf-8").splitlines()), 1)
        self.assertFalse((cache / "runner-failures.jsonl").exists())

    def test_main_failure_log_rechecks_cache_root_swapped_during_request(self):
        base, root, cache, queue_path, checkpoint_path = self.prepare_main_fixture()
        outside_cache = self.base / "outside-cache-after-request"
        outside_cache.mkdir()
        sentinel = outside_cache / "sentinel.txt"
        sentinel.write_bytes(b"controller-owned sentinel\n")
        cache.parent.mkdir(parents=True)
        cache.mkdir()

        def replace_cache_root(_command, **_kwargs):
            cache.rename(self.base / "cache-before-swap")
            cache.symlink_to(outside_cache, target_is_directory=True)
            return types.SimpleNamespace(returncode=0, stdout=b"not valid JSON", stderr=b"")

        exit_code, stderr, _stdout, run = self.run_main(
            base, root, cache, queue_path, checkpoint_path,
            ["--workers", "1", "--attempts", "1", "--max-sequence", "1"],
            replace_cache_root,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(run.call_count, 1)
        self.assertIn("Could not safely append runner failure log", stderr)
        self.assertEqual(sentinel.read_bytes(), b"controller-owned sentinel\n")
        self.assertFalse((outside_cache / "runner-failures.jsonl").exists())
        self.assertFalse((root / "batches/batch-001.jsonl").exists())
        self.assertEqual(json.loads(checkpoint_path.read_text())["processed"], 0)

    def test_evidence_outputs_reject_existing_symlinks_for_every_verdict(self):
        cases = [(verdict, filename) for verdict in (
            "UNKNOWN", "PARTIAL", "CANDIDATE_ACCEPTED"
        ) for filename in ("manifest.json", "notes.md")]
        for index, (verdict, filename) in enumerate(cases):
            with self.subTest(verdict=verdict, destination=filename):
                case_dir = self.base / f"evidence-existing-{index}"
                base = case_dir / "base"
                base.mkdir(parents=True)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                evidence_dir = root / "evidence" / f"rerun-{index + 100:06d}"
                evidence_dir.mkdir(parents=True)
                outside = case_dir / "owned-outside-base.txt"
                outside.write_text("sentinel-before", encoding="utf-8")
                link = evidence_dir / filename
                link.symlink_to(outside)
                if verdict == "CANDIDATE_ACCEPTED":
                    response_bytes = payload(
                        verdict,
                        [{"text": "complete synthetic atom", "status": "SUPPORTED",
                          "period": "2024", "sources": [source()]}],
                        True,
                        True,
                    )
                else:
                    response_bytes = payload(verdict)
                run_response = types.SimpleNamespace(
                    returncode=0, stdout=response_bytes, stderr=b""
                )
                caught = None
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run", return_value=run_response) as run:
                    try:
                        runner.process_item(
                            item(index + 100), 1, "rerun-009", False
                        )
                    except ValueError as exc:
                        caught = exc
                self.assertTrue(link.is_symlink())
                self.assertEqual(
                    outside.read_text(encoding="utf-8"), "sentinel-before",
                    "evidence output symlink overwrote the outside sentinel",
                )
                self.assertFalse(list(cache.rglob("isolated-prompt.txt")))
                run.assert_not_called()
                self.assertIsNotNone(caught, "unsafe evidence symlink was not refused")
                self.assertRegex(str(caught), "evidence.*(symlink|escape|unsafe)|symlink.*evidence")

    def test_evidence_output_rechecks_symlinks_created_by_subprocess(self):
        for filename in ("manifest.json", "notes.md"):
            with self.subTest(destination=filename):
                case_dir = self.base / f"evidence-late-{filename.replace('.', '-') }"
                base = case_dir / "base"
                base.mkdir(parents=True)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                evidence_dir = root / "evidence" / "rerun-000201"
                outside = case_dir / "owned-outside-base.txt"
                outside.write_text("sentinel-before", encoding="utf-8")

                def create_escape(*_args, **_kwargs):
                    evidence_dir.mkdir(parents=True)
                    (evidence_dir / filename).symlink_to(outside)
                    return types.SimpleNamespace(
                        returncode=0, stdout=payload("PARTIAL"), stderr=b""
                    )

                caught = None
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run", side_effect=create_escape) as run:
                    try:
                        runner.process_item(item(201), 1, "rerun-009", False)
                    except ValueError as exc:
                        caught = exc
                self.assertEqual(run.call_count, 1)
                self.assertTrue((evidence_dir / filename).is_symlink())
                self.assertEqual(
                    outside.read_text(encoding="utf-8"), "sentinel-before",
                    "post-request evidence write followed an introduced symlink",
                )
                self.assertIsNotNone(caught, "post-request evidence symlink was not refused")
                self.assertRegex(str(caught), "evidence.*(symlink|escape|unsafe)|symlink.*evidence")

    def test_evidence_root_and_claim_directory_symlink_escapes_fail_before_request(self):
        for location in ("evidence-root", "claim-directory"):
            with self.subTest(location=location):
                case_dir = self.base / f"evidence-dir-{location}"
                base = case_dir / "base"
                base.mkdir(parents=True)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                outside = case_dir / "owned-outside-base"
                outside.mkdir()
                if location == "evidence-root":
                    root.mkdir(parents=True)
                    (root / "evidence").symlink_to(outside, target_is_directory=True)
                else:
                    (root / "evidence").mkdir(parents=True)
                    (root / "evidence/rerun-000202").symlink_to(
                        outside, target_is_directory=True
                    )
                caught = None
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run") as run:
                    try:
                        runner.process_item(item(202), 1, "rerun-009", False)
                    except ValueError as exc:
                        caught = exc
                self.assertEqual(
                    list(outside.iterdir()), [],
                    "evidence directory symlink received runner output",
                )
                run.assert_not_called()
                self.assertIsNotNone(caught, "evidence directory symlink was not refused")
                self.assertRegex(str(caught), "evidence.*(symlink|escape|unsafe)|symlink.*evidence")

    def test_cache_root_symlink_escape_is_rejected_before_prompt_or_request(self):
        case_dir = self.base / "cache-root-symlink"
        base = case_dir / "base"
        base.mkdir(parents=True)
        root = base / "audit-v5/semantic/candidate-rerun"
        cache_parent = base / "audit-v5/source-cache"
        cache_parent.mkdir(parents=True)
        outside = case_dir / "owned-outside-base"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_text("sentinel-before", encoding="utf-8")
        cache = cache_parent / "candidate-rerun"
        cache.symlink_to(outside, target_is_directory=True)

        caught = None
        with patch.object(runner, "BASE", base), patch.object(
            runner, "ROOT", root
        ), patch.object(runner, "CACHE", cache), patch.object(
            runner, "STOP_EVENT", threading.Event()
        ), patch.object(runner.subprocess, "run") as run:
            try:
                runner.process_item(item(203), 1, "rerun-009", False)
            except ValueError as exc:
                caught = exc

        self.assertTrue(cache.is_symlink())
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "sentinel-before")
        self.assertFalse(
            list(outside.rglob("isolated-prompt.txt")),
            "external cache root received an isolated prompt",
        )
        run.assert_not_called()
        self.assertIsNotNone(caught, "external cache root was not refused")
        self.assertRegex(str(caught), "CACHE.*(symlink|escape|unsafe)")

    def test_cache_prompt_and_existing_attempt_symlinks_are_rejected_before_request(self):
        for target_name in (
            "isolated-prompt.txt",
            "hermes-attempt-1.stdout.txt",
            "hermes-attempt-1.stderr.txt",
        ):
            with self.subTest(destination=target_name):
                case_dir = self.base / f"cache-existing-{target_name.replace('.', '-') }"
                base = case_dir / "base"
                base.mkdir(parents=True)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                candidate_dir = cache / "1234/204/rerun-009"
                candidate_dir.mkdir(parents=True)
                outside = case_dir / "owned-outside-base.txt"
                outside.write_text("sentinel-before", encoding="utf-8")
                (candidate_dir / target_name).symlink_to(outside)
                caught = None
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run") as run:
                    try:
                        runner.process_item(item(204), 1, "rerun-009", False)
                    except ValueError as exc:
                        caught = exc
                self.assertTrue((candidate_dir / target_name).is_symlink())
                self.assertEqual(
                    outside.read_text(encoding="utf-8"), "sentinel-before",
                    "cache output symlink overwrote the outside sentinel",
                )
                run.assert_not_called()
                self.assertIsNotNone(caught, "existing cache output symlink was not refused")
                self.assertRegex(str(caught), "(CACHE|prompt|attempt).*(symlink|escape|unsafe)")

    def test_cache_attempt_outputs_recheck_symlinks_created_by_subprocess(self):
        for target_name, stderr in (
            ("hermes-attempt-1.stdout.txt", b""),
            ("hermes-attempt-1.stderr.txt", b"synthetic stderr"),
        ):
            with self.subTest(destination=target_name):
                case_dir = self.base / f"cache-late-{target_name.replace('.', '-') }"
                base = case_dir / "base"
                base.mkdir(parents=True)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                candidate_dir = cache / "1234/205/rerun-009"
                outside = case_dir / "owned-outside-base.txt"
                outside.write_text("sentinel-before", encoding="utf-8")

                def create_escape(*_args, **_kwargs):
                    candidate_dir.mkdir(parents=True, exist_ok=True)
                    (candidate_dir / target_name).symlink_to(outside)
                    return types.SimpleNamespace(
                        returncode=0, stdout=payload("PARTIAL"), stderr=stderr
                    )

                caught = None
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "STOP_EVENT", threading.Event()
                ), patch.object(runner.subprocess, "run", side_effect=create_escape) as run:
                    try:
                        runner.process_item(item(205), 1, "rerun-009", False)
                    except ValueError as exc:
                        caught = exc
                self.assertEqual(run.call_count, 1)
                self.assertTrue((candidate_dir / target_name).is_symlink())
                self.assertEqual(
                    outside.read_text(encoding="utf-8"), "sentinel-before",
                    "post-request attempt write followed an introduced symlink",
                )
                self.assertIsNotNone(caught, "post-request attempt symlink was not refused")
                self.assertRegex(str(caught), "attempt.*(symlink|escape|unsafe)")

    def test_later_batch_and_resume_attempts_do_not_overwrite_saved_stdout(self):
        first = payload()
        result_one, _, _ = self.run_item(
            item(43), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=first, stderr=b"")]
        )
        stdout_one = self.cache / "1234/43/rerun-009/hermes-attempt-1.stdout.txt"
        self.assertEqual(stdout_one.read_bytes(), first)
        later = payload("PARTIAL", [{"text": "new synthetic claim", "status": "UNKNOWN", "sources": []}])
        result_two, _, _ = self.run_item(
            item(43), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=later, stderr=b"")]
        )
        result_other_batch, _, _ = self.run_item(
            item(43), "rerun-010", [types.SimpleNamespace(returncode=0, stdout=later, stderr=b"")], superseding=True
        )
        self.assertEqual(stdout_one.read_bytes(), first)
        self.assertEqual(result_one["rerun_batch_id"], "rerun-009")
        self.assertEqual(result_two["rerun_batch_id"], "rerun-009")
        self.assertEqual(result_other_batch["rerun_batch_id"], "rerun-010")
        manifest_two = self.manifest_for(result_two)
        manifest_other = self.manifest_for(result_other_batch)
        self.assertEqual(manifest_two["successful_attempt"], 2)
        self.assertNotEqual(manifest_two["hermes_raw_output"], manifest_other["hermes_raw_output"])

    def test_candidate_gate_never_writes_final_accepted_and_requires_full_evidence(self):
        supported_atoms = [{
            "text": "complete synthetic original atom",
            "status": "SUPPORTED",
            "period": "2024",
            "sources": [source()],
        }]
        accepted_payload = payload("ACCEPTED", supported_atoms, True, True)
        accepted, _, _ = self.run_item(
            item(44), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=accepted_payload, stderr=b"")]
        )
        self.assertEqual(accepted["verdict"], "CANDIDATE_ACCEPTED")
        self.assertTrue(accepted["candidate_accepted"])
        self.assertTrue(accepted["requires_final_adjudication"])
        self.assertNotEqual(accepted["verdict"], "ACCEPTED")

        incomplete_atoms = [
            {"text": "supported synthetic atom", "status": "SUPPORTED", "sources": [source()]},
            {"text": "unsupported original qualifier", "status": "UNKNOWN", "sources": []},
        ]
        incomplete, _, _ = self.run_item(
            item(45), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=payload("CANDIDATE_ACCEPTED", incomplete_atoms, True, True), stderr=b"")]
        )
        self.assertEqual(incomplete["verdict"], "PARTIAL")
        self.assertFalse(incomplete["candidate_accepted"])
        self.assertFalse(incomplete["requires_final_adjudication"])
        self.assertTrue(all(a["status"] == "SUPPORTED" and a["evidence_ids"] for a in accepted["atomic_claims"]))

    def test_operational_timeout_returns_no_candidate_row_or_fabricated_unknown(self):
        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            runner, "STOP_EVENT", threading.Event()
        ), patch.object(runner.subprocess, "run", side_effect=TimeoutError("synthetic timeout")), patch.object(
            runner.time, "sleep"
        ):
            result, warning = runner.process_item(item(46), 2, "rerun-009", False)
        self.assertIsNone(result)
        self.assertIn("TimeoutError", warning)
        self.assertFalse(list(self.root.glob("batches/batch-*.jsonl")))

    def test_main_passes_cli_run_budget_to_worker_without_calling_hermes(self):
        queue_path = self.root / "queue.jsonl"
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "batches").mkdir()
        queue_path.write_text("synthetic queue fixture\n", encoding="utf-8")
        checkpoint_path = self.root / "checkpoint.json"
        checkpoint_path.write_text(json.dumps({
            "queued": 1,
            "processed": 0,
            "remaining": 1,
            "verdict_counts": {"PARTIAL": 0, "CANDIDATE_ACCEPTED": 0, "UNKNOWN": 0},
            "queue_sha256": runner.sha_bytes(queue_path.read_bytes()),
            "current_rerun_batch": "rerun-001",
        }), encoding="utf-8")
        captured = []

        def fake_process(claim, attempts, batch, superseding, run_budget_seconds):
            captured.append((attempts, batch, superseding, run_budget_seconds))
            return ({
                "queue_sequence": claim["queue_sequence"],
                "rerun_batch_id": batch,
                "rerun_id": "synthetic-main-result",
                "reviewed_at": "2020-01-01T00:00:00Z",
                "verdict": "UNKNOWN",
                "claim": {
                    "claim_id": claim["claim_id"],
                    "normalized_claim_hash": claim["normalized_claim_hash"],
                    "issuer_ticker": claim["issuer_ticker"],
                    "issuer_company": claim["issuer_company"],
                    "report_path": claim["report_path"],
                    "original_text": claim["claim"],
                    "author_batch_id": claim["author_batch_id"],
                    "author_batch_path": claim["author_batch_path"],
                    "author_batch_sha256": claim["author_batch_sha256"],
                    "author_decision": claim["author_decision"],
                },
            }, None)

        with patch.object(runner, "BASE", self.base), patch.object(
            runner, "ROOT", self.root
        ), patch.object(runner, "CACHE", self.cache), patch.object(
            runner, "QUEUE_PATH", queue_path
        ), patch.object(runner, "CHECKPOINT_PATH", checkpoint_path), patch.object(
            runner, "read_queue", return_value=[item(1)]
        ), patch.object(runner, "process_item", side_effect=fake_process), patch.object(
            sys, "argv", ["run_hermes_batch.py", "--workers", "1", "--run-budget", "73"]
        ):
            self.assertEqual(runner.main(), 0)
        self.assertEqual(captured, [(2, "rerun-001", False, 73)])

    def test_main_rejects_duplicate_and_invalid_queue_sequences_before_workers(self):
        cases = [
            ([item(1), item(1)], "duplicate"),
            ([item(0)], "positive integer"),
            ([item(True)], "positive integer"),
            ([item("1")], "positive integer"),
            ([item(1.0)], "positive integer"),
            ([{**item(1), "author_batch_path": ""}], "required identity"),
        ]
        for queued_items, _label in cases:
            with self.subTest(queue=queued_items), tempfile.TemporaryDirectory(
                prefix="candidate-queue-", dir=os.environ["TMPDIR"]
            ) as temp:
                base = Path(temp)
                root = base / "audit-v5/semantic/candidate-rerun"
                cache = base / "audit-v5/source-cache/candidate-rerun"
                root.mkdir(parents=True)
                queue_path = root / "queue.jsonl"
                queue_path.write_text("synthetic frozen queue\n", encoding="utf-8")
                checkpoint_path = root / "checkpoint.json"
                checkpoint_path.write_text(json.dumps({
                    "queued": len(queued_items),
                    "processed": 0,
                    "remaining": len(queued_items),
                    "verdict_counts": {"PARTIAL": 0, "CANDIDATE_ACCEPTED": 0, "UNKNOWN": 0},
                    "queue_sha256": runner.sha_bytes(queue_path.read_bytes()),
                    "current_rerun_batch": "rerun-001",
                }), encoding="utf-8")
                with patch.object(runner, "BASE", base), patch.object(
                    runner, "ROOT", root
                ), patch.object(runner, "CACHE", cache), patch.object(
                    runner, "QUEUE_PATH", queue_path
                ), patch.object(runner, "CHECKPOINT_PATH", checkpoint_path), patch.object(
                    runner, "read_queue", return_value=queued_items
                ), patch.object(runner, "process_item") as process, patch.object(
                    sys, "argv", ["run_hermes_batch.py", "--workers", "1"]
                ), redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit):
                        runner.main()
                process.assert_not_called()
                self.assertFalse(list(root.glob("evidence/**/manifest.json")))
                self.assertFalse(list(cache.rglob("isolated-prompt.txt")))

    def test_default_run_budget_remains_420_seconds(self):
        stdout = payload()
        result, _, run = self.run_item(
            item(47), "rerun-009", [types.SimpleNamespace(returncode=0, stdout=stdout, stderr=b"")]
        )
        manifest = self.manifest_for(result)
        self.assertEqual(manifest["run_budget_seconds"], 420)
        self.assertEqual(manifest["subprocess_timeout_seconds"], 465)
        self.assertEqual(run.call_args.args[0][run.call_args.args[0].index("--run-budget") + 1], "420")

    def test_nonpositive_run_budget_is_rejected(self):
        stderr = io.StringIO()
        with patch.object(sys, "argv", ["run_hermes_batch.py", "--run-budget", "0"]), redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as raised:
                runner.main()
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("must be a positive integer", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
