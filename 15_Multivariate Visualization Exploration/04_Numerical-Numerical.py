"""
- 연속형 - 연속형
* 비시각화 방안: Corr.coefficient(상관계수)
* 목적: 두개 연속형 변수의 관계성 정도 파악.

- 높은 상관계수: 비슷한 정보를 제공하는 밀접한 관계의 변수.
* 회귀분석에서 독립변수 간에 강한 상관관계 발생으로 인해 다중공선성 발생.
* 독립변수 간의 관계는 독립적이라는 회귀분석 가정에 위배됨.
* 회귀 계수가 불안정하여 종속 변수에 미치는 영향력을 올바르게 설명하지 못하므로 모델의 안정성 저해.
"""

import pandas as pd
import numpy as np

# 임의의 데이터 생성
np.random.seed(42)
data = {
    # 0 이상 1 미만 범위에서 균등 분포(uniform distribution)를 따르는 난수들을 생성
    '변수A': np.random.rand(100),
    '변수B': np.random.rand(100),
    # 변수A와의 상관관계를 약간 높게 설정
    '변수C': 0.5 * np.random.rand(100) + 0.5 * np.random.rand(100)
}

df = pd.DataFrame(data)

# corr(): 데이터 프레임에 포함된 연속형 변수 간의 상관계수를 계산. 반환값은 변수 간의 상관계수를 나타내는 데이터 프레임
correlation_matrix = df.corr()
print(correlation_matrix)
