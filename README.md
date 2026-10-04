# engine-phm-study

> 航空发动机综合监控与故障诊断 —— 数据驱动方法学习与实践
> 面向课题「基于数据驱动模型的发动机综合监控与故障诊断软件」的公开数据集实验代码库。

## 这个仓库是干什么的

把「信号处理 → 特征工程 → 数据驱动模型 → 诊断/监控软件」这条链路完整走通一遍，
并用公开数据集积累可复用的代码与实验流程。

背景：沈阳工业大学卓工学院推免直博（仪器科学与技术），校内导师刘斌，
联培单位中国航发沈阳发动机研究所。

**本仓库只使用公开数据集。企业真实数据、型号参数、试验记录一律不入库。**

## 学习路线

| 阶段 | 内容 | 状态 |
|---|---|---|
| 0 | 工程环境：Git / venv / 项目骨架 | 进行中 |
| 1 | NumPy / pandas / matplotlib 数据探索 | 未开始 |
| 2 | 信号处理：时域指标 / FFT / 滤波 / 包络分析（CWRU） | 未开始 |
| 3 | 经典机器学习：特征 + 随机森林 / XGBoost | 未开始 |
| 4 | 深度学习：1D-CNN / LSTM（C-MAPSS 剩余寿命预测） | 未开始 |
| 5 | 监控诊断软件原型：Streamlit / FastAPI | 未开始 |

## 目录结构

    engine-phm-study/
    ├── data/          raw(原始,只读) / interim(中间) / processed(建模用)
    ├── notebooks/     探索性分析
    ├── src/           data_loader.py / features.py / models.py / utils.py
    ├── scripts/       setup_env.ps1 / check_env.py
    ├── results/       figures / models / reports
    ├── docs/          笔记与学习记录
    ├── requirements.txt
    └── .gitignore

## 环境搭建（Windows）

要求：**Python 3.11 或 3.12**。PyTorch 不支持系统默认的 3.14。

一键安装：

    powershell -ExecutionPolicy Bypass -File scripts\setup_env.ps1

手动安装：

    py -3.11 -m venv .venv
    .\.venv\Scripts\python.exe -m pip install --no-cache-dir --only-binary=:all: -i https://mirrors.aliyun.com/pypi/simple/ numpy pandas scipy matplotlib seaborn scikit-learn xgboost PyWavelets jupyter ipykernel tqdm
    .\.venv\Scripts\python.exe scripts\check_env.py

警告：不要一次性 `pip install -r requirements.txt`。已实测会触发 pip 依赖解析回溯，
下载 pyspark(430MB) 等无关大包，1.5GB 下完仍装不上。请用 setup_env.ps1 的分批次方式。

### VS Code

1. 打开本文件夹
2. Ctrl+Shift+P -> Python: Select Interpreter -> 选 .venv\Scripts\python.exe
3. 新终端确认提示符前有 (.venv)

## 数据准备

详见 data/README.md。

## 复现实验

| 实验 | 命令 | 输出 |
|---|---|---|
| 环境自检 | python scripts\check_env.py | 控制台 |
| CWRU 数据探索 | 打开 notebooks/01_cwru_explore.ipynb | 图表 + 特征表 |

## 参考文献

1. 航空发动机健康管理技术综述. 航空发动机, 2025.
2. 军用航空发动机气路故障诊断技术进展. 航空发动机, 2024.
3. Saxena A, et al. Damage propagation modeling for aircraft engine run-to-failure simulation. PHM 2008.
4. Smith W A, Randall R B. Rolling element bearing diagnostics using the CWRU data: A benchmark study. MSSP, 2015.