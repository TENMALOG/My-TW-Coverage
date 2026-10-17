import json
from pathlib import Path
R = Path(__file__).resolve().parents[3] / "research-site/ops/renames"
jobs = json.load(open(R / "jobs/rn_002.json", encoding="utf8"))
notes = {
 "1708": "僅涉及確信機構法標國際認證(原艾法諾國際)更名，非發行公司本身。",
 "2013": "僅涉及股東友縳投資更名為光鉅控股，非發行公司本身。",
 "2115": "僅涉及孫公司昆山六暉更名，非發行公司本身。",
 "2002": "僅涉及子公司/投資事業(中鋼日鐵越南公司)改名，非發行公司本身。",
 "2030": "僅涉及驗證機構英商勞氏更名，非發行公司本身。",
}
default = "命中僅為委員會、守則、報告書、制度、小組或酬金表欄位等更名，非發行公司本身更名。"
with open(R / "out/rn_002.jsonl", "w", encoding="utf8") as f:
    for e in jobs:
        f.write(json.dumps({"id": e["id"], "renames": [], "note": notes.get(e["id"], default)}, ensure_ascii=False) + "\n")
