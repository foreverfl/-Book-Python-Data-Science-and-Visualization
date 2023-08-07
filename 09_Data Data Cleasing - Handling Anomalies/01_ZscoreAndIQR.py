import pandas as pd
import numpy as np

# 예제 데이터 생성
data = {
    'Value': [10, 15, 12, 20, 100, 11, 9, 8, 25, 30]
}

df = pd.DataFrame(data)

# 1. Z-score
# * 데이터가 평균에서 얼마나 떨어져 있는지를 표준편차의 단위로 나타내는 값.
# * 평균으로부터 얼마나 떨어져 있는지를 알 수 있으므로 데이터가 평균으로부터 얼마나 표준편차만큼 떨어져 있는지를 측정하는 표준화된 값으로 사용됨.
# * Z = (X - μ) / σ
# 1) X: 개별 데이터 포인트 값.
# 2) μ: 데이터의 평균.
# 3) σ: 데이터의 표준편차.

# Z-score를 이용한 이상치 처리
z_scores = np.abs((df - df.mean()) / df.std())
threshold = 3  # 임계값 설정(일반적으로 2~3)
outliers_z_score = df[z_scores > threshold]

print("Z-score를 이용한 이상치 처리:")
print(outliers_z_score)

# 2. IQR(Interquartile Range)
# * 데이터의 중간 50% 범위를 나타내는 값.
# * 데이터의 중간 50% 범위를 간단하게 측정하는 방법.
# * IQR = Q3 - Q1
# 1) Q3: 75% 지점
# 2) Q1: 25% 지점
Q1 = df.quantile(0.25)  # 데이터의 분위수(quantile)를 계산하는 함수
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
threshold_lower = Q1 - 1.5 * IQR
threshold_upper = Q3 + 1.5 * IQR
outliers_iqr = df[(df < threshold_lower) | (df > threshold_upper)]

print("\nIQR을 이용한 이상치 처리:")
print(outliers_iqr)
