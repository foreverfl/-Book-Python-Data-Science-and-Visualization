"""
- 단순회귀분석: 한 개의 종속변수(Y)와 한 개의 독립변수(X) 사이의 관계를 분석하는 통계 기법.
* 기본 가정
1) 선형성: 독립변수(X)와 종속변수(Y)는 선형관계임.
2) 독립성: 종속변수 Y는 서로 독립이어야 함.
3) 등분산성: 독립변수 X의 값에 관계없이 종속변수 Y의 분산은 일정함.
4) 정규성: 독립변수 X의 고정된 어떤 값에 대하여 종속변수 Y는 정규 분포를 따름.
- 최소제곱법(OLS): 잔차를 최소화하는 회귀 계수 추청.
- 결정계수
* 전체 제곱합(SST) = 회귀 제곱합(SSR) + 잔차 제곱합(SSE)
* 총 변동을 설명하는데 있어서 회귀선에 의하여 설명되는 변동 기여 비율.
* t검정: 단순회귀계수를 검정할 때, 개별회귀계수의 통계적 유의성은 t검정으로 확인.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

# 예제 데이터 생성
data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [2.5, 4.5, 6, 7.5, 9, 10.5, 12, 13, 14.5, 16]
}
df = pd.DataFrame(data)

# X에 상수항(Intercept) 추가
X = sm.add_constant(df['X'])
Y = df['Y']

# OLS(최소제곱법)을 이용한 회귀 모델 학습
model = sm.OLS(Y, X).fit()

# 결과 출력
print(model.summary())

# 결정계수
print(f"\n결정계수(R^2): {model.rsquared:.3f}")

# t검정 결과
print(f"\nX의 t값: {model.tvalues['X']:.3f}")
