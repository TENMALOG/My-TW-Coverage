@echo off
rem Daily job (Windows Task Scheduler): upload the next unlisted videos until the YouTube daily limit, then refresh the
rem site's youtube-ids.csv. Progress is resumable; see youtube_upload.py.
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0"
"C:\Users\Neo Pegasus\AppData\Local\Programs\Python\Python313\python.exe" youtube_upload.py upload --limit 2000 --audited >> "out\upload\youtube-daily.log" 2>&1
