"""
- sort_values
* 형태: dataframe.sort_values(by='열이름')
* 옵션
1) by: 정렬할 기준이 되는 열의 이름 또는 열의 이름 리스트를 지정. 여러 열을 리스트로 전달하면, 순차적으로 정렬됨.
2) axis: 정렬을 수행할 축을 지정. 0은 행 기준, 1은 열 기준. 기본값은 0입니다.
3) ascending: 정렬 순서를 지정. True이면 오름차순, False이면 내림차순. 여러 열을 정렬할 때는 불리언 값의 리스트를 전달할 수 있음. 기본값은 True.
4) inplace: 원본 객체를 변경할지 여부를 지정. True이면 원본 객체가 변경되고, False이면 새로운 객체가 반환됨. 기본값은 False.
5) na_position: 결측값(NaN)의 위치를 지정. 'first'이면 결측값이 처음에 위치하고, 'last'이면 마지막에 위치합. 기본값은 'last'.
6) ignore_index: 인덱스를 재설정할지 여부를 지정. True이면 인덱스가 재설정되고, False이면 원본 인덱스가 유지됨. 기본값은 False.
"""

import pandas as pd

# 예제 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 22, 28, 35],
    'Salary': [50000, 60000, 55000, 75000, 80000]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 'Age' 열을 기준으로 오름차순 정렬
sorted_by_age_asc = df.sort_values(by='Age')
print("Age 오름차순 정렬:")
print(sorted_by_age_asc)

# 'Salary' 열을 기준으로 내림차순 정렬
sorted_by_salary_desc = df.sort_values(by='Salary', ascending=False)
print("\nSalary 내림차순 정렬:")
print(sorted_by_salary_desc)
