"""
- 범주형 - 범주형
* 비시각화 방안: Cross tabulation(교차표)
* 목적
1) 두개 범주형 변수의 범주별 연관성 및 구성 파악
2) 조합 간 연관 관계 파악
"""

import pandas as pd

# 예시 데이터프레임
data = {
    '성별': ['남자', '여자', '남자', '여자', '남자', '남자', '여자', '남자', '여자', '여자'],
    '제품': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']
}
df = pd.DataFrame(data)
print('데이터')
print(df)

# 교차표
# index: 교차표의 row로 사용할 데이터
# column: 교차표의 column으로 사용할 데이터
cross_tab = pd.crosstab(df['성별'], df['제품'])
print('\n교차표')
print(cross_tab)
