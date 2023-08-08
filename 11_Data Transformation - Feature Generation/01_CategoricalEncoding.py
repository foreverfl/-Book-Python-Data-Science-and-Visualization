"""
- 범주 인코딩: 크게 Nominal(순서가 없는)과 Ordinal(순서가 있는)으로 나뉘는 범주형 변수. 숫자가 아닌 범주 변수 값을 숫자로 표현.
* One-hot Encoding: Nominal한 변수를 처리. K개의 범주를 지닌 범주형 변수를 K개의 변수로 변환.
"""

import pandas as pd

# 범주형 변수를 가진 데이터프레임을 생성
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue']
})

df_encoded = pd.get_dummies(df, columns=['color']) # One-hot Encoding을 수행
print(df_encoded)
