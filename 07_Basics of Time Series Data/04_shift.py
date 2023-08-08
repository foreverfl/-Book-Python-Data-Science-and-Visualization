"""
- shift(): 함수는 데이터를 특정 방향으로 이동시키는 기능을 제공.
"""

import pandas as pd


# 예제 데이터 생성
data = {
    'Date': pd.date_range(start='2023-07-01', periods=5, freq='D'),
    'Value': [10, 20, 15, 30, 25]
}

df = pd.DataFrame(data)

df['Shifted_Value'] = df['Value'].shift(-1) # 'Value' 열을 한 칸씩 위로 이동

print(df)
