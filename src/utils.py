"""通用工具：路径管理、绘图风格、随机种子。"""
from __future__ import annotations

import random
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
MODELS_DIR = RESULTS_DIR / "models"
REPORTS_DIR = RESULTS_DIR / "reports"
DOCS_DIR = PROJECT_ROOT / "docs"

for _d in (RAW_DIR, INTERIM_DIR, PROCESSED_DIR, FIGURES_DIR, MODELS_DIR, REPORTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)


def set_seed(seed: int = 42) -> None:
    """固定随机种子，保证实验可复现。"""
    random.seed(seed)
    np.random.seed(seed)


def setup_chinese_font() -> None:
    """配置 matplotlib 中文字体，避免图中文字变成方框。"""
    import matplotlib

    matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
    matplotlib.rcParams["axes.unicode_minus"] = False


def save_figure(fig, filename: str, dpi: int = 300) -> Path:
    """把图保存到 results/figures/ 下，返回文件路径。"""
    out = FIGURES_DIR / filename
    fig.savefig(out, dpi=dpi, bbox_inches="tight")
    print(f"[保存] {out}")
    return out