"""
- 모델
* 자기회귀 모델(AR): 시계열의 미래 값이 과거 값에 기반한다는 모델. 이전 값의 영향을 받음.
1) 기본 아이디어: 과거의 데이터 포인트들이 미래의 데이터 포인트에 영향을 줌.
2) 예시: "어제 비가 왔다면, 오늘도 비가 올 확률이 높다"라는 개념.
* 이동평균 모델(MA): 전체적인 편향성을 다루는 모델. 설명변수가 최근 오차항으로만 구성되어 있음. 이전 시점의 예측 오차에 가중치를 두어 미래의 값을 예측.
1) 기본 아이디어: 현재의 데이터 포인트는 최근의 오차(또는 '충격')들에 의해 영향을 받음.
2) 예시: "어제의 날씨 예측이 얼마나 틀렸는지"가 "오늘의 날씨가 어떨지"에 영향을 줌
* ARIMA 모델: AR과 MA를 고려하고, 누적(Integretion)으로 추세를 고려한 모델. 자기회귀 누적 이동평균 모델.
1) 기본 아이디어: AR과 MA 모델의 아이디어를 결합하고, 또한 누적된 데이터(또는 추세)를 포함하여 더 복잡한 시계열 패턴을 모델링.
2) 예시: "어제 비가 왔고, 어제의 날씨 예측이 얼마나 틀렸는지, 그리고 최근 몇 년 동안의 비의 추세"가 "오늘의 날씨가 어떨지"에 영향을 준줌.

- 정상성: 정상성을 나타내는 시계열은 관측치가 시관과 무관하여야 함.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 임의의 시계열 데이터 생성
np.random.seed(42)
n_points = 100
x = np.linspace(0, 10, n_points)
y = 3 * np.sin(0.5 * x) + 1.5 * np.random.randn(n_points)

# 데이터프레임으로 변환
df = pd.DataFrame({'value': y})

# ARIMA 모델 설정 및 학습
# 여기서는 (1,1,1) 파라미터를 사용 (AR차수 1, 차분 1, MA차수 1)
# 1(첫 번째 숫자): AR의 차수. 1차 자기회귀다.
# 1(두 번째 숫자): 차분의 차수. 여기서는 1차 차분을 사용하여 데이터를 정상 상태로 만듬.
# 1(세 번째 숫자): MA의 차수. 1차 이동평균.
model = ARIMA(df['value'], order=(1, 1, 1))
model_fit = model.fit()

# 예측
forecast = model_fit.forecast(steps=20)

# 결과 시각화
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value'], label='Actual')
plt.plot(np.arange(n_points, n_points + 20),
         forecast, label='Forecast', color='red')
plt.legend()
plt.title('ARIMA Model 예제')
plt.show()
