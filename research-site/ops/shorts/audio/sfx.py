"""Gravity sound effects for the chart reveals, synced to the stage's event list (window.events()).

  py sfx.py 2330 H1     -> out/2330_H1.mp4

Events come from short.html: 'whoosh' (pie sweep, accelerating), 'fall' (bar dropping into place),
'thud' (impact; g = weight, rebounds are smaller), 'tap' (legend row lands). All sounds are synthesized here.
  H1  深沉重擊：cinematic low boom, long sub tail
  H2  厚實落地：shorter punchy thump with a cardboard/wood knock (matches the paper-sticker look)
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.signal import butter, sosfilt

from make_sounds import FFMPEG, SR, write

HERE = Path(__file__).resolve().parent
RNG = np.random.default_rng(7)


def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(t / max(a, 1e-4), 1) * np.exp(-t / d)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], btype='band', fs=SR, output='sos'), x)


def lp(x, f):
    return sosfilt(butter(2, f, btype='low', fs=SR, output='sos'), x)


def sweep_noise(dur, f0, f1, curve=1.0):
    """Band-limited noise whose centre moves f0 -> f1 (processed in short overlapping chunks)."""
    n = int(SR * dur); out = np.zeros(n); hop = 480; win = np.hanning(hop * 2)
    noise = RNG.uniform(-1, 1, n + hop * 2)
    for i in range(0, n, hop):
        c = f0 + (f1 - f0) * (i / n) ** curve
        seg = bp(noise[i:i + hop * 2], c * .7, min(c * 1.4, SR / 2 - 100)) * win
        m = min(hop * 2, n - i); out[i:i + m] += seg[:m]
    return out


def kick(f0, f1, dur, decay):
    n = int(SR * dur); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .002, decay)


def thud(kind, g):
    if kind == 'H1':
        body = kick(150, 38, 1.0, .32)
        sub = np.sin(2 * np.pi * 32 * np.arange(int(SR * 1.0)) / SR) * env(int(SR * 1.0), .01, .45) * .5
        dust = lp(RNG.uniform(-1, 1, int(SR * 1.0)), 900) * env(int(SR * 1.0), .001, .06) * .9
        x = body + sub + dust
    else:
        body = kick(190, 55, .5, .14)
        knock = bp(RNG.uniform(-1, 1, int(SR * .5)), 350, 1100) * env(int(SR * .5), .0005, .03) * 1.4
        slap = bp(RNG.uniform(-1, 1, int(SR * .5)), 2500, 7000) * env(int(SR * .5), .0003, .008) * .5
        # phone speakers cannot play the 55 Hz body: a saturated 100-400 Hz copy keeps the weight audible
        mid = bp(np.tanh(body * 4), 100, 400) * .45
        x = body + knock + slap + mid
    return x * g


def fall(dur, g):
    n = int(SR * dur)
    return sweep_noise(dur, 2400, 500) * np.linspace(0, 1, n) ** 2 * .35 * g


def whoosh(dur, g):
    n = int(SR * dur); t = np.arange(n) / SR
    air = sweep_noise(dur, 250, 3000, 2.2) * np.linspace(0, 1, n) ** 2.2
    tone = np.sin(2 * np.pi * np.cumsum(120 + 380 * (t / dur) ** 2.2) / SR) * np.linspace(0, 1, n) ** 3 * .25
    return (air * .6 + tone) * g


def tap(kind, g):
    n = int(SR * .25)
    if kind == 'H1':
        return kick(110, 60, .25, .06) * g
    return (bp(RNG.uniform(-1, 1, n), 500, 1600) * env(n, .0005, .025) * 1.2 + kick(220, 120, .25, .04) * .5) * g


def events(ticker):
    from playwright.sync_api import sync_playwright
    sb = json.loads((HERE.parent / 'storyboard' / f'{ticker}.json').read_text(encoding='utf-8'))
    with sync_playwright() as p:
        b = p.chromium.launch(channel='chrome'); pg = b.new_page()
        pg.goto((HERE.parent / 'short.html').as_uri()); pg.evaluate('window.ready')
        total = pg.evaluate('sb => build(sb)', sb); ev = pg.evaluate('events()'); b.close()
    return ev, total


def track(ev, total, kind):
    out = np.zeros(int(SR * (total + 1.5)))
    for e in ev:
        g = e.get('g', 1)
        if e['type'] == 'thud':
            sig = thud(kind, g) * .9
        elif e['type'] == 'fall':
            sig = fall(e['d'], g)
        elif e['type'] == 'whoosh':
            sig = whoosh(e['d'], g)
        elif e['type'] == 'tap':
            sig = tap(kind, g)
        else:
            continue
        # sounds that lead INTO an impact are placed so they end exactly on it
        i = int(SR * e['t']); m = min(len(sig), len(out) - i)
        out[i:i + m] += sig[:m]
    return np.tanh(out * 1.2)        # soft-clip: keeps the weight, avoids harsh peaks


def mux(ticker, kind):
    ev, total = events(ticker)
    wav = HERE / f'_sfx_{ticker}_{kind}.wav'
    write(wav, track(ev, total, kind))
    out = HERE.parent / 'out' / f'{ticker}_{kind}.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(HERE.parent / 'out' / f'{ticker}.mp4'), '-i', str(wav),
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(out)], check=True)
    wav.unlink()
    print(out, sum(1 for e in ev if e['type'] == 'thud'), 'impacts')


if __name__ == '__main__':
    mux(sys.argv[1], sys.argv[2])
