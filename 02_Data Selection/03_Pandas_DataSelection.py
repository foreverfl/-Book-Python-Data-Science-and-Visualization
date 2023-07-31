import pandas as pd

# 샘플 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 18, 47, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
}

# DataFrame 생성
df = pd.DataFrame(data)

# DataFrame 출력
print(df)

# 1. loc: 인덱스를 기준으로 해당하는 행의 데이터를 선택
# 인덱스 2의 데이터를 선택하여 추출
row_data = df.loc[2]
print(row_data)

# 2. iloc: 행과 열의 위치를 기준으로 해당하는 데이터를 선택
# 첫 번째 행의 첫 번째 열 데이터를 선택하여 추출
cell_data = df.iloc[0, 0]
print(cell_data)
