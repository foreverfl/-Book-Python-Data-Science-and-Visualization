"""
- ACF (Autocorrelation Function)
* ACF는 시계열 데이터에서 한 시점의 값과 다른 시점의 값 사이의 상관 관계를 측정.
* 특히 ACF는 특정 시차(lag)에 대해 직접적인 상관 관계를 나타냄.
* 이를 통해 시계열 데이터의 패턴, 주기성 및 추세를 파악할 수 있음.
- PACF (Partial Autocorrelation Function)
* PACF는 다른 시차의 영향을 배제하고 두 시점의 값 사이의 상관 관계를 측정.
* 예를 들어, PACF의 2차 시차는 1차 시차의 영향을 배제하고 2차 시차만의 상관 관계를 나타냄.
* ARIMA와 같은 시계열 모델의 파라미터를 결정하는 데 도움을 줌.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import yfinance as yf

# QQQ 주식 데이터 다운로드
data = yf.download('QQQ', start='2000-01-01')

# 종가 데이터 선택
close = data['Close']

# ACF 및 PACF 그래프 그리기
fig, ax = plt.subplots(1, 2, figsize=(16, 4))

# ACF 그래프
# lags=40은 40차 시차까지의 자기상관을 계산하고 그래프에 나타내라는 의미
plot_acf(close, lags=40, ax=ax[0])
ax[0].set_title("Autocorrelation Function (ACF)")

# PACF 그래프
# lags=40은 40차 시차까지의 부분 자기상관을 계산하고 그래프에 나타내라는 의미
plot_pacf(close, lags=40, ax=ax[1])
ax[1].set_title("Partial Autocorrelation Function (PACF)")

plt.tight_layout()
plt.show()
