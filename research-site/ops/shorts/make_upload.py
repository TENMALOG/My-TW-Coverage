"""Upload folder for YouTube: out/upload/{NN 產業}/{代號}_{公司}.mp4 + .txt (title + description), plus 上傳清單.csv.

  py make_upload.py

Videos are hard links to out/master/{t}_youtube.mp4 (no extra disk space). Industry folders are numbered by size
(largest first) so uploading folder by folder fills one playlist at a time. 上傳清單.csv has an empty
youtube_id column: fill it in after uploading and run `py make_upload.py --ids` to write
research-site/data/youtube-ids.csv, which the website uses to embed each video.
"""
import csv
import json
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
MASTER, META, UP = HERE / 'out' / 'master', HERE / 'out' / 'meta', HERE / 'out' / 'upload'
LIST = UP / '上傳清單.csv'


def safe(s):
    return re.sub(r'[\\/:*?"<>|]', '＿', s).strip()


def build():
    cat = list(csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig')))
    zh = {r['industry_folder']: r['name_zh'].rstrip('?？') for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
    old = {}
    if LIST.exists():                                  # keep any youtube ids already filled in
        old = {r['代號']: r.get('youtube_id', '') for r in csv.DictReader(open(LIST, encoding='utf-8-sig'))}
    size = Counter(r['industry_folder'] for r in cat)
    order = {f: i + 1 for i, (f, _) in enumerate(sorted(size.items(), key=lambda x: (-x[1], x[0])))}
    if UP.exists():
        for p in UP.iterdir():
            if p.is_dir():
                shutil.rmtree(p)
    UP.mkdir(parents=True, exist_ok=True)
    rows, missing = [], []
    for r in sorted(cat, key=lambda r: (order[r['industry_folder']], r['ticker'])):
        t, name, ind = r['ticker'], r['company'], r['industry_folder']
        src, meta = MASTER / f'{t}_youtube.mp4', META / f'{t}.json'
        if not src.exists() or not meta.exists():
            missing.append(t)
            continue
        m = json.loads(meta.read_text(encoding='utf-8'))
        d = UP / f'{order[ind]:02d} {safe(zh[ind])}'
        d.mkdir(exist_ok=True)
        base = f'{t}_{safe(name)}'
        dst = d / f'{base}.mp4'
        try:
            os.link(src, dst)
        except OSError:
            shutil.copy2(src, dst)
        (d / f'{base}.txt').write_text(f"【標題】\n{m['title']}\n\n【說明】\n{m['description']}\n", encoding='utf-8')
        rows.append({'順序': len(rows) + 1, '代號': t, '公司': name, '產業': zh[ind], '資料夾': d.name,
                     '影片檔': dst.name, '標題': m['title'], '播放清單': f'股.tw 研究室｜{zh[ind]}',
                     'youtube_id': old.get(t, '')})
    with open(LIST, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (UP / '使用說明.txt').write_text(
        '股.tw 研究室 YouTube 上傳資料夾\n\n'
        '・資料夾依產業分類，編號越小家數越多；建議一次上傳一個產業，並放進同名播放清單（見上傳清單.csv 的「播放清單」欄）。\n'
        '・每支影片旁的同名 .txt 是標題與說明欄，直接複製貼上。\n'
        '・上傳後把影片網址最後的代號（例如 youtube.com/shorts/AbC123xyz 的 AbC123xyz）填進上傳清單.csv 的 youtube_id 欄，\n'
        '  存檔後告訴 Claude，網站就會自動改成內嵌播放。\n'
        '・本系列是資料視覺化動畫，不含擬真人像或人聲，上傳時一般不需要勾選「變造或合成內容」（日後若改用克隆聲音配音，則需要勾選）。\n', encoding='utf-8')
    print(f'{len(rows)} videos in {len(order)} industry folders; missing {len(missing)} {missing[:10]}')


def ids():
    rows = [r for r in csv.DictReader(open(LIST, encoding='utf-8-sig')) if r.get('youtube_id', '').strip()]
    with open(SITE / 'data/youtube-ids.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ticker', 'youtube_id'])
        for r in rows:
            w.writerow([r['代號'], r['youtube_id'].strip()])
    print(f'{len(rows)} youtube ids written')


if __name__ == '__main__':
    ids() if '--ids' in sys.argv else build()
