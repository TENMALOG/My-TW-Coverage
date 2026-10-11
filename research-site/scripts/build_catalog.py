"""Build the research catalog and release-scope manifest (read-only on all inputs).

Outputs go to research-site/catalog/. Frozen audit deliveries, reports and
ledgers are only read; their SHA256 values are recorded in catalog-manifest.json.
"""
from __future__ import annotations

import collections
import csv
import glob
import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research-site" / "catalog"
CR = "audit-v5/semantic/candidate-rerun"
ASSESSMENT_DATE = "2026-10-08"

INPUTS = {
    "consolidated": f"{CR}/delivery/consolidated-status.jsonl",
    "accepted_originals": f"{CR}/delivery/accepted-original-claims.jsonl",
    "proposals": f"{CR}/delivery/revised-claim-proposals.jsonl",
    "summary": f"{CR}/delivery/summary.json",
    "inventory": f"{CR}/revision-pilot-001/inventory.jsonl",
    "pilot_queue": f"{CR}/revision-pilot-001/queue.jsonl",
    "pilot_outcomes": f"{CR}/revision-pilot-001/delivery/pilot-outcomes.jsonl",
    "accepted_revisions": f"{CR}/revision-pilot-001/delivery/accepted-revisions.jsonl",
    "pilot_summary": f"{CR}/revision-pilot-001/delivery/summary.json",
}

CLAIM_TYPE_ZH = {
    "objective_ranking_or_market_share": "排名或市占",
    "material_named_relationship": "具名客戶／供應關係",
    "profitability_assertion": "獲利敘述",
    "identity_changing_event": "沿革與組織變更",
    "export_concentration": "外銷集中度",
    "control_acquisition": "控制權取得",
}

