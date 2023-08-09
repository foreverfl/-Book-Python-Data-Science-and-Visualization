"""
- Wrapper: 특징들의 조합을 지도학습 기반 알고리즘에 반복적으로 적용하여 특징을 선택하는 방법론. 최적의 데이터 조합을 찾기 때문에 성능 관점상 유용하나 시간과 비용이 크게 발생.
* 반복적 특징 조합 탐색: 원본 데이터셋 변수들의 다양한 조합을 모델에 적용. 최적의 subset을 도출하는 방법론. Recursive Feature Elemination이 대표적인 방식.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

iris = load_iris()
X = iris.data
y = iris.target

# Recursive Feature Elimination을 적용하려면, RFE를 사용하고, 원하는 모델(여기서는 로지스틱 회귀)을 함께 전달
# 로지스틱 회귀는 분류 문제를 해결하는 데 사용되는 알고리즘으로, 각 클래스에 속할 확률을 예측
# solver='lbfgs': 'lbfgs'는 모델을 최적화하는 알고리즘. 미분 가능한 목적 함수의 미니멈을 찾기 위한 반복 방법. 로지스틱 회귀에서는 손실 함수를 최소화하려고 사용됨
# multi_class='auto': 이 데이터셋은 다중 클래스 문제. 이 파라미터는 다중 클래스 분류 문제를 어떻게 처리할 것인지 지정
# max_iter=1000: 'max_iter'는 최적화 과정에서의 최대 반복 횟수. 이 숫자가 너무 작으면, 최적화가 수렴하지 않을 수 있으며, 너무 크면 과다한 계산 시간이 소요됨
model = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=1000)
rfe = RFE(model, n_features_to_select=2)  # 중요한 2개의 특성만 선택하도록 설정
fit = rfe.fit(X, y)

print("Number of Features: ", fit.n_features_)
print("Selected Features: ", fit.support_)
print("Feature Ranking: ", fit.ranking_)
