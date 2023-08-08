"""
- 결합 및 분해: 데이터 셋 변수들의 조합을 기반으로 새로운 특징을 구축. 변수간의 연산 혹은 분해를 통해 새로운 특징을 구축.
* 결합
1) Add/Divide: 종합적 수치 파악.
2) Subtract: 특정 수치의 편중 정도 파악.
3) Multiply: Interaction Feature로 시너지 효과 파악. 회귀 분석에 많이 사용함.
* 분해
1) Separate: 특정 변수 활용 기반의 새로운 의미를 파악할 수 있는 특징을 생성. 도메인 지식 및 일반적 개념 기반으로 생성 가능.
"""

import pandas as pd

df = pd.DataFrame({
    'score1': [90, 85, 78, 92, 88],
    'score2': [85, 80, 90, 88, 82],
    'datetime': pd.date_range(start='2020-01-01', periods=5)
})

# Add
df['total_score'] = df['score1'] + df['score2']

# Divide
df['average_score'] = df['total_score'] / 2

# Subtract
df['score_diff'] = df['score1'] - df['score2']

# Multiply
df['score_product'] = df['score1'] * df['score2']

# Separate
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time

print(df)
