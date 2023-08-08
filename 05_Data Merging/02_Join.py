"""
- join
* 인덱스를 기준으로 함.
* DataFrame의 메소드로 사용함.
* 왼쪽 DataFrame을 기준으로함.
* 중복된 칼럼이 있다면, 두 개 칼럼 모두 Dataframe에 다른 이름올 저장됨.
"""

import pandas as pd

# 예제 데이터 생성
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28]
}

data2 = {
    'Score': [85, 92, 78, 95],
    'Subject': ['Math', 'English', 'Science', 'History']
}

# DataFrame 생성
df1 = pd.DataFrame(data1, index=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(data2, index=['c', 'd', 'e', 'f'])

# join 수행
result_join = df1.join(df2)
print("Join 결과:")
print(result_join)
