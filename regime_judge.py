# 市场状态判断框架
import numpy as np

def market_regime_score(df, window_short=20, window_long=40):
    ma_short = df['Close'].rolling(window_short).mean()
    ma_long = df['Close'].rolling(window_long).mean()
    regime = (ma_short - ma_long) / ma_long
    return np.tanh(regime * 5)