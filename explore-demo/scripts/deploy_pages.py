"""Build the production site and upload dist/ to Cloudflare Pages (project gutw-research -> research.股.tw).

  py scripts/deploy_pages.py            build + checks + deploy
  py scripts/deploy_pages.py --check    build + checks only
  ... --archive v0.2=<dir>                also serve a frozen earlier research-site build at /paper/v0.2/ (noindex via _headers)

Credentials stay outside the repo in %USERPROFILE%/.tenmalog-cf/cf.json ({"api_token", "account_id"}); they are passed
to wrangler through the environment and never printed. The share cards and posters are generated locally (the
licensed font never leaves this machine), so Pages receives pre-built files only.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
PAPER = ROOT.parent / 'research-site' / '_site'    # the Quarto research site (查證層), served at /paper/
PROJECT = 'gutw-research'
WRANGLER = 'wrangler@4.155.0'


def run(cmd, env=None):
    print('>', ' '.join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, env=env, check=True, shell=(os.name == 'nt'))


def main():
    # the local demo links dist/video to 3 GB of videos; remove the link itself (never its contents) before building
    v = DIST / 'video'
    if v.is_junction() or v.is_symlink():
        os.rmdir(v) if v.is_junction() else v.unlink()
    run(['npm', 'run', 'build'])
    # the research site uses relative links only, so it can live under /paper/ unchanged
    assert (PAPER / 'index.html').exists(), 'render research-site first'
    shutil.copytree(PAPER, DIST / 'paper', dirs_exist_ok=True)
    # superseded editions stay readable for existing citations; the current build must not already use the name
    for arg in [a.split('=', 1)[1] for a in sys.argv if a.startswith('--archive=')]:
        name, src = arg.split('=', 1)
        assert re.fullmatch(r'v\d+(\.\d+)*', name) and (Path(src) / 'index.html').exists(), f'bad --archive {arg}'
        assert not (PAPER / name).exists(), f'{name} collides with the current research site'
        shutil.copytree(src, DIST / 'paper' / name)
    files = [p for p in DIST.rglob('*') if p.is_file()]
    big = [p for p in files if p.stat().st_size > 25 * 1024 * 1024]
    assert not (DIST / 'video').exists(), 'dist/video must not be deployed'
    assert len(files) < 20000, f'{len(files)} files exceeds the Pages limit'
    assert not big, f'files over 25 MB: {big[:3]}'
    assert not list(DIST.rglob('*.otf')) and not list(DIST.rglob('*.ttf')), 'font files must never be deployed'
    # a real link or asset pointing at a local server (Quarto's own link-filter regex mentions localhost and is fine)
    local = re.compile(r'(?:href|src|content|action)="https?://(?:localhost|127\.0\.0\.1)')
    leaked = [p for p in DIST.rglob('*.html') if local.search(p.read_text(encoding='utf-8', errors='ignore'))]
    assert not leaked, f'localhost URLs in {leaked[:3]}'
    print(f'checks ok: {len(files)} files, {sum(p.stat().st_size for p in files) / 1e6:.0f} MB', flush=True)
    if '--check' in sys.argv:
        return
    c = json.loads((Path.home() / '.tenmalog-cf' / 'cf.json').read_text(encoding='utf-8'))
    env = {**os.environ, 'CLOUDFLARE_API_TOKEN': c['api_token'].strip(), 'CLOUDFLARE_ACCOUNT_ID': c['account_id'].strip()}
    have = subprocess.run(['npx', '--yes', WRANGLER, 'pages', 'project', 'list'], cwd=ROOT, env=env,
                          capture_output=True, text=True, encoding='utf-8', shell=(os.name == 'nt'))
    if PROJECT not in (have.stdout or ''):
        run(['npx', '--yes', WRANGLER, 'pages', 'project', 'create', PROJECT, '--production-branch', 'main'], env)
    run(['npx', '--yes', WRANGLER, 'pages', 'deploy', 'dist', '--project-name', PROJECT, '--branch', 'main',
         '--commit-dirty=true'], env)


if __name__ == '__main__':
    main()
