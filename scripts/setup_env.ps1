# 一键创建 / 修复项目运行环境（Windows PowerShell）
# 用法：powershell -ExecutionPolicy Bypass -File scripts\setup_env.ps1
#
# 设计说明（踩坑记录）：
#   一次性 pip install 全部依赖会触发依赖解析回溯，实测会下载 pyspark(430MB)
#   等大量无关包，1.5GB 下载后仍失败。因此改为分批次 + --only-binary=:all:
#   + 关闭缓存 + 限制重试，稳定且快得多。

$ErrorActionPreference = 'Continue'
$IDX = 'https://mirrors.aliyun.com/pypi/simple/'
$PIP_COMMON = @('-m','pip','install','--no-cache-dir','--only-binary=:all:','--retries','2','--timeout','30','-i',$IDX)

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
Write-Host "项目根目录: $root" -ForegroundColor Cyan

# 1) 找 Python 3.11 / 3.12
$py = $null
foreach ($ver in @('3.12','3.11')) {
    try {
        $exe = & py "-$ver" -c "import sys; print(sys.executable)" 2>$null
        if ($LASTEXITCODE -eq 0 -and $exe) { $py = $exe.Trim(); break }
    } catch { }
}
if (-not $py) {
    Write-Host "[错误] 未找到 Python 3.11 或 3.12。下载: https://www.python.org/downloads/release/python-3119/" -ForegroundColor Red
    exit 1
}
Write-Host "使用解释器: $py" -ForegroundColor Green

# 2) 虚拟环境
$vpy = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $vpy)) {
    Write-Host "创建虚拟环境 .venv ..." -ForegroundColor Yellow
    & $py -m venv .venv
} else {
    Write-Host ".venv 已存在，跳过创建" -ForegroundColor Yellow
}
& $vpy --version

# 3) 分批次安装
$batches = @(
    @{ name='批次1 科学计算核心'; pkgs=@('numpy','pandas','scipy','matplotlib') },
    @{ name='批次2 可视化与经典机器学习'; pkgs=@('seaborn','scikit-learn') },
    @{ name='批次3 梯度提升与信号处理'; pkgs=@('xgboost','PyWavelets') },
    @{ name='批次4 Notebook 与表格'; pkgs=@('jupyter','ipykernel','openpyxl','tqdm') }
)
foreach ($b in $batches) {
    Write-Host "`n########## $($b.name) ##########" -ForegroundColor Cyan
    & $vpy @PIP_COMMON @($b.pkgs)
}

# 4) PyTorch (CPU)
Write-Host "`n########## 批次5 PyTorch (CPU) ##########" -ForegroundColor Cyan
& $vpy -m pip install --no-cache-dir --only-binary=:all: --retries 2 --timeout 30 torch --index-url https://download.pytorch.org/whl/cpu

# 5) 注册 Jupyter 内核
Write-Host "`n注册 Jupyter 内核 ..." -ForegroundColor Yellow
& $vpy -m ipykernel install --user --name phm --display-name "Python (phm)"

# 6) 自检
Write-Output ""
& $vpy scripts\check_env.py