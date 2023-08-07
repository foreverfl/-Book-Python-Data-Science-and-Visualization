# - 구간화(Binning): 연속형 데이터를 구간으로 구별하여 범주화 형태 변환
# * 특징
# 1) 지정 길이 기반 구간 정의: 사용자 기준으로 데이터 범위의 간격을 구분하여 관측치를 나눔
# 2) 분포 기간 구간 정의: 관측치가 각 구간 내 동일한 개수로 구분되도록 나눔

import pandas as pd
import numpy as np

# 랜덤한 숫자로 이루어진 데이터 프레임을 생성
np.random.seed(0)  # 동일한 랜덤 결과를 위해 seed 값을 0으로 설정
df = pd.DataFrame({
    'value': np.random.randint(1, 100, 20)  # 1에서 100 사이의 정수를 랜덤하게 20개 생성
})

print(df)

# 1. 지정 길이 기반 구간 정의
# 0부터 100까지 10의 간격으로 배열을 생성. '('는 해당 숫자를 포함하지 않음을, ']'는 해당 숫자를 포함함을 의미.
df['value_bin_cut'] = pd.cut(df['value'], bins=np.arange(0, 101, 10))

# 2. 분포 기반 구간 정의
# 'value' 열의 값들을 4분위수를 기준으로 구간을 나눔. qcut은 데이터가 극단적으로 치우쳐져 있다면 오류가 발생함.
df['value_bin_qcut'] = pd.qcut(df['value'], q=4)
print('\n', df)
