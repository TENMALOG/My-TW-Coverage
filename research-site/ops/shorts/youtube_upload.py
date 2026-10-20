"""Upload the company videos to the 尼奧天馬 @tenmalog channel as UNLISTED (embeddable on 股.tw), then publish a
few per day.

  py youtube_upload.py auth                 one-time: opens the browser for Google sign-in (the chairman signs in)
  py youtube_upload.py upload [--limit 90]  upload pending videos (largest market cap first) as unlisted
  py youtube_upload.py publish [--per-day 3] switch the next videos (market-cap order) from unlisted to public
  py youtube_upload.py status               counts

Credentials stay OUTSIDE the repo in %USERPROFILE%/.tenmalog-youtube/ (client_secret.json from Google Cloud,
token.json written after sign-in). Never commit them. Progress is written back to out/upload/上傳清單.csv after every
single video (youtube_id, 公開日期), so any run can stop (quota, network) and the next run continues.
"""
import argparse
import csv
import datetime as dt
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
UP = HERE / 'out' / 'upload'
LIST = UP / '上傳清單.csv'
LOG = UP / 'youtube.log'
CRED = Path.home() / '.tenmalog-youtube'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload', 'https://www.googleapis.com/auth/youtube']


def log(msg):
    line = f'{dt.datetime.now():%Y-%m-%d %H:%M:%S} {msg}'
    print(line, flush=True)
    with LOG.open('a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def service(interactive=False):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    tok = CRED / 'token.json'
    creds = Credentials.from_authorized_user_file(str(tok), SCOPES) if tok.exists() else None
    if not creds or not creds.valid:
        refreshed = False
        if creds and creds.expired and creds.refresh_token:
            from google.auth.exceptions import RefreshError
            try:
                creds.refresh(Request())
                refreshed = True
            except RefreshError as e:
                log(f'授權已失效（測試模式每 7 天一次），請執行 py youtube_upload.py auth 重新登入：{str(e)[:120]}')
        if not refreshed:
            if not interactive:
                log('需要重新授權：請執行 py youtube_upload.py auth')
                sys.exit(2)
            secret = CRED / 'client_secret.json'
            if not secret.exists():
                sys.exit(f'找不到 {secret}：請先把 Google Cloud 下載的 OAuth 用戶端金鑰檔放到這裡（檔名改成 client_secret.json）。')
            creds = InstalledAppFlow.from_client_secrets_file(str(secret), SCOPES).run_local_server(port=0, prompt='consent')
        CRED.mkdir(exist_ok=True)
        tok.write_text(creds.to_json(), encoding='utf-8')
    return build('youtube', 'v3', credentials=creds, cache_discovery=False)


def rows():
    rs = list(csv.DictReader(open(LIST, encoding='utf-8-sig')))
    cap = {r['ticker']: float(r['market_cap_mn_twd'] or 0) for r in csv.DictReader(open(SITE / 'catalog/release-scope-companies.csv', encoding='utf-8-sig'))}
    for r in rs:
        r.setdefault('公開日期', '')
        r['_cap'] = cap.get(r['代號'], 0)
    return rs


def save(rs):
    fields = [k for k in rs[0] if not k.startswith('_')]
    tmp = LIST.with_suffix('.tmp')
    with open(tmp, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rs)
    tmp.replace(LIST)


def quota_hit(e):
    s = str(e)
    return any(k in s for k in ('quotaExceeded', 'uploadLimitExceeded', 'rateLimitExceeded', 'dailyLimitExceeded'))


def playlist_id(yt, title, cache):
    if title in cache:
        return cache[title]
    req = yt.playlists().list(part='snippet', mine=True, maxResults=50)
    while req:
        res = req.execute()
        for p in res.get('items', []):
            cache[p['snippet']['title']] = p['id']
        req = yt.playlists().list_next(req, res)
    if title not in cache:
        p = yt.playlists().insert(part='snippet,status', body={
            'snippet': {'title': title, 'description': '股.tw 研究室：每一家上市櫃公司，每一句都附年報頁碼。製作：尼奧天馬 @tenmalog',
                        'defaultLanguage': 'zh-Hant'},
            'status': {'privacyStatus': 'public'}}).execute()
        cache[title] = p['id']
        log(f'playlist created: {title}')
    return cache[title]


def upload(limit):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
    yt = service()
    rs = rows()
    todo = sorted([r for r in rs if not r['youtube_id'].strip()], key=lambda r: -r['_cap'])[:limit]
    log(f'upload: {len(todo)} this run, {sum(1 for r in rs if r["youtube_id"].strip())} already uploaded of {len(rs)}')
    cache = {}
    for r in todo:
        meta = json.loads((HERE / 'out' / 'meta' / f"{r['代號']}.json").read_text(encoding='utf-8'))
        body = {'snippet': {'title': meta['title'], 'description': meta['description'],
                            'tags': [h.lstrip('#') for h in meta['hashtags']] + ['股.tw研究室', '尼奧天馬'],
                            'categoryId': '27', 'defaultLanguage': 'zh-Hant', 'defaultAudioLanguage': 'zh-Hant'},
                'status': {'privacyStatus': 'unlisted', 'embeddable': True, 'selfDeclaredMadeForKids': False,
                           'license': 'youtube', 'publicStatsViewable': True}}
        media = MediaFileUpload(str(UP / r['資料夾'] / r['影片檔']), mimetype='video/mp4', chunksize=8 * 1024 * 1024, resumable=True)
        try:
            req = yt.videos().insert(part='snippet,status', body=body, media_body=media)
            res = None
            while res is None:
                _, res = req.next_chunk()
            r['youtube_id'] = res['id']
            save(rs)
            log(f"{r['代號']} {r['公司']} uploaded {res['id']}")
            for attempt in range(3):   # 409 "operation was aborted" happens right after a playlist is created
                try:
                    yt.playlistItems().insert(part='snippet', body={'snippet': {
                        'playlistId': playlist_id(yt, r['播放清單'], cache),
                        'resourceId': {'kind': 'youtube#video', 'videoId': res['id']}}}).execute()
                    break
                except HttpError as e:
                    log(f"{r['代號']} playlist add failed ({attempt + 1}/3): {str(e)[:160]}")
                    if quota_hit(e) or attempt == 2:
                        break
                    time.sleep(3)
        except HttpError as e:
            log(f"{r['代號']} upload stopped: {str(e)[:200]}")
            if quota_hit(e):
                log('daily limit reached: run again tomorrow (progress is saved)')
                break
            time.sleep(5)
    sync_ids()


def publish(per_day):
    from googleapiclient.errors import HttpError
    yt = service()
    rs = rows()
    today = dt.date.today().isoformat()
    done_today = sum(1 for r in rs if r['公開日期'] == today)
    todo = sorted([r for r in rs if r['youtube_id'].strip() and not r['公開日期']], key=lambda r: -r['_cap'])[:max(0, per_day - done_today)]
    for r in todo:
        try:
            cur = yt.videos().list(part='status', id=r['youtube_id']).execute()['items'][0]['status']
            cur['privacyStatus'] = 'public'
            yt.videos().update(part='status', body={'id': r['youtube_id'], 'status': cur}).execute()
            r['公開日期'] = today
            save(rs)
            log(f"{r['代號']} {r['公司']} published {r['youtube_id']}")
        except HttpError as e:
            log(f"{r['代號']} publish failed: {str(e)[:200]}")
            if quota_hit(e):
                break


def sync_ids():
    """Write research-site/data/youtube-ids.csv for the website (every uploaded video, unlisted or public)."""
    rs = rows()
    with open(SITE / 'data/youtube-ids.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ticker', 'youtube_id'])
        for r in rs:
            if r['youtube_id'].strip():
                w.writerow([r['代號'], r['youtube_id'].strip()])


def status():
    rs = rows()
    up = sum(1 for r in rs if r['youtube_id'].strip())
    pub = sum(1 for r in rs if r['公開日期'])
    print(f'總數 {len(rs)}｜已上傳（不公開）{up}｜已公開 {pub}｜待上傳 {len(rs) - up}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['auth', 'upload', 'publish', 'status'])
    ap.add_argument('--limit', type=int, default=90)
    ap.add_argument('--per-day', type=int, default=3)
    ap.add_argument('--audited', action='store_true', help='Google Cloud project passed the YouTube API audit (otherwise uploads get locked private)')
    a = ap.parse_args()
    if a.cmd == 'auth':
        (CRED / 'token.json').unlink(missing_ok=True)
        service(interactive=True)
        print('授權完成，金鑰已存在', CRED)
    elif a.cmd == 'upload':
        if not a.audited and a.limit > 1:
            sys.exit('未通過 YouTube API 稽核的專案，上傳的影片會被鎖成私人（無法內嵌）。通過稽核後加 --audited；測試只能 --limit 1。')
        upload(a.limit)
    elif a.cmd == 'publish':
        publish(a.per_day)
    else:
        status()
