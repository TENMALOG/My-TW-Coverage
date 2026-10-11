# Rerun notes — 1722 台肥不動產與南港開發

## Original claim

> (2) 不動產 — 持有全台土地約 53 萬坪，南港經貿園區為台北市最大地主 (約 3.58 萬坪)，南港 C3 地上權案帶來 150 億元現金、C2 觀光旅館暨辦公大樓總投資逾 100 億元；

## Findings

- **全台土地**：台肥現行官網列約170公頃，換算約51.4萬坪。2009年MoneyDJ轉載的公司資料是全台533,843.53坪，約53.4萬坪；這解釋原數字，但只代表2009年，不能當現況。現行面積應改用官方頁較新的約170公頃。
- **南港最大地主及3.58萬坪**：台肥2020刊物的中文原文是「台肥公司身為台北市南港經貿園區之最大地主」，英文版本也限於Nangang Economic and Trade Park in Taipei City。這支持園區內地主排名，不支持「台肥是全台北市最大地主」。3.58萬坪在2009 MoneyDJ資料中為南港經貿園區持地面積，含當時已設定給中信金的地上權；沒有足夠新資料驗證這是現今面積。
- **C3現金**：台肥2015公司刊物記載C3權利金分兩階段，每階段150億元；第一階段為45年權利金並帶來150億元現金，第二階段另為40年權利金150億元。因此原句需說明150億元是第一階段，整個規劃總權利金為300億元。
- **C2投資**：台肥2015動工公告估算觀光旅館暨辦公大樓總投資逾100億元。111年度（2022）年報將C2總需資金列為123.85億元、截至2022-12-31實際動支約106.98億元、2023年預定使用16.87億元。

## Rerun outcome

Overall `CANDIDATE_ACCEPTED` after a scope and period-preserving rewrite. The current area is taken from the present company page; old 53萬/3.58萬坪 values are explicitly dated; the land ranking is attributed to the issuer and limited to the Nangang Economic and Trade Park; C3 cash and C2 cost figures are time- and basis-bound. Final acceptance still belongs to strong-model adjudication.

Suggested supported rewrite:

> 台肥現行官網稱持有土地約170公頃（約51.4萬坪）；台肥2020年刊物稱其為台北市南港經貿園區最大地主。2009年轉載的公司資料曾列全台土地約53.38萬坪、南港經貿園區約3.58萬坪。C3地上權權利金於2015年分兩階段、各150億元，第一階段帶來150億元現金；台肥111年度年報列C2開發案總需資金123.85億元，截至2022年底實際動支約106.98億元。

## Provenance

Source hashes and raw file paths are recorded in `manifest.json`; author-batch and normalized-claim hashes remain in the result. The 2009 MoneyDJ figure is treated only as a historical third-party report of data attributed to the company.
