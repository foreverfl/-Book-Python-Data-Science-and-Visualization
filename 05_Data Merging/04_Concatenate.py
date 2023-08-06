import pandas as pd
# Concatenate: 연결은 공유하는 Key 값을 사용하지 않고, 데이터를 기존 DataFrame 아래(또는 우측)에 붙여 연결함.

# 1. 아래에 붙임
# 예제 데이터 생성
data1 = {
    'ID': [1, 2],
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}

data2 = {
    'ID': [3, 4],
    'Name': ['Charlie', 'David'],
    'Age': [22, 28]
}

# DataFrame 생성
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 아래로 연결 (행 방향으로 연결)
concatenated_df = pd.concat([df1, df2])
print("아래로 연결 결과:")
print(concatenated_df)

# 2. 우측에 붙임
# 예제 데이터 생성
data1 = {
    'ID': [1, 2],
    'Name': ['Alice', 'Bob'],
}

data2 = {
    'Age': [25, 30],
    'Department': ['HR', 'Finance'],
}

# DataFrame 생성
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 우측으로 연결 (열 방향으로 연결)
concatenated_df = pd.concat([df1, df2], axis=1)
print("\n우측으로 연결 결과:")
print(concatenated_df)
