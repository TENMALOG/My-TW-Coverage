# _generated：全產業章節清單（尚未併入 _quarto.yml）

本資料夾的檔案由 `research-site/scripts/generic/` 的產生器寫出，請勿手動修改。

| 檔案 | 產生器 | 內容 |
|---|---|---|
| `book-chapters.yml` | `build_book_config.py` | Quarto `book.chapters` 清單：首頁與「研究主文」照舊，接著依公司家數由多到少，每個產業一個 part（產業專章＋該產業公司頁；航太與國防沿用既有章節與頁面順序），最後是公司索引與參考文獻。 |
| `company-pages-build-log.jsonl` | `build_company_pages_all.py` | 年報事實檔未通過身分核對而被整份略過的紀錄（每行一家公司與原因）；空檔表示沒有被略過的檔案。 |

## 產生順序

```
.venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_verified_sentences.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_company_pages_all.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_industry_chapters.py
.venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_book_config.py
```

年報事實檔（`data/company-facts/{ticker}.json`）新增或更新後，重跑第 2、3 步即可；只會採用 `verification.status == "PASS"` 的事實。

## 如何併入 `_quarto.yml`

`build_book_config.py` 不會改動 `research-site/_quarto.yml`。要正式採用時：

1. 打開 `research-site/_quarto.yml`，找到 `book:` 底下的 `  chapters:` 區塊（從 `  chapters:` 那一行到 `  appendices:` 的前一行）。
2. 用 `book-chapters.yml` 第二行起的內容（`  chapters:` 開頭，縮排已對齊 `book:` 底下）整段取代該區塊。`appendices:` 及其後的設定不變。
3. 舊的「產業專章」與「公司研究頁：航太與國防」兩個 part 已被併入新的「航太與國防」part，不要重複保留。

也可以讓腳本把清單寫進一份**複本**：

```
.venv/Scripts/python.exe -X utf8 research-site/scripts/generic/build_book_config.py --merge-into <複本資料夾>/_quarto.yml
```

腳本拒絕直接寫入 repo 內的 `research-site/_quarto.yml`。加上 `--industry "Electronic Components"` 等參數可以只放部分產業（航太與國防一律保留），適合試算繪製時間。

## 併入前請注意

- 全部 98 個產業、1,838 個章節檔一起繪製會很慢，側邊目錄也很長；可先分批上線（用 `--industry` 選產業）。
- `scripts/build_company_index.py` 以 `chapters/companies/*.qmd` 是否存在判定 T2，產生全產業公司頁後重跑它，會把所有公司都標成 T2；需要先調整該腳本的判定方式。
- 公司頁與產業章用 Pandoc 註腳標示來源，不使用 `filters/refs.lua` 的〔編號〕標記，因此不需要更新 `ref-map.json` 或參考文獻檔。
