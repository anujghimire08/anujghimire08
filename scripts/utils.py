from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"
CONFIG = ROOT / "scripts" / "config.json"


def load_config():
    with open(CONFIG, "r", encoding="utf-8") as f:
        return json.load(f)


def ensure_assets():
    ASSETS.mkdir(exist_ok=True)