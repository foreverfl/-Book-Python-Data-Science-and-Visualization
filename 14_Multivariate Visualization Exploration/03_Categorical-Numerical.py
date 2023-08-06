"""
- 범주형 - 연속형
* 비시각화 방안: 범주별 통계량
* 목적
1) 범주 별 대표 통계량 비교 파악.
2) 범주형-연속형 변수 조합 간 볌주 별 대표 수치 비교.
"""

import pandas as pd
import numpy as np

# 예시 데이터 생성
np.random.seed(42)
data = {
    '성별': np.random.choice(['남자', '여자'], 100),
    '제품': np.random.choice(['제품A', '제품B', '제품C'], 100),
    '판매량': np.random.randint(1, 100, 100)
}

df = pd.DataFrame(data)

# '성별' 별 '판매량'의 평균
gender_avg_sales = df.groupby('성별')['판매량'].mean()
print(gender_avg_sales)

# '제품' 별 '판매량'의 평균
product_avg_sales = df.groupby('제품')['판매량'].mean()
print(product_avg_sales)

# '성별'과 '제품' 별 '판매량'의 평균
gender_product_avg_sales = df.groupby(['성별', '제품'])['판매량'].mean(
).unstack()  # unstack(): 다중 인덱스를 갖는 결과를 테이블 형태로 재구성
print(gender_product_avg_sales)
