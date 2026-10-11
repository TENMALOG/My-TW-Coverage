#!/usr/bin/env python3
"""Create reviewable copies from independently supported revisions only."""
import difflib
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
import run_final_adjudication as controller

ROOT = Path(__file__).resolve().parent / 'revision-pilot-001'


def read(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()] if path.exists() else []


def digest(data):
    return hashlib.sha256(data).hexdigest()


def financial(data):
    match = re.search(rb'(?m)^## \xe8\xb2\xa1\xe5\x8b\x99\xe6\xa6\x82\xe6\xb3\x81[^\r\n]*', data)
    if not match:
        raise ValueError('Financial section missing')
    return data[match.start():]


def linked(text):
    entities = ['漢翔', '洛克希德馬丁公司', 'F-16', '日本ケミコン', '台灣國際造船',
                '長榮海運股份有限公司', 'Evergreen Marine', '雲豹能源', '天能綠電',
                '永豐金控', '永豐銀行', 'TOYOTA', 'LEXUS', 'Lexus', 'HINO',
                'ASML', 'Applied Materials', 'Lam Research', 'KLA', 'Tokyo Electron',
                'Airbus', 'Supermicro', 'Huawei', 'Levi’s', 'UNIQLO', 'Adidas',
                'Columbia', 'The North Face', '青新環境工程股份有限公司', '青新',
                '日友環保科技股份有限公司', '大國鋼', 'BBI-USA', 'Nike', 'ON', 'On', 'Hoka',
                "LEVI'S", '如興', '泰創工程', '晶碩光學股份有限公司', '晶碩光學',
                '得力', 'Under Armour', '華泰', 'EMS', 'SMT', '美超微', 'AI 伺服器',
                '富世達', '華為', 'Mate XT', '台船', '中鋼', '台積電', 'EUV', '星宇航空',
                '空中巴士集團', 'A321neo', 'A330-900neo', 'A350-900', 'A350-1000', 'A350F',
                '大台北區瓦斯', '台灣中油股份有限公司', '台灣中油', '新海瓦斯',
                '臺灣水泥股份有限公司', '精聯電子', '精技電腦股份有限公司', '精技電腦',
                '富華創新股份有限公司', '富華新', '總太地產開發股份有限公司', '鼎翰科技',
                '台灣半導體', '北基', '三地能源', '嘉佑能源', 'EV', '三星科技', '強茂',
                '由田', 'CoWoS', 'FOPLP', 'SEMI檢測系統', '大研生醫', '尚凡', '宏碁遊戲']
    aliases = {'日本ケミコン': 'Nippon Chemi-Con', '洛克希德馬丁公司': 'Lockheed Martin',
               'UNIQLO': 'Uniqlo', "LEVI'S": "Levi's", '臺灣水泥股份有限公司': '台泥',
               '台灣半導體': '台半', '青新環境工程股份有限公司': '青新-創',
               '空中巴士集團': 'Airbus', '日友環保科技股份有限公司': '日友'}
    pattern = '|'.join(re.escape(e) for e in sorted(entities, key=len, reverse=True))
    result = re.sub(pattern, lambda m: '[[' + aliases.get(m[0], m[0]) +
                    ('|' + m[0] if m[0] in aliases else '') + ']]', text)
    plain = re.sub(r'\[\[([^\]]+)\]\]', lambda m: m[1].split('|')[-1], result)
    if plain != text:
        raise ValueError('Wikilinks changed the verified wording')
    return result


