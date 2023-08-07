import pandas as pd

# 데이터 생성(Create)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 18, 47, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 새로운 행 추가
new_data = {
    'Name': ['Frank', 'Grace'],
    'Age': [29, 34],
    'City': ['Seattle', 'Boston']
}

new_df = pd.DataFrame(new_data)
df = df._append(new_df, ignore_index=True)  # 새로운 인덱스를 부여

print("\nDataFrame after adding new row:")
print(df)

# 새로운 열 추가
df['Gender'] = ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
print("\nDataFrame after adding new column:")
print(df)

# 데이터 수정(Update)
# 인덱스가 2인 행의 'Age' 값을 20으로 변경합니다.
df.at[2, 'Age'] = 20
print("\nDataFrame after updating data:")
print(df)

# 데이터 삭제(Delete)
# 행 삭제
df = df.drop(4)  # 인덱스가 4인 행을 삭제합니다.
print("\nDataFrame after deleting data:")
print(df)

# 열 삭제 (Delete)
df = df.drop('City', axis=1)  # 'City' 열을 삭제합니다.
print("\nDataFrame after deleting column:")
print(df)
