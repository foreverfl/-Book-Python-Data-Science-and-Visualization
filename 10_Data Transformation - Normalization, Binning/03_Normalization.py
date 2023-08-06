# - 정규화: 데이터 탐색 및 기계학습 적용을 위한 연속형 변수 변환.
# * 특징
# 1) 최대-최소 정규화: 데이터 구간을 0에서 1사이로 변환. 데이터의 위치 파악.
# 2) Z-점수 정규화(표준화): 0을 중심으로 양쪾으로 데이터 분포시킴. 특정 데이터가 평균화 얼마나 떨어져 있는지 파악.

import pandas as pd
import numpy as np

# 동일한 랜덤 결과를 위해 seed 값을 0으로 설정합니다.
np.random.seed(0)

# 1에서 100 사이의 정수를 랜덤하게 20개 생성하여 'value'라는 이름의 열로 가진 데이터프레임을 생성합니다.
df = pd.DataFrame({
    'value': np.random.randint(1, 100, 20)
})

# 1. 최대-최소 정규화
df['value_min_max'] = (df['value'] - df['value'].min()) / \
    (df['value'].max() - df['value'].min())

# 2. Z-점수 정규화
df['value_z_score'] = (df['value'] - df['value'].mean()) / df['value'].std()

print(df)