def main():
    queue = {x['claim_id']: x for x in read(ROOT / 'queue.jsonl')}
    accepted = read(ROOT / 'delivery/accepted-revisions.jsonl')
    groups = defaultdict(list)
    for row in accepted:
        groups[queue[row['revision_id']]['parent_report_context']['resolved_report_path']].append(row)
    files = []; changes = []; issues = []
    for rel, rows in groups.items():
        try:
            source = controller.BASE / rel
            original = source.read_bytes()
            for row in rows:
                item = queue[row['revision_id']]
                if digest(original) != item['parent_report_context']['report_sha256']:
                    raise ValueError('Parent report changed')
                if not source.name.startswith(item['issuer_ticker'] + '_'):
                    raise ValueError('Ticker filename mismatch')
            text = original.decode('utf-8')
            nl = '\r\n' if '\r\n' in text else '\n'
            body = []
            for row in rows:
                item = queue[row['revision_id']]
                old = item['parent_claim']['original_text']
                actual = old
                if text.count(old) != 1:
                    pattern = r'\s+'.join(re.escape(t) for t in re.split(r'\s+', old))
                    matches = list(re.finditer(pattern, text))
                    if len(matches) != 1:
                        raise ValueError('Parent assertion does not occur exactly once: ' + row['revision_id'])
                    actual = matches[0][0]
                start = text.index(actual)
                line_start = text.rfind('\n', 0, start)+1
                line_end = text.find('\n', start+len(actual))
                if line_end<0:
                    line_end = len(text)
                remainder = text[line_start:start]+text[start+len(actual):line_end]
                relocation = ''
                numbered = re.match(r'^\((\d+)\)\s*([^：:]+)[：:]', old)
                if numbered:
                    relocation = '('+numbered[1]+') '+numbered[2]+'：相關經查證資料見「業務與歷史資料」。'
                if re.fullmatch(r'\s*-\s*(?:\*\*[^\n]+:?\*\*)?\s*', remainder):
                    text = text[:line_start]+text[min(line_end+1, len(text)):]
                else:
                    text = text[:start]+relocation+text[start+len(actual):]
                new = linked(row['text'])
                urls = list(dict.fromkeys(e['url'] for a in row['adjudication']['atomic_claims'] for e in a['evidence']))
                body.append(new + nl + nl + '來源：' + '、'.join('[來源 ' + str(i+1) + '](' + url + ')' for i, url in enumerate(urls)))
                changes.append({'revision_id': row['revision_id'], 'parent_claim_id': row['parent_claim_id'],
                    'report_path': rel, 'original_text_removed': old, 'actual_report_span_removed': actual, 'verified_new_text': row['text'],
                    'replacement_at_original_location': relocation,
                    'formatted_new_text': new, 'target_section': row['target_section'], 'source_urls': urls,
                    'output_sha256': row['output_sha256'], 'parent_report_sha256': digest(original),
                    'qualifier_changes': item['qualifier_changes'], 'parent_original_acceptance_changed': False})
            # A removed assertion can leave an otherwise empty list item.
            text = re.sub(r'(?m)^-\s*\r?\n', '', text)
            marker = '## 財務概況'
            pos = text.index(marker)
            block = '## 業務與歷史資料' + nl + nl + (nl + nl).join(body) + nl + nl
            text = text[:pos] + block + text[pos:]
            first = text.find(nl)
            notice = nl + nl + '> 審閱草稿：本次僅複核「業務與歷史資料」所列修正句，其餘內容沿用原報告，尚未於本批次驗證。' + nl
            text = text[:first] + notice + text[first:]
            data = text.encode('utf-8')
            if financial(data) != financial(original):
                raise ValueError('Financial section byte mismatch')
            dest = ROOT / 'report-drafts' / Path(rel).relative_to('Pilot_Reports')
            dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(data)
            patch = ROOT / 'report-diffs' / (source.stem + '.diff')
            patch.parent.mkdir(parents=True, exist_ok=True)
            patch.write_text(''.join(difflib.unified_diff(original.decode().splitlines(True), text.splitlines(True),
                fromfile=rel, tofile=str(dest.relative_to(controller.BASE)))))
            files.append({'source_path': rel, 'draft_path': str(dest.relative_to(controller.BASE)),
                'source_sha256': digest(original), 'draft_sha256': digest(data),
                'financial_sha256': digest(financial(original)), 'financial_bytes_preserved': True,
                'diff_path': str(patch.relative_to(controller.BASE)), 'diff_sha256': digest(patch.read_bytes()),
                'revision_ids': [row['revision_id'] for row in rows],
                'wikilink_count': len(re.findall(r'\[\[.*?\]\]', text)),
                'entire_report_verified': False})
        except Exception as exc:
            issues.append({'report_path': rel, 'error': str(exc)})
    (ROOT / 'delivery/change-register.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in changes))
    controller.write_json(ROOT / 'delivery/draft-manifest.json', {'generated_at': controller.now(),
        'accepted_input_sha256': digest((ROOT / 'delivery/accepted-revisions.jsonl').read_bytes()),
        'accepted_revision_count': len(accepted), 'draft_count': len(files), 'files': files, 'issues': issues,
        'corpus_modified': False, 'partial_delivery': not json.loads((ROOT/'delivery/summary.json').read_text())['adjudication_complete']})
    print(json.dumps({'draft_count': len(files), 'included_revisions': sum(len(f['revision_ids']) for f in files), 'issues': issues}, ensure_ascii=False))


if __name__ == '__main__':
    main()
