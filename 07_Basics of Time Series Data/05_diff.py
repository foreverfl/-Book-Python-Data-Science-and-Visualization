"""
- diff(): 시계열 데이터에서 각 요소 간의 차이를 계산하는 기능을 제공함.
"""

import pandas as pd

# 예제 데이터 생성
data = {
    'Date': pd.date_range(start='2023-07-01', periods=5, freq='D'),
    'Value': [10, 20, 15, 30, 25]
}

df = pd.DataFrame(data)

# 'Value' 열의 차분 계산
df['Value_Diff'] = df['Value'].diff() #각 요소 간의 차이를 계산하는 기능을 제공

print(df)
