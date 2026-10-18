"""Synthesize the Shorts sound marks (original, no third-party samples) and mux them onto a recorded Short.

  py make_sounds.py                         -> audio/{A,B,C}_tick{0..9}.wav, audio/{A,B,C}_logo.wav
  py make_sounds.py mux 2330 A              -> out/2330_A.mp4 (tick at every scene start, logo on the outro)

Every progress-bar segment plays the next note of a rising C-major pentatonic line, so the bar itself
"plays" a melody across the video and resolves on the outro logo: that melody is the sound mark.
  A  木琴：soft marimba
  B  鐘琴：glockenspiel bell, two-note call per segment
  C  貼紙：sticker "pop" + bright pluck
"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SR = 48000
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
SCALE = [523.25, 587.33, 659.25, 783.99, 880.00, 1046.50, 1174.66, 1318.51, 1567.98, 1760.00]  # C5 D5 E5 G5 A5 C6 ...


def env(n, a=0.004, d=0.25):
    t = np.arange(n) / SR
    return np.minimum(t / a, 1) * np.exp(-t / d)


def marimba(f, dur=0.6):
    n = int(SR * dur); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * env(n, .003, .22) + .35 * np.sin(2 * np.pi * 4 * f * t) * env(n, .002, .05)
            + .12 * np.sin(2 * np.pi * 9.9 * f * t) * env(n, .001, .015))


def bell(f, dur=0.9):
    n = int(SR * dur); t = np.arange(n) / SR
    return sum(a * np.sin(2 * np.pi * f * m * t) * env(n, .002, d) for m, a, d in
               [(1, 1, .45), (2.76, .45, .18), (5.40, .25, .08), (8.93, .12, .04)])


def pop(dur=0.07):
    n = int(SR * dur); t = np.arange(n) / SR
    f = 1400 * np.exp(-t * 45) + 180
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .001, .018)


def pluck(f, dur=0.5):
    n = int(SR * dur); p = int(SR / f)
    rng = np.random.default_rng(int(f))
    buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return out * env(n, .001, .3)


def mix(parts, dur):
    out = np.zeros(int(SR * dur))
    for at, sig, g in parts:
        i = int(SR * at); m = min(len(sig), len(out) - i)
        out[i:i + m] += g * sig[:m]
    return out


def tick(kind, k):
    f = SCALE[k % len(SCALE)]
    if kind == 'A':
        return mix([(0, marimba(f), .8), (0, marimba(f * 2), .15)], .7)
    if kind == 'B':
        return mix([(0, bell(f * 2), .5), (.09, bell(f * 3), .35)], 1.0)
    return mix([(0, pop(), .9), (.045, pluck(f), .7)], .6)


def logo(kind):
    c = [1046.50, 1318.51, 1567.98, 2093.0]           # C6 E6 G6 C7: the resolution
    if kind == 'A':
        return mix([(i * .11, marimba(f, 1.2), .7) for i, f in enumerate(c)] + [(.33, marimba(c[0], 1.4), .4)], 1.8)
    if kind == 'B':
        return mix([(i * .12, bell(f, 1.5), .45) for i, f in enumerate(c)], 2.0)
    return mix([(0, pop(), .9), (.12, pop(), .9)] + [(.24 + i * .09, pluck(f, .9), .6) for i, f in enumerate(c)], 1.6)


def write(path, sig):
    sig = sig / max(1e-9, np.abs(sig).max()) * .7
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((sig * 32767).astype('<i2').tobytes())


def make():
    for kind in 'ABC':
        for k in range(10):
            write(HERE / f'{kind}_tick{k}.wav', tick(kind, k))
        write(HERE / f'{kind}_logo.wav', logo(kind))
    print('sounds written')


def scene_starts(ticker):
    from playwright.sync_api import sync_playwright
    sb = json.loads((HERE.parent / 'storyboard' / f'{ticker}.json').read_text(encoding='utf-8'))
    with sync_playwright() as p:
        b = p.chromium.launch(channel='chrome'); pg = b.new_page()
        pg.goto((HERE.parent / 'short.html').as_uri()); pg.evaluate('window.ready')
        total = pg.evaluate('sb => build(sb)', sb); starts = pg.evaluate('START'); b.close()
    return starts, total


def mux(ticker, kind):
    starts, total = scene_starts(ticker)
    track = np.zeros(int(SR * (total + 1)))
    last = len(starts) - 1
    for k, st in enumerate(starts):
        sig = logo(kind) if k == last else tick(kind, k)
        sig = sig / np.abs(sig).max() * (.55 if k == last else .4)
        i = int(SR * st); m = min(len(sig), len(track) - i)
        track[i:i + m] += sig[:m]
    wav = HERE / f'_track_{ticker}_{kind}.wav'
    write(wav, track)
    out = HERE.parent / 'out' / f'{ticker}_{kind}.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(HERE.parent / 'out' / f'{ticker}.mp4'), '-i', str(wav),
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', str(out)], check=True)
    wav.unlink()
    print(out)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'mux':
        mux(sys.argv[2], sys.argv[3])
    else:
        make()
