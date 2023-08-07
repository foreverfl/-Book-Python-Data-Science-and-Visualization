"""
- Numpy: Python에서 수치 계산을 위한 핵심 라이브러리. 대규모 다차원 배열 및 행렬 연산에 필요한 다양한 함수를 제공하며, 이는 고성능의 수학 연산과 과학 연산 작업에 필수적.
* 주요 특징
1) 다차원 배열 객체: NumPy의 핵심 기능은 ndarray라는 다차원 배열 객체.
2) 브로드캐스팅: 다른 크기의 배열 간 연산을 지원하는 기능.
3) 통합 수학 함수: 배열 데이터를 처리하는 데 필요한 기본적인 수학 함수를 제공.
4) 선형 대수, 난수 생성, 푸리에 변환과 같은 고급 수학 및 통계 연산 지원.
5) C, C++, 포트란과 같은 저수준 언어로 작성된 코드와 통합이 가능.
"""

import numpy as np

# Slicing(슬라이싱)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = arr[2:6]  # 인덱스 2부터 인덱스 5까지의 원소를 슬라이싱하여 추출
print(result)


# Indexing(인덱싱)
arr = np.array([11, 22, 33, 44, 55])
result = arr[3]  # 인덱스 3의 원소를 가져옴
print(result)


# Boolean Indexing(불리언 인덱싱):특정 조건에 따라 배열에서 값을 추출하는 방법
arr = np.array([1, 2, 3, 4, 5])
condition = arr % 2 == 0  # 배열에서 짝수인 원소만 추출
result = arr[condition]
print(result)


# Fancy Indexing(팬시 인덱싱): 배열에 인덱스 값을 리스트 또는 배열로 주어서 해당 인덱스 위치에 있는 원소들을 선택
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3]  # 인덱스 1, 3의 원소를 추출
result = arr[indices]
print(result)
