import pandas as pd

# - 제거하기: 데이터 손실 발생.
# 1. Likewise deletion: 결측치가 존재하는 행 삭제
# 예제 데이터 생성
data = {
    'Date': ['2023-07-01', '2023-07-02', None, '2023-07-04', '2023-07-05'],
    'Value': [10, 20, None, 30, None]
}

df = pd.DataFrame(data)

# 결측값이 있는 행을 제거
cleaned_df = df.dropna()

print("결측치 제거 결과:")
print(cleaned_df)

# 2. Pairwise deletion: 모든 변수가 결측치로만 존재하는 행 삭제
# 예제 데이터 생성
data = {
    'Date': [None, None, None, None, None],
    'Value': [None, None, None, None, None]
}

df = pd.DataFrame(data)

# 모든 변수가 결측치로만 존재하는 행 삭제 (Pairwise deletion)
cleaned_df = df.dropna(how='all')

print("\nPairwise deletion 결과:")
print(cleaned_df)
