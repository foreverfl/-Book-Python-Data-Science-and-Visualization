import pandas as pd
# groupby: 특정 열, 열의 리스트 또는 행 인덱스를 기준으로 그룹화를 진행함.

# 더미 데이터 생성
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# - count
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 각 그룹의 개수를 세기
count_result = df.groupby('Category')['Value'].count()
print("Count 결과:")
print(count_result)

# - sum
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 합 구하기
sum_result = df.groupby('Category')['Value'].sum()
print("\nSum 결과:")
print(sum_result)

# - mean, median: 평균값, 중앙값# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 평균과 중앙값 구하기
mean_result = df.groupby('Category')['Value'].mean()
median_result = df.groupby('Category')['Value'].median()

print("\nMean 결과:")
print(mean_result)

print("\nMedian 결과:")
print(median_result)

# - min, max
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 최솟값과 최댓값 구하기
min_result = df.groupby('Category')['Value'].min()
max_result = df.groupby('Category')['Value'].max()

print("\nMin 결과:")
print(min_result)

print("\nMax 결과:")
print(max_result)

# - var, std: 분산, 표준편차
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 분산과 표준편차 구하기
var_result = df.groupby('Category')['Value'].var()
std_result = df.groupby('Category')['Value'].std()

print("\nVariance 결과:")
print(var_result)

print("\nStandard Deviation 결과:")
print(std_result)

# - first, last
first_result = df.groupby('Category')['Value'].first()
last_result = df.groupby('Category')['Value'].last()

print("\nfirst 결과:")
print(first_result)

print("\nlast 결과:")
print(last_result)

# - Describe: 기술통계량
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 기술통계량 요약 출력
describe_result = df.groupby('Category')['Value'].describe()
print("\nDescribe 결과:")
print(describe_result)

# - aggregate or agg
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 합과 최댓값 동시에 구하기
aggregate_result = df.groupby('Category')['Value'].agg(['sum', 'max'])
print("\nAggregate 결과:")
print(aggregate_result)

# - apply
# 'Category' 열을 기준으로 그룹화하여 'Value' 열의 값을 제곱하는 함수 적용하기


def square_values(x):
    return x ** 2


apply_result = df.groupby('Category')['Value'].apply(square_values)
print("\nApply 결과:")
print(apply_result)
