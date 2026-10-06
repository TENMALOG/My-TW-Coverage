"""Protect append-only component corrections and the paper-facing index."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_reviewer_ledger import validate, text_sha256


class ReviewerAmendmentIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.sem = self.root / 'audit-v5/semantic'
        self.now = datetime.now(timezone.utc).isoformat()
        claim = '公司有三個事業部，產品A全球第一。'
        self.cid = '1001:objective_ranking_or_market_share:test'
        self.chash = hashlib.sha256(claim.encode()).hexdigest()
        self.put('audit-v5/generated/semantic-high-queue.json', {'items': [
            {'claim_id': self.cid, 'normalized_claim_hash': self.chash, 'claim': claim}]})
        self.put('audit-v5/semantic/author-001.json', {'batch_id': 'author-001', 'items': [
            {'claim_id': self.cid, 'normalized_claim_hash': self.chash,
             'decision': 'ACCEPTED', 'independent_review': None, 'final_state': None}]})
        raw = self.root / 'source.txt'
        raw.write_bytes(b'Three divisions manufacture product A.')
        note = self.root / 'note.txt'
        note.write_text('Three divisions are stated; ranking is absent.', encoding='utf-8')
        self.source = {'source_id': 'test-source', 'url': 'https://example.invalid/report',
                       'source_sha256': hashlib.sha256(raw.read_bytes()).hexdigest(),
                       'local_source_path': 'source.txt', 'inspection_note_path': 'note.txt',
                       'inspection_note_sha256': text_sha256(note), 'inspected_at': self.now}
        self.put('manifest.json', {'sources': [self.source]})
        self.put('counterchecks.json', {})
        self.evidence = {'source_id': 'test-source', 'url': self.source['url'],
                         'source_sha256': self.source['source_sha256'],
                         'locator': 'paragraph 1', 'period_binding': '2024',
                         'inspection_note_path': 'note.txt', 'inspection_note_sha256': text_sha256(note)}
        before = [{'text': 'Three divisions and global first', 'assessment': 'UNRESOLVED',
                   'source_ids': ['test-source']}]
        after = [{'text': 'Three divisions', 'assessment': 'SUPPORTED_WITH_PERIOD',
                  'source_ids': ['test-source']},
                 {'text': 'Global first', 'assessment': 'UNRESOLVED', 'source_ids': ['test-source']}]
        self.item = {'claim_id': self.cid, 'normalized_claim_hash': self.chash, 'claim': claim,
                     'author_batch_id': 'author-001', 'author_decision': 'ACCEPTED',
                     'author_batch_sha256': text_sha256(self.sem / 'author-001.json'),
                     'decision': 'PARTIALLY_SUPPORTED', 'agrees_with_author': False,
                     'final_state': 'ESCALATED_REVIEW_DISAGREEMENT', 'status': 'ESCALATED',
                     'component_assessments': before, 'gap_types': ['group_count', 'ranking'],
                     'proposed_text': 'The company manufactures product A.', 'evidence': [self.evidence]}
        self.put('audit-v5/semantic/reviewer-001.json', {
            'schema': 'semantic-manual-independent-review-2', 'reviewed_at': self.now,
            'review_count': 1, 'evidence_manifest': 'manifest.json',
            'evidence_manifest_sha256': text_sha256(self.root / 'manifest.json'),
            'counterchecks': 'counterchecks.json', 'counterchecks_sha256': text_sha256(self.root / 'counterchecks.json'),
            'items': [self.item], 'decision_counts': {'PARTIALLY_SUPPORTED': 1},
            'final_state_counts': {'ESCALATED_REVIEW_DISAGREEMENT': 1}})
        self.event = {'event_id': 'correction-1', 'reviewed_at': self.now,
                      'claim_id': self.cid, 'normalized_claim_hash': self.chash,
                      'target_batch_path': 'audit-v5/semantic/reviewer-001.json',
                      'target_batch_sha256': text_sha256(self.sem / 'reviewer-001.json'),
                      'rationale': 'Source explicitly states three divisions; ranking remains unresolved.',
                      'evidence': [self.evidence], 'component_assessments_before': before,
                      'component_assessments_after': after, 'gap_types_before': self.item['gap_types'],
                      'gap_types_after': ['ranking'], 'proposed_text_before': self.item['proposed_text'],
                      'proposed_text_after': 'In 2024 the company had three divisions.'}
        for f in ('decision', 'final_state', 'status'):
            self.event[f + '_before'] = self.event[f + '_after'] = self.item[f]
        self.save_event()

    def put(self, path, obj):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    def save_event(self):
        self.put('audit-v5/semantic/reviewer-amendments-001.json', {
            'schema': 'semantic-reviewer-component-amendment-1', 'event_count': 1, 'events': [self.event]})

    def assert_rejected(self, message):
        result = validate(self.root, check_local_sources=True)
        self.assertFalse(result['ok'])
        self.assertTrue(any(message in e for e in result['errors']), result['errors'])

    def test_valid_correction_preserves_decision_and_unique_claim_count(self):
        result = validate(self.root, check_local_sources=True)
        self.assertTrue(result['ok'], result['errors'])
        self.assertEqual(result['reviewer_claims'], 1)
        self.assertEqual(result['component_amendments'], 1)
        self.assertEqual(result['final_accepted'], 0)

    def test_rejects_stale_before_snapshot(self):
        self.event['gap_types_before'] = ['invented']
        self.save_event()
        self.assert_rejected('before snapshot mismatch')

    def test_rejects_promotion_inside_component_amendment(self):
        self.event['final_state_after'] = 'ACCEPTED'
        self.save_event()
        self.assert_rejected('changes decision/state')

    def test_rejects_changed_target_batch_hash(self):
        self.event['target_batch_sha256'] = '0' * 64
        self.save_event()
        self.assert_rejected('target hash mismatch')

    def test_rejects_reassigned_source(self):
        self.event['evidence'] = [dict(self.evidence, url='https://example.invalid/other-company')]
        self.save_event()
        self.assert_rejected('evidence lineage mismatch')

    def test_rejects_changed_raw_source(self):
        (self.root / 'source.txt').write_bytes(b'An unrelated company document.')
        self.assert_rejected('local raw source changed/missing')

    def test_rejects_final_acceptance_in_derived_index(self):
        item = copy.deepcopy(self.item)
        for f in ('component_assessments', 'gap_types', 'proposed_text'):
            item[f] = self.event[f + '_after']
        item['reviewer_batch_path'] = self.event['target_batch_path']
        item['reviewer_batch_sha256'] = self.event['target_batch_sha256']
        item['amendments_applied'] = [{
            'path': 'audit-v5/semantic/reviewer-amendments-001.json',
            'sha256': text_sha256(self.sem / 'reviewer-amendments-001.json'), 'event_id': 'correction-1'}]
        item['evidence'] += self.event['evidence']
        item['final_state'] = 'ACCEPTED'
        self.put('audit-v5/semantic/accepted-review-index.json', {
            'items': [item], 'claim_count': 1, 'reviewer_decisions': {'PARTIALLY_SUPPORTED': 1},
            'cleared_original_claims': 0, 'disagreements_pending_adjudication': 1})
        self.assert_rejected('effective ledger')


if __name__ == '__main__':
    unittest.main()
