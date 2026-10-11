"""Regression checks for defects found before resuming real research."""
import json
import os
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

import test_candidate_checkpoint as checkpoint
import test_candidate_provenance as provenance


class FinalizationRegressions(unittest.TestCase):
    def test_supported_atom_without_a_source_url_is_an_output_failure(self):
        with tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as temp:
            base=Path(temp);root=base/'audit-v5/semantic/candidate-rerun';cache=base/'audit-v5/source-cache/candidate-rerun'
            response=types.SimpleNamespace(returncode=0, stderr=b'', stdout=provenance.payload(atoms=[{
                'text':'Synthetic unsupported citation', 'status':'SUPPORTED', 'period':'2024',
                'sources':[{'source_title':'Synthetic report','url':None}]}]))
            with patch.multiple(provenance.runner, BASE=base, ROOT=root, CACHE=cache), \
                    patch.object(provenance.runner.subprocess, 'run', return_value=response):
                row,error=provenance.runner.process_item(provenance.item(1),1,'rerun-001',False)
            self.assertIsNone(row)
            self.assertIn('SUPPORTED atom has no usable source',error)
            self.assertFalse((root/'evidence/rerun-000001/manifest.json').exists())

    def test_invalid_result_ids_do_not_reconcile_as_completed(self):
        for case in ('missing', 'duplicate'):
            with self.subTest(case=case), tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as temp:
                base, root, cache, queue_path, cp = checkpoint.fixture_layout(
                    temp, [checkpoint.queue_item(1), checkpoint.queue_item(2)])
                first = checkpoint.result(1, 'rerun-001', 'UNKNOWN', 'same-id')
                second = checkpoint.result(2, 'rerun-001', 'PARTIAL', 'second-id')
                if case == 'missing':
                    first.pop('rerun_id')
                else:
                    second['rerun_id'] = first['rerun_id']
                (root / 'batches/batch-001.jsonl').write_text(
                    ''.join(json.dumps(row) + '\n' for row in [first, second]))
                cp.write_text('{"queued":2,"processed":0}\n')
                before = cp.read_bytes()
                with patch.multiple(checkpoint.runner, BASE=base, ROOT=root, CACHE=cache,
                                    QUEUE_PATH=queue_path, CHECKPOINT_PATH=cp):
                    with self.assertRaisesRegex(ValueError, 'rerun_id'):
                        checkpoint.runner.reconcile_checkpoint()
                self.assertEqual(cp.read_bytes(), before)

    def test_duplicate_result_id_is_rejected_before_append(self):
        with tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as temp:
            base, root, cache, queue_path, cp = checkpoint.fixture_layout(
                temp, [checkpoint.queue_item(1), checkpoint.queue_item(2)])
            first = checkpoint.result(1, 'rerun-001', 'UNKNOWN', 'same-id')
            second = checkpoint.result(2, 'rerun-001', 'PARTIAL', 'same-id')
            ledger = root / 'batches/batch-001.jsonl'
            ledger.write_text(json.dumps(first) + '\n')
            cp.write_text('{"queued":2,"processed":1}\n')
            before = (ledger.read_bytes(), cp.read_bytes())
            with patch.multiple(checkpoint.runner, BASE=base, ROOT=root, CACHE=cache,
                                QUEUE_PATH=queue_path, CHECKPOINT_PATH=cp):
                with self.assertRaisesRegex(ValueError, 'Duplicate rerun_id'):
                    checkpoint.runner.persist_result(second)
            self.assertEqual((ledger.read_bytes(), cp.read_bytes()), before)

    def test_directory_file_leaves_are_rejected_before_model_request(self):
        for leaf in ('notes.md', 'manifest.json', 'stdout', 'stderr', 'prompt'):
            with self.subTest(leaf=leaf), tempfile.TemporaryDirectory(dir=os.environ['TMPDIR']) as temp:
                base = Path(temp)
                root = base / 'audit-v5/semantic/candidate-rerun'
                cache = base / 'audit-v5/source-cache/candidate-rerun'
                evidence = root / 'evidence/rerun-000001'
                source = cache / '1234/1/rerun-001'
                targets = {'notes.md': evidence / 'notes.md',
                           'manifest.json': evidence / 'manifest.json',
                           'stdout': source / 'hermes-attempt-1.stdout.txt',
                           'stderr': source / 'hermes-attempt-1.stderr.txt',
                           'prompt': source / 'isolated-prompt.txt'}
                targets[leaf].mkdir(parents=True)
                with patch.multiple(provenance.runner, BASE=base, ROOT=root, CACHE=cache), \
                        patch.object(provenance.runner.subprocess, 'run') as external:
                    with self.assertRaises(provenance.runner.PathSafetyError):
                        provenance.runner.process_item(provenance.item(1), 1, 'rerun-001', False)
                external.assert_not_called()
                if leaf != 'manifest.json':
                    self.assertFalse((evidence / 'manifest.json').exists())


if __name__ == '__main__':
    unittest.main()
