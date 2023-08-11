"""
- SVM
* SVM은 주로 분류와 회귀 문제에 사용되는 강력한 알고리즘.
* 데이터를 클래스(범주)로 나누는 결정 경계를 찾음.
* SVM은 고차원 데이터에도 잘 작동하며, 데이터 선택을 통해 중요한 변수들을 찾아낼 수 있음. 
* 이렇게 선택된 변수들을 사용하면 모델의 복잡성을 줄이고 일반화 성능을 향상시킬 수 있음.
"""

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# X_train: 특성 (Feature) 데이터의 훈련 세트 부분. 모델 학습에 사용됩니다. 이 예제에서는 붓꽃 데이터셋의 4가지 특성(꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비)이 포함됨.
# X_test: 특성 데이터의 테스트 세트 부분. 모델이 얼마나 잘 일반화되었는지 평가할 때 사용됨.
# y_train: 타겟 (Target) 데이터의 훈련 세트 부분. 모델 학습에 사용되며, X_train에 해당하는 라벨(붓꽃의 품종)을 포함.
# y_test: 타겟 데이터의 테스트 세트 부분. 모델 평가에 사용되며, X_test에 해당하는 라벨을 포함함.
# rain_test_split(): 첫 번째 인자는 feature. 두 번째 인자는 target
# random_state: 무작위 분할의 결과를 재현 가능하게 하기 위해 사용됨
X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names], df['target'], random_state=0)

# SVM 모델 생성 및 학습
model = svm.SVC(kernel='linear')  # linear 커널을 사용한 SVM 분류기 생성
model.fit(X_train, y_train)  # 모델 학습

# 테스트 데이터에 대한 예측 수행
predicted = model.predict(X_test)

# 예측 결과 출력
print(predicted)
