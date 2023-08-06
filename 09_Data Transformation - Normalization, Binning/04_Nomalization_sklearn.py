from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np

# 동일한 랜덤 결과를 위해 seed 값을 0으로 설정
np.random.seed(0)

# 1에서 100 사이의 정수를 랜덤하게 20개 생성하여 'value'라는 이름의 열로 가진 데이터프레임을 생성
df = pd.DataFrame({
    'value': np.random.randint(1, 100, 20)
})

# 1. 최대-최소 정규화
min_max_scaler = MinMaxScaler()
df['value_min_max'] = min_max_scaler.fit_transform(df[['value']])

# 2. Z-점수 정규화
standard_scaler = StandardScaler()
df['value_z_score'] = standard_scaler.fit_transform(df[['value']])

print(df)
