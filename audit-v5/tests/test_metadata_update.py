import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from utils import update_metadata


def test_insert_missing_metadata():
    content = "## 業務簡介\n\n公司敘述。\n"
    out = update_metadata(content, "1,234", "2,345", "Technology", "Electronic Components")
    assert "**板塊:** Technology" in out
    assert "**產業:** Electronic Components" in out
    assert "**市值:** 1,234 百萬台幣" in out
    assert "**企業價值:** 2,345 百萬台幣" in out


def test_update_existing_metadata():
    content = "## 業務簡介\n**板塊:** Old\n**市值:** 1 百萬台幣\n"
    out = update_metadata(content, "9,999", None, "Technology", None)
    assert "**板塊:** Technology" in out
    assert "**市值:** 9,999 百萬台幣" in out


if __name__ == "__main__":
    test_insert_missing_metadata()
    test_update_existing_metadata()
    print("metadata tests passed")


def test_collapse_duplicate_business_heading():
    content = (
        "## 業務簡介\n"
        "**板塊:** Basic Materials\n"
        "**產業:** Building Materials\n"
        "**市值:** 1,234 百萬台幣\n"
        "**企業價值:** 2,345 百萬台幣\n\n"
        "## 業務簡介\n"
        "公司敘述。\n"
    )
    out = update_metadata(content, "1,234", "2,345", "Basic Materials", "Building Materials")
    assert out.count("## 業務簡介") == 1
    assert "公司敘述。" in out
