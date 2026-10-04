"""数据读取与基本检查。

支持：CWRU 轴承振动数据(.mat)、C-MAPSS 涡扇发动机退化数据(.txt)
原则：读函数只负责读，不清洗；原始数据永不修改。
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils import RAW_DIR

CMAPSS_COLUMNS = [
    "unit", "cycle",
    "op1", "op2", "op3",
    *[f"s{i}" for i in range(1, 22)],
]


def load_cmapss(subset: str = "FD001", split: str = "train") -> pd.DataFrame:
    """读取 C-MAPSS 的一个子集。subset: FD001-FD004；split: train/test。"""
    path = RAW_DIR / "cmapss" / f"{split}_{subset}.txt"
    if not path.exists():
        raise FileNotFoundError(f"未找到 {path}。请先按 data/README.md 下载 C-MAPSS 数据。")
    return pd.read_csv(path, sep=r"\s+", header=None, names=CMAPSS_COLUMNS)


def load_cmapss_rul(subset: str = "FD001") -> pd.Series:
    """读取测试集的真实 RUL 标签。"""
    path = RAW_DIR / "cmapss" / f"RUL_{subset}.txt"
    if not path.exists():
        raise FileNotFoundError(f"未找到 {path}。")
    return pd.read_csv(path, sep=r"\s+", header=None, names=["RUL"])["RUL"]


def load_cwru_mat(path):
    """读取一个 CWRU .mat 文件，返回 (信号数组, 键名)。优先取驱动端 DE 信号。"""
    from scipy.io import loadmat

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"未找到 {path}。请先按 data/README.md 下载 CWRU 数据。")
    mat = loadmat(path)
    keys = [k for k in mat if not k.startswith("__")]
    target = next((k for k in keys if k.endswith("_DE_time")), keys[0])
    return mat[target].ravel(), target


def describe_dataframe(df: pd.DataFrame, name: str = "data") -> None:
    """打印数据体检报告：形状、缺失、重复、统计量。"""
    print("=" * 60)
    print(f"[数据体检] {name}")
    print("=" * 60)
    print(f"形状      : {df.shape[0]} 行 x {df.shape[1]} 列")
    print(f"内存占用  : {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"重复行    : {df.duplicated().sum()}")
    missing = df.isna().sum()
    missing = missing[missing > 0]
    print(f"含缺失列  : {len(missing)}")
    if len(missing):
        print(missing.to_string())
    print("-" * 60)
    print(df.describe().T.to_string())
    print("=" * 60)


if __name__ == "__main__":
    try:
        describe_dataframe(load_cmapss("FD001", "train"), "C-MAPSS FD001 train")
    except FileNotFoundError as exc:
        print(f"[跳过] {exc}")