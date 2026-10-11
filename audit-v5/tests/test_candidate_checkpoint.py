from __future__ import annotations

import importlib.util
import hashlib
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "candidate_runner_checkpoint_test",
    REPO / "audit-v5/semantic/candidate-rerun/run_hermes_batch.py",
)
runner = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runner
SPEC.loader.exec_module(runner)


def queue_item(seq: int) -> dict:
    return {
        "queue_sequence": seq,
        "claim_id": f"synthetic-claim-{seq}",
        "normalized_claim_hash": f"synthetic-hash-{seq}",
        "issuer_ticker": "1234",
        "issuer_company": "Synthetic Issuer",
        "report_path": f"synthetic/report-{seq}.md",
        "claim": "Synthetic original claim [[波音]]",
        "author_batch_id": "synthetic-author-batch",
        "author_batch_path": "synthetic/author.json",
        "author_batch_sha256": "synthetic-author-hash",
        "author_decision": "PARTIALLY_SUPPORTED",
    }


def result(seq: int, batch: str, verdict: str, result_id: str) -> dict:
    queued = queue_item(seq)
    row = {
        "queue_sequence": seq,
        "rerun_batch_id": batch,
        "rerun_id": result_id,
        "reviewed_at": "2020-01-01T00:00:00Z",
        "verdict": verdict,
        "claim": {
            "claim_id": queued["claim_id"],
            "normalized_claim_hash": queued["normalized_claim_hash"],
            "issuer_ticker": queued["issuer_ticker"],
            "issuer_company": queued["issuer_company"],
            "report_path": queued["report_path"],
            "original_text": queued["claim"],
            "author_batch_id": queued["author_batch_id"],
            "author_batch_path": queued["author_batch_path"],
            "author_batch_sha256": queued["author_batch_sha256"],
            "author_decision": queued["author_decision"],
        },
    }
    if verdict == "CANDIDATE_ACCEPTED":
        row.update({
            "candidate_accepted": True,
            "requires_final_adjudication": True,
            "atomic_claims": [{"status": "SUPPORTED", "evidence_ids": ["synthetic-evidence"]}],
            "evidence_manifest": (
                f"audit-v5/semantic/candidate-rerun/evidence/{result_id}/manifest.json"
            ),
        })
    return row


def fixture_layout(temp: str, queued_items: list[dict] | None = None):
    base = Path(temp)
    root = base / "audit-v5/semantic/candidate-rerun"
    cache = base / "audit-v5/source-cache/candidate-rerun"
    queue_path = root / "queue.jsonl"
    checkpoint_path = root / "checkpoint.json"
    (root / "batches").mkdir(parents=True, exist_ok=True)
    (root / "evidence").mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    items = [queue_item(1)] if queued_items is None else queued_items
    queue_path.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in items),
        encoding="utf-8",
    )
    return base, root, cache, queue_path, checkpoint_path


