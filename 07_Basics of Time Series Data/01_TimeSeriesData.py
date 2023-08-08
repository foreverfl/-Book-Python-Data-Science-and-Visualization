"""
- 시계열 데이터: 순차적인 시간의 흐름으로 기록된 관측치의 집합
* 시간이 순차적인 경우에 사용.
* 고정된 시간 구간의 관측치: 시간 구간이 일정해야함.
* DatetimeIndex라는 자료형을 사용함.
"""

import pandas as pd


# 예제 데이터 생성
dates = pd.date_range(start='2023-07-01', periods=5, freq='D')
values = [10, 20, 15, 30, 25]

# DatetimeIndex 생성
datetime_index = pd.DatetimeIndex(dates)

# DataFrame 생성
df = pd.DataFrame({'Value': values}, index=datetime_index)

print("DataFrame:")
print(df)
