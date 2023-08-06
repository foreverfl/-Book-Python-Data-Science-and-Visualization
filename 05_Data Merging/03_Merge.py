import pandas as pd

# Merge의 특징
# - 열을 기준으로 함.
# - Pandas의 함수로 사용함.
# - 기본적으로 inner join. how 파라미터를 통해 변경 가능.


# 예제 데이터 생성
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28]
}

data2 = {
    'ID': [3, 4, 5, 6],
    'Score': [78, 95, 88, 90],
}

# DataFrame 생성
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# merge 수행
result_merge = pd.merge(df1, df2, on='ID', how='inner')
print("Merge 결과:")
print(result_merge)
