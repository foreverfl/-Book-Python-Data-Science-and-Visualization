"""
- SVM
* 특징
* 1) SVM은 주로 분류와 회귀 문제에 사용되는 강력한 알고리즘.
* 2) 데이터를 클래스(범주)로 나누는 결정 경계를 찾음.
* 3) SVM은 고차원 데이터에도 잘 작동하며, 데이터 선택을 통해 중요한 변수들을 찾아낼 수 있음. 
* 4) 이렇게 선택된 변수들을 사용하면 모델의 복잡성을 줄이고 일반화 성능을 향상시킬 수 있음.
"""

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# rain_test_split 함수는 첫 번째 인자로 피처들, 두 번째 인자로 타겟을 받아, 데이터를 무작위로 학습 데이터와 테스트 데이터로 분할
# random_state 인자는 무작위 분할의 결과를 재현 가능하게 하기 위해 사용됨
X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names], df['target'], random_state=0)

# SVM 모델 생성 및 학습
model = svm.SVC(kernel='linear')  # linear 커널을 사용한 SVM 분류기 생성
model.fit(X_train, y_train)  # 모델 학습

# 테스트 데이터에 대한 예측 수행
predicted = model.predict(X_test)

# 예측 결과 출력
print(predicted)
