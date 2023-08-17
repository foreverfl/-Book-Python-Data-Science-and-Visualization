"""
- 다중회귀분석: 단순회귀분석의 확장으로 독립변수가 두 개 이상인 회귀모형에 대한 분석.
* 다중선형회귀모델
* 단순회귀와의 차이점: 단일 개의 독립변수가 아닌 여러 개의 독립 변수를 사용.
* 다중공선성
1) 독립변수 간 독립성이 없는 상관성 존재를 의미.
2) 여러 개의 독립 변수가 존재할 때 종속변수의 영향을 주는 독립변수를 찾는 것이 중요하며, 최적의 변수 선택 필요.

- 이차회귀모델: 비선형성을 고려한 이차회귀분석.

- 다항회귀모델
* 2차 이상의 회귀모형.
* 변수 간 상호작용 가능.
* 비선형적 추세를 고려할 수 있음.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 예제 데이터 생성
np.random.seed(42)
data = {
    'X1': np.random.rand(100),
    'X2': np.random.rand(100),
    'X3': np.random.rand(100),
    'Y': np.random.rand(100)
}
df = pd.DataFrame(data)
print('data')
print(df)

# X에 상수항(Intercept) 추가
X = sm.add_constant(df[['X1', 'X2', 'X3']])
Y = df['Y']

# OLS(최소제곱법)를 이용한 회귀 모델 학습
model = sm.OLS(Y, X).fit()

# 결과 출력
print(model.summary())

# VIF(Variance Inflation Factor)를 사용하여 다중공선성을 확인하기 위한 DataFrame을 생성
vif = pd.DataFrame()
# 'variance_inflation_factor' 함수를 사용해 각 독립 변수의 VIF 값을 계산
# 이 값을 "VIF Factor"라는 새로운 열로 DataFrame에 추가
# X.values는 독립변수들의 값을 가져오고, range(X.shape[1])는 독립변수의 갯수만큼 반복을 의미
vif["VIF Factor"] = [variance_inflation_factor(
    X.values, i) for i in range(X.shape[1])]
# VIF 값에 대응하는 독립변수의 이름을 "features"라는 열로 DataFrame에 추가
vif["features"] = X.columns
print("\n", vif)
