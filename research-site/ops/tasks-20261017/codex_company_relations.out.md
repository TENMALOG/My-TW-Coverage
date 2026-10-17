已依任務檔建立兩個檔案：

- [company_relations.py](</C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/research-site/scripts/generic/company_relations.py>)：`load_edges()` 建立雙方視角的關係索引並去重；`render_relations()` 產生含來源註腳的 Markdown 表格。
- [test_company_relations.py](</C:/Users/Neo Pegasus/Documents/ChatGPT/078-kaori sample/artifacts/stock-coverage-audit-20261003/incoming/latest-audit/My-TW-Coverage/research-site/scripts/generic/test_company_relations.py>)：涵蓋角色反轉、去重、空結果、表格列數、註腳與連結。

**測試結果：5 項通過。** 實際資料涵蓋 **449 家**有至少一筆關係的公司，雙方頁面合計 **1,108 列**；449 家頁面均已成功試算。專案虛擬環境未安裝 pytest，因此測試使用本機 Python 3.13 執行。