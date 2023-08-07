"""
- 데이터 병합: 각기 다른 두 개 이상의 Dataframe을 하나로 병합하여 결과 집합을 만들어 내는 것.
* Inner Join: Dataframe 간 조인 조건을 만족하는 행을 합치는 것.
1) One-to-One
2) One-to-Many
* Outer Join: 조건에 부합하지 않는 행까지 포함시켜 결합하는 방법. NaN 처리를 함.
* Left Join: 첫 번째 Dataframe을 기준으로 두 번째 Dataframe을 결합하는 방법.
* Right Join: 첫 번째 Dataframe을 기준으로 첫 번째 Dataframe을 결합하는 방법.
"""

import pandas as pd

# 데이터 생성
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28]
}

data2 = {
    'ID': [3, 4, 5, 6],
    'Department': ['HR', 'Finance', 'Marketing', 'IT']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


# 공통 열인 'ID'를 기준으로 Inner Join
inner_join_df = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Join(One-to-One) 결과:")
print(inner_join_df)


# 데이터프레임 df1과 df2의 'ID'를 기준으로 Inner Join
# One-to-Many 관계가 되도록 중복 데이터 추가
data2_modified = {
    'ID': [3, 4, 4, 5, 6, 6],
    'Department': ['HR', 'Finance', 'Finance', 'Marketing', 'IT', 'IT']
}

df2_modified = pd.DataFrame(data2_modified)
inner_join_many_df = pd.merge(df1, df2_modified, on='ID', how='inner')
print("\nInner Join(One-to-Many) 결과:")
print(inner_join_many_df)


# 데이터프레임 df1과 df2의 'ID'를 기준으로 Outer Join
outer_join_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join 결과:")
print(outer_join_df)


# 데이터프레임 df1을 기준으로 Left Join
left_join_df = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join 결과:")
print(left_join_df)


# 데이터프레임 df2을 기준으로 Right Join
right_join_df = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join 결과:")
print(right_join_df)
