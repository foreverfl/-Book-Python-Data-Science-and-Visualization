"""
- 일변량 비시각화: 분석 대상 데이터가 하나의 변수로 구성되고 요약 통계량, 빈도 등으로 표현하는 탐색 유형.
* 빈도표: 범주별 빈도 파악이 목적. 범주별 빈도 수 기반의 구성 파악 및 결측치 빈도 파악. 데이터 전체 수 대비 각 범주별 분포 파악.
* 연속형 비시각화: 기술 통계량(평균, 분산), 사분위수(중앙값), 분포 관련 지표(왜도, 첨도)
"""

import pandas as pd

# 1. 빈도표
# 예시 데이터프레임 생성
data = {'category': ['A', 'B', 'C', 'A', 'B', 'B', 'C', 'A', 'B', 'C']}
df = pd.DataFrame(data)

# value_counts() 함수를 통해 범주별 빈도 파악
frequency_table = df['category'].value_counts()
print(frequency_table)

# 2. 연속형 비시각화
# 예시 데이터프레임 생성
data = {'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# describe() 함수를 통해 기술 통계량 파악
descriptive_stats = df['value'].describe()
print(descriptive_stats)

# 3. 왜도 및 첨도
# 왜도(분포의 비대칭도) 계산
# 값이 0보다 크면 왼쪽으로 치우치고, 오른쪽꼬리가 긴 형태의 분포를 보임
skewness = df['value'].skew()
print('Skewness:', skewness)

# 첨도(분포의 뾰족함) 계산
# 값이 0보다 크면 표족한 모양을 지님
kurtosis = df['value'].kurt()
print('Kurtosis:', kurtosis)
