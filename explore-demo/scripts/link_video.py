"""Local demo only: expose the rendered videos at dist/video/{ticker}.mp4 (a junction, no copy). Production uses
PUBLIC_VIDEO_URL (Cloudflare R2) instead."""
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
src = ROOT / 'research-site/ops/shorts/out/web-video'
dst = ROOT / 'explore-demo/dist/video'
if dst.exists() and not any(dst.iterdir()):
    dst.rmdir()
if not dst.exists() and src.exists():
    subprocess.run(['cmd', '/c', 'mklink', '/J', str(dst), str(src)], check=True, capture_output=True)
print('video:', len(list(dst.glob('*.mp4'))) if dst.exists() else 0)
