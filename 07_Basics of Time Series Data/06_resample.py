"""
- 다운샘플링: 원래의 데이터가 그룹으로 묶여 대표값 필요. 데이터의 양이 감소.
- 업샘플링: 실제로 존재하지 않는 데이터를 만듦. 데이터의 값이 증가.
* Forward filling: 처음 데이터를 기준으로 결측치를 보관함.
1) 시계열 데이터에서 값이 연속적으로 유지되어야 할 때.
2) 센서로부터의 읽기 누락 등이 있어 직전 데이터를 현재 값으로 사용해야 할 때.
* Backward filling: 마지막 데이터를 기준으로 결측치를 보관함.
1) 미래의 데이터가 과거의 누락된 값에 더 영향을 미칠 것으로 예상되는 상황.
2) 특정 이벤트 후의 데이터가 더 중요한 정보를 제공할 수 있을 때.
"""


import pandas as pd

# 다운샘플링
# 예제 데이터 생성(1초 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=60, freq='S'),
    'Value': range(60)  # 0부터 59까지의 숫자를 나열
}

df = pd.DataFrame(data) # DataFrame 생성
df.set_index('Timestamp', inplace=True) # Timestamp 열을 DatetimeIndex로 변환
downsampled_df = df.resample('10S').sum() # 10초 단위로 다운샘플링

print("다운샘플링 결과:")
print(downsampled_df)


# 업샘플링(Forward Filling)
# 예제 데이터 생성 (1분 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=5, freq='T'),
    'Value': [10, 20, 15, 30, 25]
}

df = pd.DataFrame(data) # DataFrame 생성
df.set_index('Timestamp', inplace=True) # Timestamp 열을 DatetimeIndex로 변환
upsampled_df = df.resample('15S').asfreq()  # 15초 단위로 업샘플링. 시계열 데이터의 주기를 변경
forward_filled_df = upsampled_df.fillna(method='ffill')  # 결측값(NaN)을 지정된 값으로 채움
print("\n업샘플링 결과(Forward Filling) 결과:")
print(forward_filled_df)

# 업샘플링(Backward Filling)
# 예제 데이터 생성 (1분 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=5, freq='T'),
    'Value': [10, 20, 15, 30, 25]
}

df = pd.DataFrame(data) # DataFrame 생성
df.set_index('Timestamp', inplace=True) # Timestamp 열을 DatetimeIndex로 변환
upsampled_df = df.resample('15S').asfreq() # 15초 단위로 업샘플링
backward_filled_df = upsampled_df.fillna(method='bfill') # 다운샘플링(Backward Filling)
print("\n업샘플링 결과(Backward Filling) 결과:")
print(backward_filled_df)
