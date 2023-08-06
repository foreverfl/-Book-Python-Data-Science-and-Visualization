"""
- crosstab(): 두 범주형 변수 간의 교차 테이블을 생성하는데 사용됨
"""

import pandas as pd

# 예시 데이터프레임 생성
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']}
df = pd.DataFrame(data)

# crosstab을 통한 교차 테이블 생성
cross_tab = pd.crosstab(df['A'], df['B'])
print(cross_tab)

# margins는 행과 열의 합계를 추가
cross_tab = pd.crosstab(df['A'], df['B'], margins=True)
print(cross_tab)

# normalize는 전체 빈도에 대한 비율을 나타냄
cross_tab = pd.crosstab(df['A'], df['B'], normalize=True)
print(cross_tab)
