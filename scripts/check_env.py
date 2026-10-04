"""环境自检脚本。用法： .\\.venv\\Scripts\\python.exe scripts\\check_env.py"""
from __future__ import annotations

import platform
import sys


def main() -> int:
    print("=" * 56)
    print("engine-phm-study 环境自检")
    print("=" * 56)
    print(f"Python 版本 : {sys.version.split()[0]}")
    print(f"解释器路径 : {sys.executable}")
    print(f"操作系统   : {platform.system()} {platform.release()}")
    print("-" * 56)

    if sys.version_info[:2] >= (3, 14):
        print("[!] 警告：当前用的是 Python 3.14+，PyTorch 尚不支持。请改用项目内 .venv（3.11）。")

    packages = [
        ("numpy", "NumPy"), ("pandas", "pandas"), ("scipy", "SciPy"),
        ("matplotlib", "matplotlib"), ("seaborn", "seaborn"),
        ("sklearn", "scikit-learn"), ("xgboost", "xgboost"),
        ("pywt", "PyWavelets"), ("torch", "PyTorch"),
    ]

    missing: list[str] = []
    for module_name, display_name in packages:
        try:
            module = __import__(module_name)
            print(f"[OK]   {display_name:<14} {getattr(module, '__version__', 'unknown')}")
        except ImportError:
            print(f"[MISS] {display_name:<14} 未安装")
            missing.append(display_name)

    if "PyTorch" not in missing:
        import torch
        print(f"       torch.cuda.available = {torch.cuda.is_available()}")

    print("-" * 56)
    if missing:
        print(f"[结果] 缺少 {len(missing)} 个依赖：{', '.join(missing)}")
        return 1
    print("[结果] 全部依赖就绪，可以开始干活。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())