"""
- 대체하기: 편향(Bias) 발생 가능. 정보의 손실을 방지하나 변수 특성(평균, 상관관계)에 영향 발생.
* 일정 값 대체
* 선형 값 대체
1) linear(기본값): 선형 보간을 수행하여 결측값을 주변 두 값의 선형 비율에 따라 추정.
2) time: 시계열 데이터에서 사용할 때, 시간에 따른 선형 보간을 수행.
3) polynomial: 다항식 보간을 수행.
4) spline: 스플라인(spline) 보간을 수행.
"""

import pandas as pd

# 예제 데이터 생성
data = {
    'Date': ['2023-07-01', '2023-07-02', None, '2023-07-04', '2023-07-05'],
    'Value': [10, 20, None, 30, None]
}

df = pd.DataFrame(data)

# 일정 값(예: 0)으로 결측값 대체
df_filled_constant = df.fillna(0)

print("\n일정 값 대체 결과:")
print(df_filled_constant)


# 예제 데이터 생성
data = {
    'Date': ['2023-07-01', '2023-07-02', None, '2023-07-04', '2023-07-05'],
    'Value': [10, 20, None, 30, None]
}

df = pd.DataFrame(data)

# 선형 값으로 결측값 대체
df_filled_linear = df.interpolate()  # 결측값을 주변 값들을 기반으로 일련의 방법으로 대체
print("\n선형 값 대체 결과:")
print(df_filled_linear)
