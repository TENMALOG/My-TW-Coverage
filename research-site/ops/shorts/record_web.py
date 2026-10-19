"""Record the web cover video (1:1, ~13 s, silent, loops) from storyboard/{ticker}.json with web.html.

  py record_web.py stills 2330 1 3 6 9 12      -> stills/web_2330_t001.0.png ...
  py record_web.py video 2330 [2330 ...]       -> out/web/{ticker}.mp4 (720x720 H.264, no audio, faststart)

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
STAGE = (HERE / 'web.html').as_uri()
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
FPS = 30

_ZH = {r['industry_folder']: r['name_zh'].rstrip('?？') for r in csv.DictReader(open(SITE / 'data/industry-names.csv', encoding='utf-8-sig'))}
_IND = {r['ticker']: r['industry_folder'] for r in csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig'))}


def storyboard(t):
    sb = json.loads((HERE / 'storyboard' / f'{t}.json').read_text(encoding='utf-8'))
    sb['industry_zh'] = _ZH.get(_IND.get(t, ''), '')
    return sb


def open_stage(p, t):
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1080})
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
    ff = subprocess.Popen([FFMPEG, '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg',
                           '-i', '-', '-vf', 'scale=720:720:flags=lanczos', '-c:v', 'libx264', '-preset', 'slow', '-crf', '27',
                           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', str(dst)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, t)
        for f in range(int(total * FPS)):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=90))
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
