"""
- 교차테이블: 교차테이블(cross-tabulation, 또는 crosstab)은 두 개 이상의 범주형 변수의 빈도수를 기록한 테이블.
* 다차원 빈도수를 정리해서 보여주는 통계학의 기본 도구 중 하나로, 데이터의 패턴을 이해하는 데 유용하게 사용됨.
- crosstab(): 두 범주형 변수 간의 교차 테이블을 생성하는데 사용됨.
"""

import pandas as pd

# 예시 데이터프레임 생성
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']}
df = pd.DataFrame(data)

print("기본 교차 테이블:")
cross_tab = pd.crosstab(df['A'], df['B']) # crosstab을 통한 교차 테이블 생성
print(cross_tab)

print("\n합계가 포함된 교차 테이블:")
cross_tab = pd.crosstab(df['A'], df['B'], margins=True) # margins는 행과 열의 합계를 추가
print(cross_tab)


print("\n비율로 나타낸 교차 테이블:")
cross_tab = pd.crosstab(df['A'], df['B'], normalize=True) # normalize는 전체 빈도에 대한 비율을 나타냄
print(cross_tab)
