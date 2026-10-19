"""Record the web cover video (1:1, ~13 s, silent, loops) from storyboard/{ticker}.json with web.html.

  py record_web.py stills 2330 1 3 6 9 12      -> stills/web_2330_t001.0.png ...
  py record_web.py video 2330 [2330 ...]       -> out/web/{ticker}.mp4 (1080x1080 H.264 from 2160 px frames, no audio, faststart)

The industry label uses the corrected class (data/industry-corrections.csv via the catalog), not the
storyboard's original folder.
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
STAGE = (HERE / __import__('os').environ.get('WEB_STAGE', 'web2.html')).as_uri()
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
FPS = 30

_ZH = {r['industry_folder']: r['name_zh'].rstrip('?？') for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
_MOPS = {json.loads(l)['ticker']: json.loads(l).get('industry_mops') or '' for l in open(SITE / 'data/basic-data.jsonl', encoding='utf-8')}
_IND = {r['ticker']: r['industry_folder'] for r in csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig'))}


def storyboard(t):
    sb = json.loads((HERE / 'storyboard' / f'{t}.json').read_text(encoding='utf-8'))
    sb['industry_zh'] = _ZH.get(_IND.get(t, ''), '')
    sb['mops_industry'] = _MOPS.get(t, '')
    doc = json.loads((SITE / 'data/company-facts' / f'{t}.json').read_text(encoding='utf-8'))
    sb['pages'] = {f['id']: f.get('page') for f in doc['facts']}          # fact id -> annual-report page (for 出處)
    return sb


def open_stage(p, t):
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1080}, device_scale_factor=2)   # 2160 px supersampling
    pg.goto(STAGE)
    pg.evaluate('window.ready')
    total = pg.evaluate('sb => build(sb)', storyboard(t))
    return b, pg, total


def stills(t, times):
    (HERE / 'stills').mkdir(exist_ok=True)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, t)
        for x in times:
            pg.evaluate(f'render({x})')
            pg.screenshot(path=str(HERE / 'stills' / f'web_{t}_t{x:05.1f}.png'))
        b.close()
    print(t, 'seconds', total)


def video(t):
    out = HERE / 'out' / 'web'
    out.mkdir(parents=True, exist_ok=True)
    dst = out / f'{t}.mp4'
    ff = subprocess.Popen([FFMPEG, '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png',
                           '-i', '-', '-vf', 'scale=1080:1080:flags=lanczos', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-tune', 'animation',
                           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', str(dst)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, t)
        for f in range(int(total * FPS)):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='png'))
        b.close()
    ff.stdin.close()
    ff.wait()
    print(dst, round(total, 1), 's', dst.stat().st_size // 1024, 'KB')


if __name__ == '__main__':
    if sys.argv[1] == 'stills':
        stills(sys.argv[2], [float(x) for x in sys.argv[3:]])
    else:
        for t in sys.argv[2:]:
            video(t)
