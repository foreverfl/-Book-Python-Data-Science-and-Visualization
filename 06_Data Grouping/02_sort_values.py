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
