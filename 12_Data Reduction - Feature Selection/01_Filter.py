"""
- Filter: 특징들에 대한 통계적 점수를 부여하여 순위를 매기고 선택하는 방법론. 실행 속도가 빠르다는 측면에서 시간 및 비용 측면의 장점을 보임.
* Chi-square filter(카이제곱 필터)
1) 범주형인 독립 및 종속 변수 간의 유의미성을 도출하기 위한 통계적 방안.
2) 연속형 범주를 이산화하여 활용 가능.
3) 독립성을 평가하고, 독립성이 낮을수록 해당 특징이 타겟 클래스와 관련이 깊다고 볼 수 있으므로, 그 특징을 선택함.
* Correlation filter
1) 연속적인 독립 및 종속변수 간 유의미성을 도출하기 위한 통계적 방안.
2) 보통 threshold(임계치) 설정하여 변수 선택.
3) 상관계수: 공분산을 각 변수의 표준편차로 나눈 값.
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

# Chi-square filter
iris = load_iris() # 붓꽃의 품종을 분류하는 데 사용되며, 각 품종에 대한 4개의 특징(꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비)을 포함
feature_names = iris.feature_names
print(feature_names)
X = iris.data
y = iris.target  # 붓꽃의 세 가지 품종

# 데이터를 pandas DataFrame으로 변환
# np.c_: numpy의 연결(concatenation) 기능으로, 배열을 수평으로 연결
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target']) 
iris_df['target'] = iris_df['target'].map({0: "setosa", 1: "versicolor", 2: "virginica"}) # target을 의미 있는 품종 이름으로 바꾸기
print(iris_df)

# Chi-square filter를 적용하려면, SelectKBest와 chi2를 함께 사용
# SelectKBest는 특징 선택 방법을 지정하고, 선택할 특징의 수를 결정하는 데 사용
# k=2: 가장 높은 카이제곱 통계를 가진 2개의 특징을 선택
chi2_selector = SelectKBest(chi2, k=2)
X_kbest = chi2_selector.fit_transform(X, y)

# shape는 numpy 배열의 차원을 보여주는 속성
# shape 속성은 이 배열의 차원을 표현하는 튜플을 반환
# X.shape[0]은 행의 수를 나타내고, X.shape[1]은 열의 수, 즉 특징의 수를 나타냄
print("Original number of features:", X.shape[1])
print("Reduced number of features:", X_kbest.shape[1])

# Correlation filter
np.random.seed(0)

# 랜덤하게 생성된 특징
F3 = np.random.normal(0, 1, 100)
F4 = np.random.normal(0, 1, 100)
F5 = np.random.normal(0, 1, 100)

# F1과 F2는 높은 상관관계를 가지도록 설정
F1 = np.random.normal(0, 1, 100)
F2 = F1 + np.random.normal(0, 0.1, 100)
df = pd.DataFrame({'F1': F1, 'F2': F2, 'F3': F3, 'F4': F4, 'F5': F5})

# Correlation filter를 적용하려면, pandas의 corr() 함수를 사용하여 상관계수를 계산한 후,
# 상관계수의 절대값이 특정 임계값(여기서는 0.5) 이상인 특징만 선택
correlated_features = set()
correlation_matrix = df.corr()  # 상관계수를 계산하여 상관계수 행렬을 반환
print(correlation_matrix)

for i in range(len(correlation_matrix.columns)):
    for j in range(i):  # 상관계수 행렬이 대칭행렬이므로, 행렬의 절반만 검사하면 모든 쌍의 상관계수를 확인 가능
        if abs(correlation_matrix.iloc[i, j]) > 0.5:
            colname = correlation_matrix.columns[i]
            correlated_features.add(colname)

print('\n', correlated_features)
