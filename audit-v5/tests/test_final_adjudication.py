import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('final_judge', Path(__file__).resolve().parents[2]/'audit-v5/semantic/candidate-rerun/run_final_adjudication.py')
judge = importlib.util.module_from_spec(spec); spec.loader.exec_module(judge)


class FinalAcceptanceGate(unittest.TestCase):
    def test_final_acceptance_requires_runtime_coverage_and_reproducible_body(self):
        result = {'verdict':'ACCEPTED', 'research_complete':True, 'complete_original_supported':True,
                  'qualifier_coverage_complete':True, 'all_sources_inspected':True,
                  'unresolved_qualifiers':[], 'contradictions':[],
                  'atomic_claims':[{'status':'SUPPORTED','evidence':[{'url':'https://example.invalid/report',
                    'support_excerpt':'sole registered shareholder', 'inspection_method':'captured_content'}]}]}
        with tempfile.TemporaryDirectory() as temp:
            text = Path(temp)/'source.txt'; text.write_text('The sole registered shareholder is Example Ltd.')
            capture = lambda url: {'status':'captured','url':url,'text_path':str(text)}
            problems, _ = judge.acceptance_problems(result, {'verified':True}, capture)
            self.assertEqual(problems, [])
            for field in ('research_complete','complete_original_supported','qualifier_coverage_complete','all_sources_inspected'):
                bad=copy.deepcopy(result);bad[field]=False
                self.assertTrue(judge.acceptance_problems(bad, {'verified':True}, capture)[0])
            self.assertTrue(judge.acceptance_problems(result, {'verified':False}, capture)[0])
            self.assertTrue(judge.acceptance_problems(result, {'verified':True}, lambda url:{'status':'capture_failed'})[0])
            for status in ('UNKNOWN','CONTRADICTED'):
                bad=copy.deepcopy(result);bad['atomic_claims'][0]['status']=status
                self.assertTrue(judge.acceptance_problems(bad, {'verified':True}, capture)[0])
            for excerpt in ('', 'largest company', 'shareholder not stated in this source'):
                bad=copy.deepcopy(result);bad['atomic_claims'][0]['evidence'][0]['support_excerpt']=excerpt
                self.assertTrue(judge.acceptance_problems(bad, {'verified':True}, capture)[0])
            bad=copy.deepcopy(result);bad['atomic_claims'][0]['evidence'][0]['inspection_method']='uninspected'
            self.assertTrue(judge.acceptance_problems(bad, {'verified':True}, capture)[0])

    def test_table_formatting_normalization_preserves_numbers_and_signs(self):
        result={'verdict':'UNSUPPORTED','research_complete':True,
                'atomic_claims':[{'status':'CONTRADICTED','evidence':[{
                    'url':'https://example.invalid/table','support_excerpt':'Example Ltd | 97年12月18日 | -25.5%',
                    'inspection_method':'captured_content'}]}]}
        with tempfile.TemporaryDirectory() as temp:
            text=Path(temp)/'source.txt';text.write_text('Example Ltd\n97年12月18日\n-25.5%')
            capture=lambda url:{'status':'captured','url':url,'text_path':str(text)}
            self.assertEqual(judge.acceptance_problems(result, {'verified':True}, capture)[0],[])
            result['atomic_claims'][0]['evidence'][0]['support_excerpt']='Example Ltd | 97年12月18日 | 25.5%'
            self.assertTrue(judge.acceptance_problems(result, {'verified':True}, capture)[0])


if __name__ == '__main__': unittest.main()
