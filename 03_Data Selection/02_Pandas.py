"""
- Pandas: Python에서 데이터 분석을 위한 가장 인기 있는 라이브러리. 고성능의 DataFrame 객체를 제공하여 데이터 분석, 클린징, 처리, 시각화 등의 작업을 효과적으로 수행 가능.
* 주요 특징
1) 데이터 구조: Series와 DataFrame이라는 두 가지 주요 데이터 구조를 제공.
2) Series: 1차원 배열과 같은 데이터 구조로, 여러 데이터 타입을 저장할 수 있음.
3) DataFrame: 2차원 레이블이 있는 데이터 구조로, 다양한 타입의 열을 가질 수 있음.
4) 데이터 처리: 데이터 병합, 조인, 리쉐이핑, 피벗, 슬라이싱, 인덱싱, 데이터 클린징 등의 다양한 데이터 처리 기능을 제공.
5) 데이터 분석: 그룹화, 집계, 통계 계산 등의 기능을 통해 데이터 분석을 지원.
6) 시계열 처리: 날짜 및 시간 데이터를 위한 기능을 제공하며, 시계열 분석 및 빈도 변환 등의 작업을 수행 가능.
7) 데이터 입출력: CSV, Excel, SQL, HDF5, Parquet 등 다양한 데이터 소스로부터 데이터를 읽고 쓸 수 있는 기능을 제공.
"""

import pandas as pd

# Slicing(슬라이싱)
arr = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = arr[2:6]  # 인덱스 2부터 인덱스 5까지의 원소를 슬라이싱하여 추출
print(result)

# Indexing(인덱싱)
arr = pd.Series([11, 22, 33, 44, 55])
result = arr[3]  # 인덱스 3의 원소를 가져옴
print(result)


# Boolean Indexing(불리언 인덱싱)
arr = pd.Series([1, 2, 3, 4, 5])
condition = arr % 2 == 0  # 배열에서 짝수인 원소만 추출
result = arr[condition]
print(result)


# Fancy Indexing(팬시 인덱싱)
arr = pd.Series([10, 20, 30, 40, 50])
indices = [1, 3]  # 인덱스 1, 3의 원소를 추출
result = arr[indices]
print(result)
