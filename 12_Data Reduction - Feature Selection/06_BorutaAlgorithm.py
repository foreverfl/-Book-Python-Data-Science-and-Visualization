"""
- Boruta
* 특징
1) 특성 선택을 위한 랜덤 포레스트 기반 알고리즘. 
2) 이 알고리즘은 원래 특성의 중요성을 무작위로 생성된 '그림자' 특성의 중요성과 비교하여 특성의 중요성을 평가. 
3) 그림자 특성은 원래 특성의 값을 무작위로 섞은 것으로, 실제로는 중요하지 않아야 함.
* 단계
1) 랜덤 포레스트 모델을 학습하고, 각 특성의 중요도를 계산.
2) 원래 특성의 값들을 무작위로 섞어서 그림자 특성을 생성하고, 랜덤 포레스트 모델을 다시 학습.
3) 그림자 특성의 최대 중요도보다 원래 특성의 중요도가 높으면, 해당 원래 특성을 중요하다고 판단.
4) 이 과정을 여러 번 반복하며, 각 특성이 중요하다고 판단된 횟수를 기록.
5) 마지막으로, 특성이 충분히 자주 중요하다고 판단되면, 해당 특성을 선택.
"""

from boruta import BorutaPy
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

# 랜덤 포레스트 분류기 설정
# n_jobs=-1은 사용 가능한 모든 CPU 코어를 사용하여 학습을 병렬로 수행하라는 의미
# class_weight='balanced'는 클래스 불균형을 처리하기 위해 각 클래스에 가중치를 부여하라는 의미
# 이는 소수 클래스의 샘플에 더 많은 가중치를 부여하여, 모델이 소수 클래스를 무시하는 것을 방지
# max_depth=5는 생성할 트리의 최대 깊이를 5로 제한하라는 의미
# 이는 트리가 너무 복잡해지는 것을 방지하고 과적합을 줄이는 데 도움이 됨
rf = RandomForestClassifier(
    n_jobs=-1, class_weight='balanced', max_depth=5)


# n_estimators='auto'는 Boruta 알고리즘이 내부적으로 사용하는 랜덤 포레스트의 트리 개수를 자동으로 설정하라는 의미
# verbose=2는 Boruta 알고리즘이 진행 상황을 자세히 출력하도록 설정
# random_state=1는 결과의 재현성을 보장하기 위해 랜덤 시드를 고정
feat_selector = BorutaPy(rf, n_estimators='auto',
                         verbose=2, random_state=1)  # Boruta 알고리즘 설정

feat_selector.fit(X, y)  # Boruta 알고리즘 실행

print(feat_selector.support_)  # 선택된 특성 출력
