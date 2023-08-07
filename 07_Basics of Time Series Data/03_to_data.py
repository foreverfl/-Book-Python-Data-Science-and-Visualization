import pandas as pd

# 예제 데이터: 날짜 문자열 리스트
date_strings = ['2023-07-31', '2023-08-01', '2023-08-02']

# pd.to_datetime() 함수를 사용하여 문자열을 datetime으로 변환
datetime_objects = pd.to_datetime(date_strings)

print(datetime_objects)