def write_manifest(base: Path, row: dict, source_ids=None, *, claim_id=None, claim_hash=None,
                   sources=None) -> Path:
    if sources is None:
        source_ids = ["synthetic-evidence"] if source_ids is None else source_ids
        sources = [{"source_id": source_id} for source_id in source_ids]
    manifest = {
        "schema": "semantic-candidate-evidence-manifest-1",
        "claim_id": row["claim"]["claim_id"] if claim_id is None else claim_id,
        "normalized_claim_hash": (
            row["claim"]["normalized_claim_hash"] if claim_hash is None else claim_hash
        ),
        "sources": sources,
    }
    path = base / row["evidence_manifest"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


class CandidateCheckpointTests(unittest.TestCase):
    def assert_rejected_without_mutation(self, invalid_row, expected_message):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
            ledger_path = root / "batches/batch-001.jsonl"
            ledger_path.write_text(
                json.dumps(result(1, "rerun-001", "UNKNOWN", "synthetic-existing"), separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
            checkpoint_path.write_bytes(b'{"queued":1,"preserved":"same"}\n')
            original_ledger = ledger_path.read_bytes()
            original_checkpoint = checkpoint_path.read_bytes()

            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                with self.assertRaisesRegex(ValueError, expected_message):
                    runner.persist_result(invalid_row, True)

            self.assertEqual(ledger_path.read_bytes(), original_ledger)
            self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def assert_candidate_persist_rejected_without_mutation(
        self, invalid_row, expected_message, manifest_writer=None
    ):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
            ledger_path = root / "batches/batch-001.jsonl"
            ledger_path.write_text(
                json.dumps(result(1, "rerun-001", "UNKNOWN", "synthetic-existing"), separators=(",", ":")) + "\n",
                encoding="utf-8",
            )
            checkpoint_path.write_bytes(b'{"queued":1,"preserved":"same"}\n')
            if manifest_writer is not None:
                manifest_writer(base, root, invalid_row)
            original_ledger = ledger_path.read_bytes()
            original_checkpoint = checkpoint_path.read_bytes()

            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                with self.assertRaisesRegex(ValueError, expected_message):
                    runner.persist_result(invalid_row, True)

            self.assertEqual(ledger_path.read_bytes(), original_ledger)
            self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def test_persistence_rejects_unbound_candidate_evidence_ids_before_any_write(self):
        without_manifest = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-no-manifest")
        without_manifest.pop("evidence_manifest")
        with self.subTest(case="missing-reference"):
            self.assert_candidate_persist_rejected_without_mutation(without_manifest, "manifest|evidence")

        partially_bound = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-partial-binding")
        partially_bound["atomic_claims"][0]["evidence_ids"] = [
            "synthetic-evidence", "synthetic-not-in-manifest"
        ]

        def one_id_manifest(base, _root, row):
            write_manifest(base, row, ["synthetic-evidence"])

        with self.subTest(case="one-unbound-among-valid-ids"):
            self.assert_candidate_persist_rejected_without_mutation(
                partially_bound, "manifest|evidence", one_id_manifest
            )

    def test_candidate_manifest_rejects_missing_sources_and_wrong_claim(self):
        cases = [
            ("missing-sources", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                                  "normalized_claim_hash": "synthetic-hash-1"}),
            ("malformed-sources", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                                    "normalized_claim_hash": "synthetic-hash-1", "sources": "bad"}),
            ("non-object", ["not", "an", "object"]),
            ("invalid-json", None),
            ("wrong-claim", {"schema": "synthetic", "claim_id": "other-claim",
                              "normalized_claim_hash": "synthetic-hash-1",
                              "sources": [{"source_id": "synthetic-evidence"}]}),
            ("wrong-hash", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                             "normalized_claim_hash": "other-hash",
                             "sources": [{"source_id": "synthetic-evidence"}]}),
            ("unknown-source-id", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                                    "normalized_claim_hash": "synthetic-hash-1",
                                    "sources": [{"source_id": "different-evidence"}]}),
            ("malformed-source", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                                   "normalized_claim_hash": "synthetic-hash-1",
                                   "sources": ["not-an-object"]}),
            ("missing-source-id", {"schema": "synthetic", "claim_id": "synthetic-claim-1",
                                    "normalized_claim_hash": "synthetic-hash-1", "sources": [{}]}),
        ]
        for label, manifest in cases:
            with self.subTest(case=label):
                row = result(1, "rerun-001", "CANDIDATE_ACCEPTED", f"synthetic-{label}")

                def write_case(base, _root, candidate):
                    path = base / candidate["evidence_manifest"]
                    path.parent.mkdir(parents=True, exist_ok=True)
                    content = "{invalid json\n" if manifest is None else json.dumps(manifest) + "\n"
                    path.write_text(content, encoding="utf-8")

                self.assert_candidate_persist_rejected_without_mutation(
                    row, "manifest|evidence", write_case
                )

    def test_candidate_manifest_rejects_missing_file(self):
        missing = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-missing-file")
        self.assert_candidate_persist_rejected_without_mutation(missing, "manifest|evidence")

    def test_candidate_manifest_rejects_unsafe_references(self):
        for label, reference in (
            ("absolute", "{base}/outside-manifest.json"),
            ("traversal", "audit-v5/semantic/candidate-rerun/evidence/../outside-manifest.json"),
            ("symlink-escape", "audit-v5/semantic/candidate-rerun/evidence/symlink-manifest.json"),
        ):
            with self.subTest(reference=label):
                row = result(1, "rerun-001", "CANDIDATE_ACCEPTED", f"synthetic-unsafe-{label}")

                def write_unsafe(base, root, candidate):
                    target = base / "outside-manifest.json"
                    manifest = {
                        "claim_id": candidate["claim"]["claim_id"],
                        "normalized_claim_hash": candidate["claim"]["normalized_claim_hash"],
                        "sources": [{"source_id": "synthetic-evidence"}],
                    }
                    target.write_text(json.dumps(manifest), encoding="utf-8")
                    if label == "absolute":
                        candidate["evidence_manifest"] = reference.format(base=target)
                    elif label == "traversal":
                        candidate["evidence_manifest"] = reference
                        nested_target = root / "outside-manifest.json"
                        nested_target.write_text(json.dumps(manifest), encoding="utf-8")
                    else:
                        candidate["evidence_manifest"] = reference
                        link = root / "evidence/symlink-manifest.json"
                        link.symlink_to(target)

                self.assert_candidate_persist_rejected_without_mutation(
                    row, "manifest|evidence", write_unsafe
                )

    def test_loaded_candidate_requires_manifest_for_read_and_reconcile(self):
        row = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-ledger-no-manifest")
        for operation in ("read", "reconcile", "resume"):
            with self.subTest(operation=operation), tempfile.TemporaryDirectory(
                prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
            ) as temp:
                base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
                ledger = root / "batches/batch-001.jsonl"
                ledger.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
                checkpoint_path.write_text(json.dumps({
                    "queued": 1,
                    "processed": 0,
                    "preserved": "same",
                    "current_rerun_batch": "rerun-001",
                    "queue_sha256": runner.sha_bytes(queue_path.read_bytes()),
                }) + "\n", encoding="utf-8")
                original_checkpoint = checkpoint_path.read_bytes()
                with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                    QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                    if operation == "resume":
                        opened_locks = []
                        real_open = Path.open

                        def track_runner_lock(path, *args, **kwargs):
                            handle = real_open(path, *args, **kwargs)
                            if path.name == "runner.lock":
                                opened_locks.append(handle)
                            return handle

                        with patch.object(Path, "open", new=track_runner_lock):
                            with patch.object(sys, "argv", ["run_hermes_batch.py", "--workers", "1"]):
                                with self.assertRaisesRegex(ValueError, "manifest|evidence"):
                                    runner.main()
                        for handle in opened_locks:
                            handle.close()
                    else:
                        with self.assertRaisesRegex(ValueError, "manifest|evidence"):
                            if operation == "read":
                                runner.all_results()
                            else:
                                runner.reconcile_checkpoint()
                self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def test_bound_candidate_persists_rereads_and_remains_deduped(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
            checkpoint_path.write_text(json.dumps({"queued": 1}), encoding="utf-8")
            row = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-bound-candidate")
            row["atomic_claims"] = [
                {"status": "SUPPORTED", "evidence_ids": ["synthetic-evidence", "second-evidence"]}
            ]
            write_manifest(base, row, ["synthetic-evidence", "second-evidence"])
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                self.assertTrue(runner.persist_result(row))
                first_ledger = (root / "batches/batch-001.jsonl").read_bytes()
                first_checkpoint = checkpoint_path.read_bytes()
                loaded = runner.all_results()
                self.assertEqual(len(loaded), 1)
                self.assertIs(loaded[0]["candidate_accepted"], True)
                self.assertIs(loaded[0]["requires_final_adjudication"], True)
                self.assertFalse(runner.persist_result(row))
                reconciled = runner.reconcile_checkpoint()
            self.assertEqual((root / "batches/batch-001.jsonl").read_bytes(), first_ledger)
            self.assertEqual(checkpoint_path.read_bytes(), first_checkpoint)
            self.assertEqual(reconciled["verdict_counts"]["CANDIDATE_ACCEPTED"], 1)
            self.assertEqual(reconciled["processed"], 1)

    def test_persistence_rejects_final_accepted_before_any_write(self):
        invalid = result(1, "rerun-001", "ACCEPTED", "synthetic-final-accepted")
        self.assert_rejected_without_mutation(invalid, "Unsupported persistence verdict")

    def test_persistence_rejects_ungated_or_unsupported_candidates_before_any_write(self):
        ungated = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-ungated")
        ungated["requires_final_adjudication"] = False
        unsupported = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-unsupported")
        unsupported["atomic_claims"][0]["status"] = "UNKNOWN"
        unsupported["atomic_claims"][0]["evidence_ids"] = []

        for invalid in (ungated, unsupported):
            with self.subTest(result_id=invalid["rerun_id"]):
                self.assert_rejected_without_mutation(
                    invalid, "CANDIDATE_ACCEPTED requires a true final-adjudication gate and supported evidence"
                )

    def test_cross_batch_supersession_counts_latest_row_and_preserves_append(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            original = result(1, "rerun-008", "PARTIAL", "synthetic-original")
            original_line = json.dumps(original, separators=(",", ":")) + "\n"
            old_batch = root / "batches/batch-008.jsonl"
            old_batch.write_text(original_line, encoding="utf-8")
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(
                json.dumps({"queued": 1, "preserved_metadata": "keep"}),
                encoding="utf-8",
            )
            replacement = result(
                1, "rerun-009", "UNKNOWN", "synthetic-replacement"
            )

            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                self.assertTrue(runner.persist_result(replacement, True))

            saved = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["processed"], 1)
            self.assertEqual(saved["remaining"], 0)
            self.assertEqual(sum(saved["verdict_counts"].values()), 1)
            self.assertEqual(saved["verdict_counts"]["PARTIAL"], 0)
            self.assertEqual(saved["verdict_counts"]["UNKNOWN"], 1)
            self.assertEqual(saved["current_batch_processed"], 1)
            self.assertEqual(saved["preserved_metadata"], "keep")
            self.assertNotEqual(saved["updated_at"], replacement["reviewed_at"])
            self.assertEqual(old_batch.read_text(encoding="utf-8"), original_line)
            new_rows = [
                json.loads(line)
                for line in (root / "batches/batch-009.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(len(new_rows), 1)
            self.assertEqual(new_rows[0]["rerun_id"], "synthetic-replacement")

    def test_checkpoint_uses_fsynced_same_directory_atomic_replace(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(json.dumps({"queued": 1}), encoding="utf-8")
            observed = []
            actual_replace = os.replace

            def record_replace(source, destination):
                source_path = Path(source)
                destination_path = Path(destination)
                observed.append((source_path.parent, destination_path.parent, destination_path))
                self.assertTrue(source_path.read_text(encoding="utf-8").endswith("\n"))
                actual_replace(source, destination)

            row = result(1, "rerun-009", "UNKNOWN", "synthetic-atomic-write")
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner.os, "replace", side_effect=record_replace) as replace_mock, patch.object(
                runner.os, "fsync", wraps=os.fsync
            ) as fsync_mock, patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                self.assertTrue(runner.persist_result(row))
            self.assertEqual(replace_mock.call_count, 1)
            self.assertGreaterEqual(fsync_mock.call_count, 2)
            self.assertEqual(observed, [(checkpoint_path.parent, checkpoint_path.parent, checkpoint_path)])

    def test_same_batch_duplicate_result_is_idempotent(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(json.dumps({"queued": 1}), encoding="utf-8")
            row = result(1, "rerun-009", "UNKNOWN", "synthetic-same-batch")
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                self.assertTrue(runner.persist_result(row, True))
                self.assertFalse(runner.persist_result(row, True))
            rows = (root / "batches/batch-009.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(rows), 1)

    def test_concurrent_distinct_and_superseding_writes_keep_effective_counts(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            queued_items = [queue_item(1), queue_item(2), queue_item(3)]
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp, queued_items)
            original = result(1, "rerun-007", "PARTIAL", "synthetic-prior")
            old_path = root / "batches/batch-007.jsonl"
            old_line = json.dumps(original, separators=(",", ":")) + "\n"
            old_path.write_text(old_line, encoding="utf-8")
            checkpoint_path.write_text(json.dumps({"queued": 3}), encoding="utf-8")
            writes = [
                result(1, "rerun-008", "UNKNOWN", "synthetic-replacement"),
                result(2, "rerun-008", "PARTIAL", "synthetic-distinct-2"),
                result(3, "rerun-008", "CANDIDATE_ACCEPTED", "synthetic-distinct-3"),
            ]
            write_manifest(base, writes[2])

            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path), ThreadPoolExecutor(max_workers=3) as pool:
                futures = [pool.submit(runner.persist_result, row, True) for row in writes]
                self.assertEqual([f.result() for f in futures], [True, True, True])

            saved = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            physical = [
                json.loads(line)
                for path in sorted((root / "batches").glob("batch-*.jsonl"))
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            effective = {row["queue_sequence"]: row for row in runner.effective_result_projection(physical)}
            self.assertEqual(len(physical), 4)
            self.assertEqual(old_path.read_text(encoding="utf-8"), old_line)
            self.assertEqual(len(effective), 3)
            self.assertEqual(saved["processed"], 3)
            self.assertEqual(saved["remaining"], 0)
            self.assertEqual(saved["completed_through_sequence"], 3)
            self.assertEqual(sum(saved["verdict_counts"].values()), 3)
            self.assertEqual(saved["verdict_counts"]["PARTIAL"], 1)
            self.assertEqual(saved["verdict_counts"]["UNKNOWN"], 1)
            self.assertEqual(saved["verdict_counts"]["CANDIDATE_ACCEPTED"], 1)
            self.assertEqual(saved["current_batch_processed"], 3)

    def test_malformed_or_truncated_ledger_fails_closed_without_rewrite(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            ledger = root / "batches/batch-001.jsonl"
            valid_row = json.dumps(result(1, "rerun-001", "UNKNOWN", "synthetic-before-truncation"))
            ledger.write_text(valid_row + "\n{\"broken\"", encoding="utf-8")
            original_ledger = ledger.read_bytes()
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(json.dumps({"queued": 1, "processed": 0}), encoding="utf-8")
            original_checkpoint = checkpoint_path.read_bytes()
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                with self.assertRaisesRegex(ValueError, "Malformed result ledger row"):
                    runner.reconcile_checkpoint()
            self.assertEqual(ledger.read_bytes(), original_ledger)
            self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def assert_ledger_rejected_without_checkpoint_rewrite(self, row, message):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            ledger = root / "batches/batch-001.jsonl"
            ledger.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_bytes(b'{"queued":1,"processed":0,"preserved":"same"}\n')
            original_checkpoint = checkpoint_path.read_bytes()
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                with self.assertRaisesRegex(ValueError, message):
                    runner.reconcile_checkpoint()
            self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def test_loaded_forbidden_verdict_fails_closed(self):
        self.assert_ledger_rejected_without_checkpoint_rewrite(
            result(1, "rerun-001", "ACCEPTED", "synthetic-final-accepted"),
            "Unsupported result verdict",
        )

    def test_loaded_out_of_queue_sequence_fails_closed(self):
        self.assert_ledger_rejected_without_checkpoint_rewrite(
            result(2, "rerun-001", "UNKNOWN", "synthetic-foreign-sequence"),
            "not present in frozen queue",
        )

    def test_loaded_wrong_claim_identity_fails_closed(self):
        row = result(1, "rerun-001", "UNKNOWN", "synthetic-wrong-identity")
        row["claim"]["claim_id"] = "foreign-claim-id"
        self.assert_ledger_rejected_without_checkpoint_rewrite(row, "claim identity mismatch")

    def test_legacy_compatible_row_preserves_historical_display_whitespace(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
            row = result(1, "rerun-001", "CANDIDATE_ACCEPTED", "synthetic-legacy-candidate")
            row["claim"]["original_text"] = "Synthetic original claim  [[波音]]"
            write_manifest(base, row)
            ledger_line = (json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
            ledger = root / "batches/batch-001.jsonl"
            ledger.write_bytes(ledger_line)
            checkpoint_path.write_text(json.dumps({"queued": 1, "processed": 0}), encoding="utf-8")
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                saved = runner.reconcile_checkpoint()
                loaded = runner.all_results()
            self.assertEqual(saved["processed"], 1)
            self.assertEqual(saved["latest_result_sha256"], hashlib.sha256(ledger_line).hexdigest())
            self.assertEqual(loaded[0]["claim"]["original_text"], "Synthetic original claim  [[波音]]")
            self.assertEqual(ledger.read_bytes(), ledger_line)

    def test_empty_ledger_with_processed_checkpoint_fails_without_rewrite(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_bytes(
                b'{"queued":1,"processed":1,"latest_result_id":"known-result",'
                b'"latest_result_sha256":"known-hash"}\n'
            )
            original_checkpoint = checkpoint_path.read_bytes()
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1)]):
                with self.assertRaisesRegex(ValueError, "processed results but result ledger is empty"):
                    runner.reconcile_checkpoint()
            self.assertEqual(checkpoint_path.read_bytes(), original_checkpoint)

    def test_fresh_empty_ledger_clears_stale_latest_identity_and_preserves_metadata(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(json.dumps({
                "queued": 0,
                "processed": 0,
                "remaining": 0,
                "latest_result_id": "stale-result",
                "latest_result_sha256": "stale-hash",
                "preserved": "metadata",
            }), encoding="utf-8")
            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[]):
                saved = runner.reconcile_checkpoint()
            self.assertNotIn("latest_result_id", saved)
            self.assertNotIn("latest_result_sha256", saved)
            self.assertEqual(saved["preserved"], "metadata")
            self.assertEqual(saved["processed"], 0)

    def test_reconcile_rejects_frozen_queue_cardinality_mismatch_without_writes(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            items = [queue_item(1), queue_item(2)]
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp, items)
            ledger = root / "batches/batch-001.jsonl"
            ledger.write_text("".join(
                json.dumps(result(seq, "rerun-001", "UNKNOWN", f"synthetic-{seq}")) + "\n"
                for seq in (1, 2)
            ), encoding="utf-8")
            checkpoint_path.write_text(json.dumps({
                "queued": 1,
                "processed": 0,
                "remaining": 1,
                "queue_sha256": runner.sha_bytes(queue_path.read_bytes()),
            }) + "\n", encoding="utf-8")
            ledger_before = ledger.read_bytes()
            checkpoint_before = checkpoint_path.read_bytes()
            caught = None
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path), patch.object(
                runner, "read_queue", return_value=items
            ):
                try:
                    runner.reconcile_checkpoint()
                except ValueError as exc:
                    caught = exc
            self.assertEqual(ledger.read_bytes(), ledger_before, "reconciliation changed ledger bytes")
            self.assertEqual(
                checkpoint_path.read_bytes(), checkpoint_before,
                "queue cardinality mismatch rewrote checkpoint bytes",
            )
            self.assertIsNotNone(caught, "mismatched checkpoint queued count was not refused")
            self.assertRegex(str(caught), "queued.*(count|cardinality).*(queue|mismatch)")

    def test_persist_rejects_frozen_queue_cardinality_mismatch_before_append(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            items = [queue_item(1), queue_item(2)]
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp, items)
            ledger = root / "batches/batch-001.jsonl"
            ledger.write_text(
                json.dumps(result(1, "rerun-001", "UNKNOWN", "synthetic-existing")) + "\n",
                encoding="utf-8",
            )
            checkpoint_path.write_text(json.dumps({"queued": 1, "processed": 1}) + "\n",
                                       encoding="utf-8")
            ledger_before = ledger.read_bytes()
            checkpoint_before = checkpoint_path.read_bytes()
            row = result(2, "rerun-001", "PARTIAL", "synthetic-new")
            caught = None
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path), patch.object(
                runner, "read_queue", return_value=items
            ):
                try:
                    runner.persist_result(row, allow_superseding=True)
                except ValueError as exc:
                    caught = exc
            self.assertEqual(ledger.read_bytes(), ledger_before, "persistence appended despite queue mismatch")
            self.assertFalse((root / "batches/batch-002.jsonl").exists())
            self.assertEqual(
                checkpoint_path.read_bytes(), checkpoint_before,
                "queue cardinality mismatch rewrote checkpoint bytes",
            )
            self.assertIsNotNone(caught, "mismatched checkpoint queued count was not refused")
            self.assertRegex(str(caught), "queued.*(count|cardinality).*(queue|mismatch)")

    def test_invalid_checkpoint_queued_types_fail_closed_for_reconcile_and_persist(self):
        invalid_values = (True, "1", 1.0, -1, None, "missing")
        for invalid in invalid_values:
            for operation in ("reconcile", "persist"):
                with self.subTest(queued=invalid, operation=operation), tempfile.TemporaryDirectory(
                    prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
                ) as temp:
                    base, root, cache, queue_path, checkpoint_path = fixture_layout(temp)
                    ledger = root / "batches/batch-001.jsonl"
                    ledger.write_text(
                        json.dumps(result(1, "rerun-001", "UNKNOWN", "synthetic-existing")) + "\n",
                        encoding="utf-8",
                    )
                    checkpoint = {"processed": 1, "remaining": 0}
                    if invalid != "missing":
                        checkpoint["queued"] = invalid
                    checkpoint_path.write_text(json.dumps(checkpoint) + "\n", encoding="utf-8")
                    ledger_before = ledger.read_bytes()
                    checkpoint_before = checkpoint_path.read_bytes()
                    caught = None
                    with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                        QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path):
                        try:
                            if operation == "reconcile":
                                runner.reconcile_checkpoint()
                            else:
                                runner.persist_result(
                                    result(1, "rerun-001", "PARTIAL", "synthetic-replacement"),
                                    allow_superseding=True,
                                )
                        except (TypeError, ValueError, KeyError) as exc:
                            caught = exc
                    self.assertEqual(
                        ledger.read_bytes(), ledger_before,
                        f"invalid queued value changed ledger bytes during {operation}",
                    )
                    self.assertEqual(
                        checkpoint_path.read_bytes(), checkpoint_before,
                        f"invalid queued value changed checkpoint bytes during {operation}",
                    )
                    self.assertIsInstance(caught, ValueError)
                    self.assertRegex(str(caught), "queued.*nonnegative integer")

    def test_correct_cardinality_and_fresh_empty_queue_remain_valid(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            items = [queue_item(1), queue_item(2)]
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp, items)
            checkpoint_path.write_text(json.dumps({"queued": 2, "processed": 0}) + "\n",
                                       encoding="utf-8")
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path), patch.object(
                runner, "read_queue", return_value=items
            ):
                self.assertTrue(runner.persist_result(result(1, "rerun-001", "UNKNOWN", "valid-1")))
                self.assertTrue(runner.persist_result(result(2, "rerun-001", "PARTIAL", "valid-2")))
                saved = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["queued"], 2)
            self.assertEqual(saved["processed"], 2)
            self.assertEqual(saved["remaining"], 0)

        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            base, root, cache, queue_path, checkpoint_path = fixture_layout(temp, [])
            checkpoint_path.write_text(json.dumps({
                "queued": 0,
                "processed": 0,
                "remaining": 0,
                "preserved": "empty queue",
            }) + "\n", encoding="utf-8")
            with patch.multiple(runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=checkpoint_path), patch.object(
                runner, "read_queue", return_value=[]
            ):
                saved = runner.reconcile_checkpoint()
            self.assertEqual(saved["queued"], 0)
            self.assertEqual(saved["processed"], 0)
            self.assertEqual(saved["remaining"], 0)
            self.assertEqual(saved["preserved"], "empty queue")

    def test_reconcile_hashes_exact_bytes_of_latest_physical_row(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            earlier_path = root / "batches/batch-001.jsonl"
            earlier = result(2, "rerun-001", "PARTIAL", "earlier-file")
            earlier_path.write_bytes((json.dumps(earlier, ensure_ascii=False) + "\n").encode("utf-8"))
            latest_path = root / "batches/batch-002.jsonl"
            latest = result(1, "rerun-002", "UNKNOWN", "physical-last-漢字")
            latest["note"] = "literal π and escaped 文"
            latest_line = (" " + json.dumps(latest, ensure_ascii=False) + " \n").encode("utf-8")
            latest_path.write_bytes(
                (json.dumps(result(1, "rerun-002", "PARTIAL", "superseded-in-file")) + "\n").encode("utf-8") + latest_line
            )
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(
                json.dumps({
                    "queued": 2,
                    "processed": 0,
                    "remaining": 2,
                    "current_rerun_batch": "rerun-002",
                }),
                encoding="utf-8",
            )

            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=[queue_item(1), queue_item(2)]):
                saved = runner.reconcile_checkpoint()

            self.assertEqual(saved["latest_result_id"], "physical-last-漢字")
            self.assertEqual(
                saved["latest_result_sha256"], hashlib.sha256(latest_line).hexdigest()
            )

    def test_resume_reconciles_ledger_append_after_checkpoint_interruption(self):
        with tempfile.TemporaryDirectory(
            prefix="candidate-checkpoint-", dir=os.environ["TMPDIR"]
        ) as temp:
            root = Path(temp)
            (root / "batches").mkdir()
            queue_path = root / "queue.jsonl"
            queue_path.write_text("synthetic queue fixture\n", encoding="utf-8")
            queued_items = [queue_item(1), queue_item(2)]
            rows = [
                result(1, "rerun-001", "PARTIAL", "synthetic-first"),
                result(2, "rerun-001", "PARTIAL", "synthetic-other"),
                result(1, "rerun-001", "UNKNOWN", "synthetic-ledger-only"),
            ]
            (root / "batches/batch-001.jsonl").write_text(
                "".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows),
                encoding="utf-8",
            )
            checkpoint_path = root / "checkpoint.json"
            checkpoint_path.write_text(
                json.dumps({
                    "queued": 2,
                    "processed": 0,
                    "remaining": 2,
                    "verdict_counts": {"UNKNOWN": 0},
                    "queue_sha256": runner.sha_bytes(queue_path.read_bytes()),
                    "current_rerun_batch": "rerun-001",
                    "retained": "metadata",
                }),
                encoding="utf-8",
            )

            with patch.object(runner, "ROOT", root), patch.object(
                runner, "CACHE", root / "cache"
            ), patch.object(runner, "QUEUE_PATH", queue_path), patch.object(
                runner, "CHECKPOINT_PATH", checkpoint_path
            ), patch.object(runner, "read_queue", return_value=queued_items), patch.object(
                sys, "argv", ["run_hermes_batch.py", "--workers", "1"]
            ):
                self.assertEqual(runner.main(), 0)

            saved = json.loads(checkpoint_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["processed"], 2)
            self.assertEqual(saved["remaining"], 0)
            self.assertEqual(saved["verdict_counts"]["UNKNOWN"], 1)
            self.assertEqual(saved["latest_result_id"], "synthetic-ledger-only")
            self.assertEqual(saved["retained"], "metadata")


if __name__ == "__main__":
    unittest.main()
