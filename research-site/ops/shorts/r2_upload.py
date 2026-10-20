"""Upload the web videos (out/web-video/{ticker}.mp4) and posters to Cloudflare R2 for 股.tw.

  py r2_upload.py check     test the credentials and list what is already in the bucket
  py r2_upload.py upload    upload missing or changed files (compares size), resumable

Credentials stay OUTSIDE the repo in %USERPROFILE%/.tenmalog-r2/r2.json, written by the chairman:
  {"account_id": "...", "access_key_id": "...", "secret_access_key": "...", "bucket": "gutw-video"}
"""
import concurrent.futures as cf
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VIDEO = HERE / 'out' / 'web-video'
POSTER = HERE / 'out' / 'master'
CONF = Path.home() / '.tenmalog-r2' / 'r2.json'


def client():
    import boto3
    if not CONF.exists():
        sys.exit(f'找不到 {CONF}：請依說明建立 R2 金鑰設定檔。')
    c = {k: v.strip() for k, v in json.loads(CONF.read_text(encoding='utf-8')).items()}
    # check the shape before use so a misplaced secret is never echoed in an error message
    import re
    if not re.fullmatch(r'[0-9a-f]{32}', c['account_id']):
        sys.exit('r2.json 的 account_id 格式不對：應該是 32 碼的帳戶 ID（0-9、a-f），不是 API 權杖。')
    if not re.fullmatch(r'[0-9a-f]{32}', c['access_key_id']) or not re.fullmatch(r'[0-9a-f]{64}', c['secret_access_key']):
        sys.exit('r2.json 的 access_key_id（32 碼）或 secret_access_key（64 碼）格式不對。')
    s3 = boto3.client('s3', endpoint_url=f"https://{c['account_id']}.r2.cloudflarestorage.com",
                      aws_access_key_id=c['access_key_id'], aws_secret_access_key=c['secret_access_key'], region_name='auto')
    return s3, c['bucket']


def existing(s3, bucket):
    have = {}
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket):
        for o in page.get('Contents', []):
            have[o['Key']] = o['Size']
    return have


def files():
    out = [(f, f'video/{f.name}', 'video/mp4') for f in sorted(VIDEO.glob('*.mp4'))]
    out += [(f, f"poster/{f.name.replace('_poster', '')}", 'image/jpeg') for f in sorted(POSTER.glob('*_poster.jpg'))]
    return out


def upload():
    s3, bucket = client()
    have = existing(s3, bucket)
    todo = [x for x in files() if have.get(x[1]) != x[0].stat().st_size]
    print(f'待上傳 {len(todo)}，已在 R2 {len(have)}', flush=True)

    def put(x):
        f, key, ctype = x
        s3.upload_file(str(f), bucket, key, ExtraArgs={'ContentType': ctype, 'CacheControl': 'public, max-age=31536000'})
        return key

    done = 0
    with cf.ThreadPoolExecutor(8) as ex:
        for fut in cf.as_completed([ex.submit(put, x) for x in todo]):
            fut.result()
            done += 1
            if done % 100 == 0 or done == len(todo):
                print(f'{done}/{len(todo)}', flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if cmd == 'check':
        s3, bucket = client()
        have = existing(s3, bucket)
        print(f'連線成功：bucket {bucket}，目前 {len(have)} 個檔案')
    elif cmd == 'upload':
        upload()
