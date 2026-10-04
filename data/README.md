# 数据目录说明

**本目录下的所有真实数据文件都不会被 Git 追踪。**

## 目录约定

| 目录 | 放什么 | 可否重新生成 |
|---|---|---|
| raw/ | 原始下载的数据，只读，绝不修改 | 可重新下载 |
| interim/ | 清洗后、未做特征的中间产物 | 是（由代码生成） |
| processed/ | 可直接建模的特征矩阵与标签 | 是（由代码生成） |

科研铁律：**原始数据永远不动手改**。所有清洗写成代码，从 raw 重新生成 interim/processed。

## 准备下载的数据集

### 1. CWRU 轴承数据（第 3-4 周用，先下这个）
- Case Western Reserve University Bearing Data Center
- 内容：驱动端/风扇端轴承振动信号，正常 + 内圈/外圈/滚动体故障
- 获取：搜索 "CWRU Bearing Data Center"，官网下载 .mat
- 建议先下 12kHz 驱动端数据：Normal_0.mat / IR007_0.mat / OR007@6_0.mat / B007_0.mat
- 放到 data/raw/cwru/

### 2. C-MAPSS 涡扇发动机退化数据（第 6 周后用）
- NASA C-MAPSS Turbofan Engine Degradation Simulation，FD001-FD004
- 21 个传感器 + 3 个操作设置的时序数据
- 获取：NASA PCoE Data Repository / Kaggle 搜 C-MAPSS / IEEE DataPort
- 放到 data/raw/cmapss/，文件名通常为 train_FD001.txt / test_FD001.txt / RUL_FD001.txt

### 3. N-CMAPSS（进阶）
- 带飞行剖面的新版仿真数据，更接近真实工况
- NASA PCoE；GitHub 上有下载脚本（搜 n-cmapss_dl）

## 严禁事项
- 联培企业（中国航发沈阳发动机研究所）的任何真实数据、型号参数、试验记录，
  一律不得放入本仓库、不得上传网盘 / GitHub / 任何公开平台。