import pandas as pd

# 샘플 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 18, 47, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
}

df = pd.DataFrame(data)

# 원본 DataFrame 출력
print("원본 DataFrame:")
print(df)
print(df.index.values)

df = df.set_index('Name', drop=True)  # 'Name' 열을 새로운 인덱스로 설정하고 기존 인덱스는 유지

print("\n인덱스를 바꾼 DataFrame:")  # 변경된 DataFrame 출력

print(df)
print(df.index.values)
