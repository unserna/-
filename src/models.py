"""模型定义与训练封装。按学习顺序实现：经典 ML -> 深度学习。"""
from __future__ import annotations


def evaluate_classification(y_true, y_pred, labels=None) -> dict:
    """分类评价：准确率、宏平均 F1、混淆矩阵。

    TODO(第 3 阶段): 用 sklearn.metrics 实现
    """
    raise NotImplementedError("第 3 阶段任务")


def evaluate_rul(y_true, y_pred) -> dict:
    """剩余寿命预测评价：RMSE、MAE、PHM08 Score。

    TODO(第 4 阶段)
    """
    raise NotImplementedError("第 4 阶段任务")


class CNN1D:
    """一维卷积网络占位说明。

    TODO(第 4 阶段): Conv1d -> BatchNorm1d -> ReLU -> MaxPool1d x3 -> Linear
    """


class LSTMRUL:
    """LSTM 剩余寿命预测模型占位说明。

    TODO(第 4 阶段): 输入 (batch, 时间步, 特征数)，输出单个 RUL 值
    """