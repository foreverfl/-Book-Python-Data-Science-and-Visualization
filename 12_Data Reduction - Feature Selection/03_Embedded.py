"""
- Embedded: 모델 정확도에 기여하는 특징들을 선택하는 방법론. Filter와 Wrapper의 장점을 결합. 모델의 학습 및 생성과정에서 최적의 특징을 선택하는 방법.
* 알고리즘 내 자체 내장 함수로 특징을 선택. 학습과정에서 최적화된 변수를 선택. 트리 계열 모델 기반의 특징 선택이 대표적.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

iris = load_iris()
X = iris.data
y = iris.target

# 랜덤 포레스트는 여러 개의 결정 트리를 생성하고, 이들 각각에서 나온 예측을 종합하여 최종 예측
# 이 방법은 특징의 중요도가 주어진 임계치(여기서는 중앙값)보다 큰 모든 특징을 선택
clf = RandomForestClassifier(n_estimators=50)  # 랜덤 포레스트에서 사용할 트리의 개수
clf = clf.fit(X, y)  # fit()은 객체를 학습시키는 메소드

model = SelectFromModel(clf, prefit=True)  # 주어진 모델의 특징 중요도를 기반으로 특징을 선택하는 유틸리티
X_new = model.transform(X)  # 객체인 model을 사용하여 입력데이터 X를 변환하는 메소드

print("Original number of features:", X.shape[1])
print("Reduced number of features:", X_new.shape[1])