VERDICT_ZH = {
    "ACCEPTED": "原句通過",
    "PARTIALLY_SUPPORTED": "部分支持",
    "PERIOD_UNRESOLVED": "期間未解決",
    "UNKNOWN_AFTER_RESEARCH": "研究後仍未知",
    "UNSUPPORTED": "不支持",
    "PARTIAL": "部分支持（初查）",
    "UNKNOWN": "未知（初查）",
}

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def jsonl(rel: str) -> list[dict]:
    with open(ROOT / rel, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_revision_ledger() -> tuple[dict, dict]:
    """Final revision result per parent claim across all finished revision batches.

    Round 1 = pilot outcomes and every batch whose queue rows do not supersede an earlier
    revision; round 2 = alternative batches (queue rows carry supersedes_revision_id).
    A parent passes if either round reached REVISED_SUPPORTED; round 1 wins when both did.
    Returns (ledger, input hashes).
    """
    base = ROOT / CR
    inputs = {}
    rounds = {1: {}, 2: {}}

    def period_of(results_path: Path) -> dict:
        out = {}
        if results_path.exists():
            for line in open(results_path, encoding="utf-8"):
                r = json.loads(line)
                if r.get("output"):
                    out[r["claim_id"]] = r["output"].get("period_assessment", "")
        return out

    pilot = base / "revision-pilot-001/delivery/pilot-outcomes.jsonl"
    pilot_period = {r["revision_id"]: r["adjudication"].get("period_assessment", "")
                    for r in jsonl(INPUTS["accepted_revisions"])}
    inputs[pilot.relative_to(ROOT).as_posix()] = sha256(pilot)
    for r in jsonl(pilot.relative_to(ROOT).as_posix()):
        rounds[1][r["parent_claim_id"]] = {**r, "batch": "revision-pilot-001",
                                           "period": pilot_period.get(r["claim_id"], "")}
    for d in sorted(base.glob("revision-*")):
        out = d / "delivery/outcomes.jsonl"
        if d.name == "revision-pilot-001" or not out.exists():
            continue
        queue = [json.loads(l) for l in open(d / "queue.jsonl", encoding="utf-8") if l.strip()]
        rnd = 2 if queue and "supersedes_revision_id" in queue[0] else 1
        periods = period_of(d / "adjudication/results.jsonl")
        inputs[out.relative_to(ROOT).as_posix()] = sha256(out)
        for r in jsonl(out.relative_to(ROOT).as_posix()):
            rec = {**r, "batch": d.name, "period": periods.get(r["claim_id"], "")}
            prev = rounds[rnd].get(r["parent_claim_id"])
            if prev is None or (prev["verdict"] != "REVISED_SUPPORTED" and r["verdict"] == "REVISED_SUPPORTED"):
                rounds[rnd][r["parent_claim_id"]] = rec

    ledger = {}
    for pid in set(rounds[1]) | set(rounds[2]):
        r1, r2 = rounds[1].get(pid), rounds[2].get(pid)
        if r1 and r1["verdict"] == "REVISED_SUPPORTED":
            ledger[pid] = {**r1, "round": 1, "passed": True}
        elif r2 and r2["verdict"] == "REVISED_SUPPORTED":
            ledger[pid] = {**r2, "round": 2, "passed": True}
        else:
            last = r2 or r1
            ledger[pid] = {**last, "round": 2 if r2 else 1, "passed": False}
    return ledger, inputs


def parse_report(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = {}
    for key, field in (("板塊", "sector"), ("產業", "industry")):
        m = re.search(rf"\*\*{key}:\*\*\s*(.+)", text)
        meta[field] = m.group(1).strip() if m else ""
    m = re.search(r"\*\*市值:\*\*\s*([\d,\.]+)", text)
    meta["market_cap_mn_twd"] = m.group(1).replace(",", "") if m else ""
    body = text.split("## 財務概況")[0]
    meta["wikilinks_outside_financials"] = len(WIKILINK.findall(body))
    meta["has_financial_section"] = "## 財務概況" in text
    meta["body_chars"] = len(body)
    return meta


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # Reports: ticker is ground truth for path mapping (folders were renamed after audit).
    reports = {}
    for f in sorted(glob.glob(str(ROOT / "Pilot_Reports" / "*" / "*.md"))):
        p = Path(f)
        ticker, _, name = p.stem.partition("_")
        assert ticker not in reports, ticker
        reports[ticker] = {
            "ticker": ticker,
            "filename_company": name,
            "industry_folder": p.parent.name,
            "report_path": p.relative_to(ROOT).as_posix(),
            "report_sha256": sha256(p),
            **parse_report(p),
        }

    consolidated = jsonl(INPUTS["consolidated"])
    accepted_orig = {r["claim_id"]: r for r in jsonl(INPUTS["accepted_originals"])}
    inventory = {r["parent_claim_id"]: r for r in jsonl(INPUTS["inventory"])}
    pilot_queue = {r["parent_claim_id"]: r for r in jsonl(INPUTS["pilot_queue"])}
    ledger, ledger_inputs = load_revision_ledger()

    path_remaps = []
    claim_rows = []
    for rec in consolidated:
        c = rec["claim"]
        cid = rec["claim_id"]
        ticker = c["issuer_ticker"]
        rep = reports.get(ticker)
        if rep is None:
            raise SystemExit(f"no report for ticker {ticker}")
        if rep["report_path"] != c["report_path"]:
            path_remaps.append({"claim_id": cid, "recorded_path": c["report_path"], "current_path": rep["report_path"]})
        verdict = rec["verdict"]
        inv = inventory.get(cid)
        outcome = ledger.get(cid)
        if outcome is None:
            revision_status = "待驗證" if inv else "無修正提案"
        elif outcome["passed"]:
            revision_status = "新句通過"
        else:
            revision_status = "新句未通過（列入研究限制）"

        adoptable_text, adoption_basis, period = "", "", ""
        if cid in accepted_orig:
            adoptable_text = c["original_text"]
            adoption_basis = "原句最終 ACCEPTED"
            period = accepted_orig[cid]["adjudication"].get("period_assessment", "")
        elif outcome and outcome["passed"]:
            adoptable_text = outcome["proposed_text"]
            adoption_basis = f"新句 REVISED_SUPPORTED（第{outcome['round']}輪，{outcome['batch']}，{outcome['claim_id']}）"
            period = outcome["period"]

        claim_rows.append({
            "claim_id": cid,
            "ticker": ticker,
            "company": rep["filename_company"],
            "industry_folder": rep["industry_folder"],
            "claim_type": CLAIM_TYPE_ZH.get(cid.split(":")[1], cid.split(":")[1]),
            "stage": rec["stage"],
            "parent_verdict": verdict,
            "parent_verdict_zh": VERDICT_ZH.get(verdict, verdict),
            "original_text": c["original_text"],
            "revision_status": revision_status,
            "revision_final_verdict": outcome["verdict"] if outcome else "",
            "revision_round": outcome["round"] if outcome else "",
            "revision_id": outcome["claim_id"] if outcome else "",
            "revision_priority": inv["priority"] if inv else "",
            "preferred_proposal": inv["preferred_proposal"] if inv else "",
            "pilot_category": pilot_queue[cid]["pilot_category"] if cid in pilot_queue else "",
            "adoptable_text": adoptable_text,
            "adoption_basis": adoption_basis,
            "assessment_date": ASSESSMENT_DATE,
            "period_note": period,
        })

    by_ticker = collections.defaultdict(list)
    for row in claim_rows:
        by_ticker[row["ticker"]].append(row)

    company_rows = []
    for ticker, rep in reports.items():
        rows = by_ticker.get(ticker, [])
        adopt = [r for r in rows if r["adoptable_text"]]
        pending = [r for r in rows if r["revision_status"] == "待驗證"]
        partial_rev = [r for r in rows if r["revision_status"].startswith("新句未通過")]
        no_prop = [r for r in rows if r["revision_status"] == "無修正提案" and not r["adoptable_text"]]
        gaps = []
        if not rows:
            gaps.append("無選定查核主張；報告正文未經獨立查核")
        if pending:
            gaps.append(f"{len(pending)} 個修正句待驗證")
        if partial_rev:
            gaps.append(f"{len(partial_rev)} 個修正句經兩輪驗證仍未通過，列入研究限制")
        if no_prop:
            gaps.append(f"{len(no_prop)} 條主張無修正提案且未通過")
        gaps.append("財務數字未經獨立核對")
        company_rows.append({
            "ticker": ticker,
            "company": rep["filename_company"],
            "industry_folder": rep["industry_folder"],
            "sector": rep["sector"],
            "report_path": rep["report_path"],
            "report_sha256": rep["report_sha256"],
            "market_cap_mn_twd": rep["market_cap_mn_twd"],
            "wikilinks_outside_financials": rep["wikilinks_outside_financials"],
            "planned_content": "公司研究頁（查核主張＋限制）" if rows else "公司索引頁（基本資料，標示未深入研究）",
            "scope_tier": "T1 已有查核主張" if rows else "T0 僅索引",
            "claims_in_scope": len(rows),
            "claim_ids": ";".join(r["claim_id"] for r in rows),
            "adoptable_claims": len(adopt),
            "adoptable_claim_ids": ";".join(r["claim_id"] for r in adopt),
            "revisions_pending": len(pending),
            "data_period": f"評估基準日 {ASSESSMENT_DATE}" if rows else "",
            "gaps": "；".join(gaps),
            "needs_new_research": "是",
            "release_status": "未開始",
        })

    # Industry summary
    ind = collections.defaultdict(lambda: collections.Counter())
    for r in company_rows:
        s = ind[r["industry_folder"]]
        s["companies"] += 1
        s["companies_with_claims"] += bool(r["claims_in_scope"])
        s["market_cap_mn_twd"] += float(r["market_cap_mn_twd"] or 0)
    for r in claim_rows:
        s = ind[r["industry_folder"]]
        s["claims"] += 1
        s["adoptable"] += bool(r["adoptable_text"])
        s["relationship_claims"] += r["claim_type"] == "具名客戶／供應關係"
        s["strong_adjudicated"] += r["stage"] == "strong_adjudication"
        s["pending_revisions"] += r["revision_status"] == "待驗證"
        s["unknown_like"] += r["parent_verdict"] in ("UNKNOWN", "UNKNOWN_AFTER_RESEARCH", "UNSUPPORTED")
    industry_rows = []
    for name, s in sorted(ind.items(), key=lambda kv: -kv[1]["claims"]):
        industry_rows.append({
            "industry_folder": name,
            "companies": s["companies"],
            "companies_with_claims": s["companies_with_claims"],
            "claim_coverage_pct": round(100 * s["companies_with_claims"] / s["companies"], 1),
            "claims": s["claims"],
            "adoptable": s["adoptable"],
            "relationship_claims": s["relationship_claims"],
            "strong_adjudicated": s["strong_adjudicated"],
            "pending_revisions": s["pending_revisions"],
            "unknown_like": s["unknown_like"],
            "market_cap_mn_twd": round(s["market_cap_mn_twd"]),
        })

    def write_csv(name, rows):
        with open(OUT / name, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    write_csv("release-scope-companies.csv", company_rows)
    write_csv("release-scope-claims.csv", claim_rows)
    write_csv("industry-summary.csv", industry_rows)
    with open(OUT / "path-remaps.json", "w", encoding="utf-8") as f:
        json.dump({"purpose": "Recorded report_path differs from current file; mapped by ticker. Frozen records unchanged.",
                   "remaps": path_remaps}, f, ensure_ascii=False, indent=2)

    totals = {
        "reports": len(reports),
        "industry_folders": len(ind),
        "claims_in_scope": len(claim_rows),
        "companies_with_claims": sum(1 for r in company_rows if r["claims_in_scope"]),
        "original_accepted": sum(1 for r in claim_rows if r["adoption_basis"] == "原句最終 ACCEPTED"),
        "revised_supported": sum(1 for r in claim_rows if r["revision_status"] == "新句通過"),
        "revised_supported_round2": sum(1 for r in claim_rows
                                        if r["revision_status"] == "新句通過" and r["revision_round"] == 2),
        "revisions_not_passed": sum(1 for r in claim_rows if r["revision_status"].startswith("新句未通過")),
        "revision_parents": len(inventory),
        "revisions_pending": sum(1 for r in claim_rows if r["revision_status"] == "待驗證"),
        "claims_without_proposal": sum(1 for r in claim_rows if r["revision_status"] == "無修正提案"),
        "path_remaps": len(path_remaps),
    }
    manifest = {
        "schema": "research-catalog-1",
        "assessment_date": ASSESSMENT_DATE,
        "inputs": {**{rel: sha256(ROOT / rel) for rel in INPUTS.values()}, **ledger_inputs},
        "outputs": {p.name: sha256(p) for p in sorted(OUT.glob("*")) if p.suffix in (".csv",) or p.name == "path-remaps.json"},
        "totals": totals,
    }
    with open(OUT / "catalog-manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(json.dumps(totals, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
