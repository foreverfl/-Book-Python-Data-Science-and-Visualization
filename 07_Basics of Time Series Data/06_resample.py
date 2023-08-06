import pandas as pd

# - Resample
# 1. 다운샘플링: 원래의 데이터가 그룹으로 묶여 대표값 필요. 데이터의 양이 감소.
# 예제 데이터 생성 (1초 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=60, freq='S'),
    'Value': range(60)  # 0부터 59까지의 숫자를 나열함
}

# DataFrame 생성
df = pd.DataFrame(data)

# Timestamp 열을 DatetimeIndex로 변환
df.set_index('Timestamp', inplace=True)

# 10초 단위로 다운샘플링
downsampled_df = df.resample('10S').sum()

print("\n다운샘플링 결과:")
print(downsampled_df)

print("\n업샘플링 결과:")
# 2. 업샘플링: 실제로 존재하지 않는 데이터를 만듦. 데이터의 값이 증가.
# 1) Fordward filling: 처음 데이터를 기준으로 결측치를 보관함.
# 예제 데이터 생성 (1분 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=5, freq='T'),
    'Value': [10, 20, 15, 30, 25]
}

# DataFrame 생성
df = pd.DataFrame(data)

# Timestamp 열을 DatetimeIndex로 변환
df.set_index('Timestamp', inplace=True)

# 15초 단위로 업샘플링
upsampled_df = df.resample('15S').asfreq()  # 시계열 데이터의 주기를 변경

# Forward Filling (ffill)
forward_filled_df = upsampled_df.fillna(method='ffill')  # 결측값(NaN)을 지정된 값으로 채움

print("\nForward Filling 결과:")
print(forward_filled_df)

# 2) Backward filling: 마지막 데이터를 기준으로 결측치를 보관함.
# 예제 데이터 생성 (1분 단위 데이터)
data = {
    'Timestamp': pd.date_range(start='2023-07-31 00:00:00', periods=5, freq='T'),
    'Value': [10, 20, 15, 30, 25]
}

# DataFrame 생성
df = pd.DataFrame(data)

# Timestamp 열을 DatetimeIndex로 변환
df.set_index('Timestamp', inplace=True)

# 15초 단위로 업샘플링
upsampled_df = df.resample('15S').asfreq()

# Backward Filling (bfill)
backward_filled_df = upsampled_df.fillna(method='bfill')

print("\nBackward Filling 결과:")
print(backward_filled_df)
