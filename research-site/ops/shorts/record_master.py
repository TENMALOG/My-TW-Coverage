"""One render, two deliverables: the 9:16 master for YouTube Shorts (with the theme + effects) and a light,
silent web encode of the same frames (the web page shows only the central 1:1 square with CSS).

  py record_master.py stills 2330 2.5 7 12      -> stills/master_2330_t002.5.png ...
  py record_master.py video 2330 [workers]       -> out/master/2330_youtube.mp4, out/master/2330_web.mp4

Frames are drawn at 2x (2160x3840, lossless PNG) and scaled to 1080x1920. Audio: audio/score.py with
master.html events, loudness SHORTS_LUFS (default -18 LUFS, true peak -2 dBTP).
"""
import os
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
os.environ.setdefault('SHORTS_STAGE', 'master.html')
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / 'audio'))
from record_web import storyboard  # noqa: E402  (adds corrected industry, 證交所產業別, fact pages)

STAGE = (HERE / 'master.html').as_uri()
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
FPS = 30
OUT = HERE / 'out' / 'master'


def open_stage(p, t):
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=2)
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
            pg.screenshot(path=str(HERE / 'stills' / f'master_{t}_t{x:05.1f}.png'))
        b.close()
    print(t, 'seconds', total)


def segment(args):
    t, idx, f0, f1 = args
    seg = OUT / f'{t}_seg{idx:02d}.mp4'
    ff = subprocess.Popen([FFMPEG, '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png',
                           '-i', '-', '-vf', 'scale=1080:1920:flags=lanczos', '-c:v', 'libx264', '-preset', 'slow',
                           '-crf', '14', '-tune', 'animation', '-pix_fmt', 'yuv420p', str(seg)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, _ = open_stage(p, t)
        for f in range(f0, f1):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='png'))
        b.close()
    ff.stdin.close()
    ff.wait()
    return seg


def video(t, workers=4):
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b, pg, total = open_stage(p, t)
        b.close()
    frames = int(total * FPS)
    step = -(-frames // workers)
    with ProcessPoolExecutor(workers) as ex:
        segs = list(ex.map(segment, [(t, i, i * step, min(frames, (i + 1) * step)) for i in range(workers)]))
    lst = OUT / f'{t}_concat.txt'
    lst.write_text(''.join(f"file '{s.as_posix()}'\n" for s in segs), encoding='utf-8')
    silent = OUT / f'{t}_silent.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(silent)], check=True)
    for s in segs:
        s.unlink()
    lst.unlink()
    # audio: theme + effects synced to master.html events, normalised to SHORTS_LUFS
    import score
    mix, _ = score.mixdown(t)
    raw, norm = OUT / f'_{t}_raw.wav', OUT / f'_{t}_mix.wav'
    score.write(raw, mix)
    score.loudnorm(raw, norm)
    yt = OUT / f'{t}_youtube.mp4'           # upload master: high quality video + AAC 48 kHz
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(silent), '-i', str(norm), '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', str(yt)], check=True)
    web = OUT / f'{t}_web.mp4'               # web: same frames, lighter, silent (the page mutes it anyway)
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(silent), '-c:v', 'libx264', '-preset', 'slow', '-crf', '24',
                    '-tune', 'animation', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', str(web)], check=True)
    raw.unlink()
    norm.unlink()
    silent.unlink()
    print(yt, yt.stat().st_size // 1024, 'KB |', web, web.stat().st_size // 1024, 'KB |', round(total, 1), 's')


if __name__ == '__main__':
    if sys.argv[1] == 'stills':
        stills(sys.argv[2], [float(x) for x in sys.argv[3:]])
    else:
        video(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 4)
