"""特征提取：时域 / 频域 / 时频域。本模块是对接信号处理方向的核心。"""
from __future__ import annotations

import numpy as np
from scipy import stats


def time_domain_features(x: np.ndarray) -> dict:
    """时域统计特征：均值/标准差/RMS/峰值/峰峰值/偏度/峭度/峰值因子/波形因子/脉冲因子。"""
    x = np.asarray(x, dtype=float).ravel()
    if x.size == 0:
        raise ValueError("输入信号为空")

    abs_x = np.abs(x)
    rms = float(np.sqrt(np.mean(x**2)))
    peak = float(abs_x.max())
    mean_abs = float(abs_x.mean())
    eps = 1e-12

    return {
        "mean": float(x.mean()),
        "std": float(x.std()),
        "rms": rms,
        "peak": peak,
        "p2p": float(x.max() - x.min()),
        "skewness": float(stats.skew(x)),
        "kurtosis": float(stats.kurtosis(x)),
        "crest_factor": peak / (rms + eps),
        "shape_factor": rms / (mean_abs + eps),
        "impulse_factor": peak / (mean_abs + eps),
    }


def freq_domain_features(x: np.ndarray, fs: float) -> dict:
    """频域特征：重心频率 FC、均方频率 MSF、频率方差 VF、频谱熵。"""
    x = np.asarray(x, dtype=float).ravel()
    n = x.size
    spectrum = np.abs(np.fft.rfft(x)) / n
    freqs = np.fft.rfftfreq(n, d=1.0 / fs)
    power = spectrum**2
    total_power = power.sum() + 1e-12

    fc = float((freqs * power).sum() / total_power)
    msf = float((freqs**2 * power).sum() / total_power)
    vf = float(((freqs - fc) ** 2 * power).sum() / total_power)
    prob = power / total_power
    entropy = float(-(prob * np.log(prob + 1e-12)).sum())

    return {"FC": fc, "MSF": msf, "VF": vf, "spectral_entropy": entropy}


def extract_features(x: np.ndarray, fs: float) -> dict:
    """时域 + 频域特征一起算，返回扁平字典（一行特征向量）。"""
    feats = time_domain_features(x)
    feats.update(freq_domain_features(x, fs))
    return feats


def bandpass_filter(x: np.ndarray, fs: float, low: float, high: float, order: int = 4):
    """巴特沃斯带通滤波（零相位）。

    TODO(第 3 周): 用 scipy.signal.butter + sosfiltfilt 实现
    """
    raise NotImplementedError("第 3 周任务：实现带通滤波")


def envelope_spectrum(x: np.ndarray, fs: float, band=None):
    """包络谱：希尔伯特变换取包络 -> FFT。轴承故障诊断核心工具。

    TODO(第 3 周):
        1. 若给定 band，先带通滤波
        2. scipy.signal.hilbert 取解析信号，求模得到包络
        3. 包络去均值后做 FFT
        4. 返回 (freqs, amplitude)
    """
    raise NotImplementedError("第 3 周任务：实现包络谱")