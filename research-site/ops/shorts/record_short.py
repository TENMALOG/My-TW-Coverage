"""Record vertical company Shorts (1080x1920) from storyboard/{ticker}.json with short.html.

  py record_short.py stills 2330 1 6 12     -> stills/2330_t001.0.png ... (check composition)
  py record_short.py video 2330 [workers]   -> out/2330.mp4
"""
import json
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
STAGE = (HERE / 'short.html').as_uri()
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
FPS = 30


def open_stage(p, ticker):
    sb = json.loads((HERE / 'storyboard' / f'{ticker}.json').read_text(encoding='utf-8'))
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(STAGE)
    pg.evaluate('window.ready')
    total = pg.evaluate('sb => build(sb)', sb)
    return b, pg, total


def stills(ticker, times):
    out = HERE / 'stills'
    out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, ticker)
        for t in times or [x + 0.5 for x in range(0, int(total), 3)]:
            pg.evaluate(f'render({t})')
            pg.screenshot(path=str(out / f'{ticker}_t{t:05.1f}.png'))
        b.close()
    print(ticker, 'total seconds', total)


def segment(args):
    ticker, idx, f0, f1 = args
    seg = HERE / 'out' / f'{ticker}_seg{idx:02d}.mp4'
    ff = subprocess.Popen([FFMPEG, '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg',
                           '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '22', '-pix_fmt', 'yuv420p',
                           str(seg)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, _ = open_stage(p, ticker)
        for f in range(f0, f1):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=88))
        b.close()
    ff.stdin.close()
    ff.wait()
    return seg


def video(ticker, workers):
    (HERE / 'out').mkdir(exist_ok=True)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, ticker)
        b.close()
    frames = int(total * FPS)
    step = -(-frames // workers)
    jobs = [(ticker, i, i * step, min(frames, (i + 1) * step)) for i in range(workers)]
    with ProcessPoolExecutor(workers) as ex:
        segs = list(ex.map(segment, jobs))
    lst = HERE / 'out' / f'{ticker}_concat.txt'
    lst.write_text(''.join(f"file '{s.as_posix()}'\n" for s in segs), encoding='utf-8')
    out = HERE / 'out' / f'{ticker}.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(out)],
                   check=True)
    for s in segs:
        s.unlink()
    lst.unlink()
    print(out, round(total, 1), 'seconds')


if __name__ == '__main__':
    mode, tk = sys.argv[1], sys.argv[2]
    if mode == 'stills':
        stills(tk, [float(x) for x in sys.argv[3:]])
    else:
        video(tk, int(sys.argv[3]) if len(sys.argv) > 3 else 4)
