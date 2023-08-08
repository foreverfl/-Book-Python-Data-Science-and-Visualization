"""
- 정규화: 데이터 탐색 및 기계학습 적용을 위한 연속형 변수 변환.
* 최대-최소 정규화
1) 데이터 구간을 0에서 1사이로 변환. 데이터의 위치 파악.
2) 이상치에 민감할 수 있는 단점.
3) X(normalized) = (X - X(min)) / (X(max) - X(min))
* Z-점수 정규화(표준화)
1) 0을 중심으로 양쪽으로 데이터 분포시킴.
2) 특정 데이터가 평균화 얼마나 떨어져 있는지 파악.
3) Z = (X - μ(평균)) / a(표준편차)
"""

import pandas as pd
import numpy as np


np.random.seed(0) # 동일한 랜덤 결과를 위해 seed 값을 0으로 설정
df = pd.DataFrame({
    'value': np.random.randint(1, 100, 20) # 1에서 100 사이의 정수를 랜덤하게 20개 생성하여 'value'라는 이름의 열로 가진 데이터프레임을 생성
})

# 최대-최소 정규화
df['value_min_max'] = (df['value'] - df['value'].min()) / \
    (df['value'].max() - df['value'].min())

# Z-점수 정규화
df['value_z_score'] = (df['value'] - df['value'].mean()) / df['value'].std()

print(df)
