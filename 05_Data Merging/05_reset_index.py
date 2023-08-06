import pandas as pd

# 예제 데이터 생성
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
}

# DataFrame 생성
df = pd.DataFrame(data)

# inplace를 사용하여 인덱스 재설정 (원본 DataFrame이 변경됨)
df.reset_index(inplace=True)
print("인덱스 재설정 결과:")
print(df)
