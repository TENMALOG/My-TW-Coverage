"""Full sound for a company Short: original lo-fi theme + brand sound effects, mixed to YouTube loudness.

  py score.py 2330            -> out/2330_full.mp4   (needs out/2330.mp4 from record_short.py)
  py score.py 2330 --wav      -> also keeps audio/_mix_2330.wav

Sound identity from the brand colours (everything synthesized here, no third-party samples):
  暖紙白 #F2EFE8  warm bed: electric-piano chords, vinyl crackle, paper flips and taps
  墨黑   #181715  weight:   bass, H2 impacts on the charts, the self-claim stamp
  珊瑚橘 #FF573F  accent:   pluck melody, sticker pops, progress-bar notes, the closing sound mark

Theme: 96 BPM, swung eighths, | Fmaj7 | Em7 | Dm7 | G7 | resolving to Cmaj9 on the sound mark. The grid is
anchored so the sound mark lands on a downbeat exactly when the 「股.tw 研究室」 sticker appears in the outro.
Intro is piano only; drums and bass enter on the first bar line after the intro scene. Music is ducked under
every impact so the weight reads clearly, and sits ~10 dB under the effects.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

from make_sounds import FFMPEG, SR, pluck, pop, write
from sfx import bp, env, fall, kick, lp, sweep_noise, tap, thud, whoosh

HERE = Path(__file__).resolve().parent
RNG = np.random.default_rng(11)
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
LUFS = float(__import__('os').environ.get('SHORTS_LUFS', '-18'))   # chairman 2026-10-20: -14 was louder than other videos
FX_GAIN = .5                                  # effects bus level relative to the theme
SWING = .58                                   # off-beat eighth sits at 58% of the beat


def hz(name):
    n = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[name[0]]
    return 440 * 2 ** ((n + 12 * (int(name[-1]) + 1) - 69) / 12)


CHORDS = [('F2', ['F3', 'A3', 'C4', 'E4']), ('E2', ['E3', 'G3', 'B3', 'D4']),
          ('D2', ['D3', 'F3', 'A3', 'C4']), ('G2', ['G3', 'B3', 'D4', 'F4'])]
FINAL = ('C2', ['C3', 'G3', 'B3', 'D4', 'E4'])
# the hook over Dm7 | G7 that climbs into the sound mark (beat, note, length in beats)
HOOK = [[(0, 'A5', 1), (1, 'C6', .58), (1 + SWING, 'A5', 1), (2 + SWING, 'G5', 1.4)],
        [(0, 'F5', 1), (1, 'G5', .58), (1 + SWING, 'B5', 1), (2 + SWING, 'D6', 1.4)]]
TICKS = ['C5', 'D5', 'E5', 'G5', 'A5', 'C6', 'D6', 'E6', 'G6', 'A6', 'C7', 'D7']


# ---------------------------------------------------------------- instruments
def ep(f, dur, vel=1.0):
    """Electric piano: two-operator FM with a decaying index and gentle tremolo."""
    n = int(SR * dur); t = np.arange(n) / SR
    idx = 1.6 * np.exp(-t / .25) + .25
    x = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    x += .15 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / .1)
    return x * env(n, .006, 1.1) * (1 + .12 * np.sin(2 * np.pi * 4.5 * t)) * vel


def bass(f, dur, vel=1.0):
    n = int(SR * dur); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * 2 * f * t)
    x = np.tanh(1.6 * x) * np.minimum(t / .01, 1) * np.exp(-t / 1.4)
    rel = np.minimum(1, (n - np.arange(n)) / (SR * .04))
    return x * rel * vel


def drum(kind):
    if kind == 'kick':
        return lp(kick(110, 48, .45, .13), 1800) * 1.1
    if kind == 'snare':
        n = int(SR * .3)
        return (bp(RNG.uniform(-1, 1, n), 1200, 5000) * env(n, .001, .06) * .8
                + np.sin(2 * np.pi * 185 * np.arange(n) / SR) * env(n, .001, .04) * .6
                + bp(RNG.uniform(-1, 1, n), 2000, 4500) * env(n, .0005, .012) * 1.2)   # finger-snap edge
    n = int(SR * .08)
    return bp(RNG.uniform(-1, 1, n), 6500, 14000) * env(n, .0005, .018)


def vinyl(dur):
    n = int(SR * dur)
    hiss = lp(RNG.normal(0, 1, n), 3000) * .012
    crackle = np.zeros(n)
    for i in RNG.integers(0, n, int(dur * 9)):
        crackle[i] = RNG.uniform(.2, 1) * RNG.choice([-1, 1])
    return hiss + bp(crackle, 1500, 9000) * .5


def add(buf, at, sig, g=1.0):
    i = int(round(SR * at))
    if i < 0:
        sig, i = sig[-i:], 0
    m = min(len(sig), len(buf) - i)
    if m > 0:
        buf[i:i + m] += g * sig[:m]


# ---------------------------------------------------------------- music
def music(total, mark, drums_from):
    buf = np.zeros(int(SR * (total + 2)))
    first = mark - np.ceil(mark / BAR) * BAR          # bar line at or before t = 0, on the mark's grid
    nbars = int(round((mark - first) / BAR))
    for b in range(nbars):
        t0 = first + b * BAR
        root, chord = CHORDS[(b - nbars) % 4]        # bar right before the mark is always G7
        full = t0 >= drums_from - 1e-6
        for pos, vel, ln in [(0, .9, 1.6), (1 + SWING, .55, .6), (3, .45, .9)]:
            for k, nme in enumerate(chord):
                add(buf, t0 + pos * BEAT + k * .012, ep(hz(nme), ln * BEAT + .5, vel * .22))
        if full:
            add(buf, t0, bass(hz(root), 1.5 * BEAT), .35)
            add(buf, t0 + (2 + SWING) * BEAT, bass(hz(root), .9 * BEAT), .3)
            for pos in (0, 2 + SWING):
                add(buf, t0 + pos * BEAT, drum('kick'), .4)
            for pos in (1, 3):
                add(buf, t0 + pos * BEAT, drum('snare'), .32)
            for e in range(8):
                add(buf, t0 + (e // 2 + (SWING if e % 2 else 0)) * BEAT, drum('hat'), .16 if e % 2 else .24)
        # hook: quietly once mid-video, full in the last two bars before the mark
        hb = (b - nbars) % 4
        if hb in (2, 3) and (b >= nbars - 2 or (full and b == nbars - 6)):
            g = .5 if b >= nbars - 2 else .28
            for pos, nme, ln in HOOK[hb - 2]:
                add(buf, t0 + pos * BEAT, pluck(hz(nme), ln * BEAT + .3), g)
    root, chord = FINAL                              # resolution on the mark
    for k, nme in enumerate(chord):
        add(buf, mark + k * .018, ep(hz(nme), 3.5, .26))
    add(buf, mark, bass(hz(root), 3.0), .5)
    add(buf, mark, drum('kick'), .6)
    buf = lp(np.tanh(buf * 1.3), 7000)               # lo-fi tape softening
    buf += vinyl(len(buf) / SR)
    return buf


# ---------------------------------------------------------------- effects
def ov(*sigs):
    out = np.zeros(max(len(x) for x in sigs))
    for x in sigs:
        out[:len(x)] += x
    return out


def sfx_sound(e):
    g, ty = e.get('g', 1), e['type']
    n = int(SR * .3)
    if ty == 'thud':
        return thud('H2', g) * 1.1
    if ty == 'fall':
        return fall(e['d'], g)
    if ty == 'whoosh':
        return whoosh(e['d'], g)
    if ty == 'tap':
        return tap('H2', g) * .8
    if ty == 'pop':
        return ov(pop() * .55, bp(RNG.uniform(-1, 1, n), 2000, 6500) * env(n, .0005, .01) * .35) * g
    if ty == 'ding':
        f = hz('G6')
        return ov(pop() * .45, np.sin(2 * np.pi * f * np.arange(n * 2) / SR) * env(n * 2, .002, .18) * .3) * g
    if ty == 'stamp':
        return (kick(170, 70, .35, .07) + bp(RNG.uniform(-1, 1, int(SR * .35)), 300, 900)
                * env(int(SR * .35), .0005, .03) * 1.3) * .8
    if ty == 'swish':
        return sweep_noise(.32, 700, 3500, .8) * np.linspace(.3, 1, int(SR * .32)) ** 2 * .45 * g
    return None


def flip():
    out = np.zeros(int(SR * .2))
    for k in range(3):
        n = int(SR * .05)
        add(out, k * .028, bp(RNG.uniform(-1, 1, n), 1500, 5500) * env(n, .002, .012), .5 - k * .12)
    return out


def effects(ev, total, mark):
    buf = np.zeros(int(SR * (total + 2)))
    duck = np.zeros_like(buf)
    t = np.arange(len(buf)) / SR
    for e in ev:
        if e['type'] == 'scene':
            if e['k'] > 0:
                add(buf, e['t'] - .06, flip(), .7)
            add(buf, e['t'], pluck(hz(TICKS[e['k'] % len(TICKS)]), .5), .35)
            add(buf, e['t'], pop(), .25)
            continue
        s = sfx_sound(e)
        if s is None:
            continue
        add(buf, e['t'], s)
        if e['type'] in ('thud', 'stamp'):
            m = t >= e['t'] - .02
            duck[m] += .7 * min(e.get('g', 1), 1.2) * np.exp(-(t[m] - e['t']) / .35)
    # the sound mark: two sticker pops, then the coral pluck arpeggio landing on the downbeat
    for k, at in enumerate((-.26, -.14)):
        add(buf, mark + at, pop(), .7)
    for k, nme in enumerate(['C6', 'E6', 'G6', 'C7']):
        add(buf, mark + k * .07, pluck(hz(nme), 1.6), .55)
    m = t >= mark - .3
    duck[m] += .35 * np.exp(-np.maximum(t[m] - mark, 0) / 1.2)
    return buf, np.clip(1 - duck, .3, 1)


# ---------------------------------------------------------------- render
def stage_events(ticker):
    from playwright.sync_api import sync_playwright
    sb = json.loads((HERE.parent / 'storyboard' / f'{ticker}.json').read_text(encoding='utf-8'))
    with sync_playwright() as p:
        b = p.chromium.launch(channel='chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        stage = __import__('os').environ.get('SHORTS_STAGE', 'short.html')
        pg.goto((HERE.parent / stage).as_uri()); pg.evaluate('window.ready')
        total = pg.evaluate('sb => build(sb)', sb)
        ev = pg.evaluate('collect()')
        starts = pg.evaluate('START')
        b.close()
    return ev, total, starts


def mixdown(ticker, voice=None):
    ev, total, starts = stage_events(ticker)
    mark = starts[-1] + .7 + .12                     # outro 「股.tw 研究室」 sticker is fully popped here
    drums_from = starts[1] if len(starts) > 1 else 0
    fx, duck = effects(ev, total, mark)
    mus = music(total, mark, drums_from)
    mus = mus[:len(fx)] if len(mus) >= len(fx) else np.pad(mus, (0, len(fx) - len(mus)))
    mix_fx, mix_mus = fx * FX_GAIN, mus * duck * .24  # chairman 2026-10-18: effects were too loud, -6 dB
    if voice is not None:                             # narrated trial: voice on top, music and effects step back
        vo = np.zeros_like(fx); act = np.zeros_like(fx)
        for st, clip in zip(starts, voice):
            if len(clip) > 1:
                i = int(SR * (st + .35)); m = min(len(clip), len(vo) - i)
                vo[i:i + m] += clip[:m]; act[max(0, i - SR // 10):i + m + SR // 5] = 1
        act = np.convolve(act, np.ones(SR // 10) / (SR // 10), 'same')     # smooth the ducking edges
        mix_mus *= 1 - .6 * act
        mix_fx *= 1 - .35 * act
        mix_fx += vo * 1.6
    mix = mix_fx + mix_mus
    n = int(SR * total)
    mix = mix[:n]
    fade = int(SR * .6)
    mix[-fade:] *= np.linspace(1, 0, fade)
    return np.tanh(mix * 1.1), ev


def loudnorm(src, dst):
    """Two-pass EBU R128 normalisation to LUFS (default -18: music-only content sat louder than other videos at -14), true peak -2 dB."""
    r = subprocess.run([FFMPEG, '-hide_banner', '-i', str(src), '-af', f'loudnorm=I={LUFS}:TP=-2:LRA=11:print_format=json',
                        '-f', 'null', '-'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    m = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', r.stderr)[-1])
    af = (f"loudnorm=I={LUFS}:TP=-2:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(src), '-af', af, '-ar', str(SR), str(dst)], check=True)


def main(ticker, keep=False, voice=None):
    mix, ev = mixdown(ticker, voice)
    raw, norm = HERE / f'_raw_{ticker}.wav', HERE / f'_mix_{ticker}.wav'
    write(raw, mix)
    loudnorm(raw, norm)
    out = HERE.parent / 'out' / f'{ticker}_full.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', str(HERE.parent / 'out' / f'{ticker}.mp4'), '-i', str(norm),
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(out)], check=True)
    raw.unlink()
    if not keep:
        norm.unlink()
    kinds = {}
    for e in ev:
        kinds[e['type']] = kinds.get(e['type'], 0) + 1
    print(out, kinds)


if __name__ == '__main__':
    vo = None
    if '--voice' in sys.argv:
        vo = list(np.load(sys.argv[sys.argv.index('--voice') + 1], allow_pickle=True))
    main(sys.argv[1], '--wav' in sys.argv, vo)
