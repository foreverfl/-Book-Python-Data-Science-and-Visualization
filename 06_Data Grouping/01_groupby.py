"""
- groupby: 특정 열, 열의 리스트 또는 행 인덱스를 기준으로 그룹화를 진행함.
* count: 각 그룹의 각 열의 누락되지 않은 값의 개수를 세어줌.
* sum: 각 그룹의 각 열의 합계를 구해줌.
* mean: 각 그룹의 각 열의 평균값을 구해줌.
* median: 각 그룹의 각 열의 중앙값을 구해줌.
* min: 각 그룹의 각 열의 최솟값을 구해줌.
* max: 각 그룹의 각 열의 최댓값을 구해줌.
* var: 각 그룹의 각 열의 분산을 구해줌.
* std: 각 그룹의 각 열의 표준편차를 구해줌.
* first: 각 그룹의 각 열의 첫 번째 값 (누락되지 않은)을 가져옴.
* last: 각 그룹의 각 열의 마지막 값 (누락되지 않은)을 가져옴.
* describe: 각 그룹의 각 열의 기술통계량을 계산하여 반환함. (평균, 표준편차, 최소값, 최대값 등)
* aggregate 또는 agg: 사용자가 지정한 하나 이상의 연산을 각 그룹의 각 열에 적용함. 집계 함수의 리스트나 딕셔너리를 전달할 수 있음.
* apply: 각 그룹의 각 열에 함수를 적용하고, 결과를 합쳐줌. 매우 유연하며 사용자 정의 함수를 사용할 수 있음.
"""

import pandas as pd

# 더미 데이터 생성
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# count
count_result = df.groupby('Category')['Value'].count()
print("Count 결과:")
print(count_result)

# sum
sum_result = df.groupby('Category')['Value'].sum()
print("\nSum 결과:")
print(sum_result)

# mean, median: 평균값, 중앙값
mean_result = df.groupby('Category')['Value'].mean()
median_result = df.groupby('Category')['Value'].median()

print("\nMean 결과:")
print(mean_result)
print("\nMedian 결과:")
print(median_result)

min_result = df.groupby('Category')['Value'].min()
max_result = df.groupby('Category')['Value'].max()

# min, max
print("\nMin 결과:")
print(min_result)
print("Max 결과:")
print(max_result)

# var, std
var_result = df.groupby('Category')['Value'].var()
std_result = df.groupby('Category')['Value'].std()

print("\nVariance 결과:")
print(var_result)
print("\nStandard Deviation 결과:")
print(std_result)

# first, last
first_result = df.groupby('Category')['Value'].first()
last_result = df.groupby('Category')['Value'].last()

print("\nfirst 결과:")
print(first_result)
print("\nlast 결과:")
print(last_result)

# Describe: 기술통계량
describe_result = df.groupby('Category')['Value'].describe()
print("\nDescribe 결과:")
print(describe_result)

# aggregate or agg
aggregate_result = df.groupby('Category')['Value'].agg(['sum', 'max'])
print("\nAggregate 결과:")
print(aggregate_result)

# apply
def square_values(x):
    return x ** 2


apply_result = df.groupby('Category')['Value'].apply(square_values)
print("\nApply 결과:")
print(apply_result)
