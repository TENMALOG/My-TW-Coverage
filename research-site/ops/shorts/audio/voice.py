"""Narrated Short (trial): one voice line per scene, scenes stretched to fit, voice mixed over the theme.

  py voice.py 2330 HsiaoChen     -> out/2330_vo_HsiaoChen.mp4

Lines come from ops/shorts/voice/{ticker}.json {"lines": [one per scene, null = no voice]}.
Voices: Microsoft neural TTS through edge-tts (zh-TW-HsiaoChenNeural / zh-TW-YunJheNeural) — preview only;
publishing needs a licensed route (Azure Speech or a recorded human voice).
"""
import asyncio
import json
import subprocess
import sys
from pathlib import Path

import edge_tts
import numpy as np

HERE = Path(__file__).resolve().parent
SH = HERE.parent
FFMPEG = r'C:\Program Files\ffmpeg-7.1.1\bin\ffmpeg.exe'
SR = 48000
LEAD, TAIL = .35, .45          # voice starts this long after the scene cut; scene ends this long after the voice


def tts(text, voice, path):
    if voice in ('Yating', 'Zhiwei', 'Hanhan'):          # offline Windows OneCore voices
        path = path.with_suffix('.wav'); txt = path.with_suffix('.txt')
        txt.write_text(text, encoding='utf-8')
        subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(HERE / 'winrt_tts.ps1'),
                        '-TextFile', str(txt), '-Voice', voice, '-Out', str(path)], check=True)
    else:
        async def go():
            await edge_tts.Communicate(text, f'zh-TW-{voice}Neural', rate='+10%').save(str(path))
        asyncio.run(go())
    raw = subprocess.run([FFMPEG, '-loglevel', 'error', '-i', str(path), '-f', 's16le', '-ac', '1', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, '<i2').astype(float) / 32768


def main(ticker, voice):
    lines = json.loads((SH / 'voice' / f'{ticker}.json').read_text(encoding='utf-8'))['lines']
    tmp = SH / 'voice' / '_tmp'; tmp.mkdir(exist_ok=True)
    clips = [tts(l, voice, tmp / f'{ticker}_{i}.mp3') if l else None for i, l in enumerate(lines)]
    sb = json.loads((SH / 'storyboard' / f'{ticker}.json').read_text(encoding='utf-8'))
    sb['dur'] = [LEAD + len(c) / SR + TAIL if c is not None else 0 for c in clips]
    tag = f'{ticker}vo{voice[:2]}'
    (SH / 'storyboard' / f'{tag}.json').write_text(json.dumps(sb, ensure_ascii=False), encoding='utf-8')
    env = {'PYTHONIOENCODING': 'utf-8', **__import__('os').environ}
    subprocess.run([sys.executable, 'record_short.py', 'video', tag, '6'], cwd=SH, env=env, check=True)
    # score with the voice: score.py reads the clips and scene starts from this sidecar
    np.save(tmp / f'{tag}_voice.npy', np.array([c if c is not None else np.zeros(1) for c in clips], dtype=object),
            allow_pickle=True)
    subprocess.run([sys.executable, 'score.py', tag, '--voice', str(tmp / f'{tag}_voice.npy')], cwd=HERE, env=env, check=True)
    out = SH / 'out' / f'{ticker}_vo_{voice}.mp4'
    (SH / 'out' / f'{tag}_full.mp4').replace(out)
    (SH / 'out' / f'{tag}.mp4').unlink()
    (SH / 'storyboard' / f'{tag}.json').unlink()
    print(out)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'HsiaoChen')
