"""
- 차원 축소: 원본 데이터로부터 새로운 특징의 집합을 생성. 고차원 원시 데이터 셋을 저차원으로 축소.
* Featurization via Clustering: 군집 분석 기반의 고차원 데이터를 하나의 특징으로 차원 축소. 
1) 이렇게 획득한 군집결과 특징을 분류/회귀 등 문제해결을 위한 입력변수로 활용(Stacking). 
2) 여러개의 특징을 하나의 특징으로 축소하여 모델 연산 비용 감소 추구.
* K-Means 알고리즘: 비슷한 특성을 가진 데이터들을 그룹으로 묶는 군집화 기법. 데이터가 원형으로 뭉쳐져 있는 경우에 잘 작동.
1) 초기 중심(Centroid) 무작위로 선택.
2) 각 데이터 포인트와 가까운 중심에 데이터 포인트 할당. 유클리드 거리가 주로 사용됨.
3) 데이터 포인트들의 평균을 계산하여 새로운 중심을 업데이트.
4) 2번과 3번을 데이터 포인터들이 변하지 않을 때까지 반복.
5) 데이터 포인터들이 변하지 않으면 알고리즘 종료.
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# 2차원 데이터를 생성
df = pd.DataFrame({
    # 평균이 0이고 표준편차가 1인 정규분포에서 랜덤하게 100개의 숫자를 생성
    'feature1': np.random.normal(0, 1, 100),
    'feature2': np.random.normal(0, 1, 100)
})

# KMeans 군집화를 수행. 여기서는 3개의 군집을 생성하도록 설정
# n_cluster: 군집의 개수
# n_init: 알고리즘을 여러번 실행할 때, 서로 다른 초기 중심점을 사용하는 횟수. 기본값은 10
kmeans = KMeans(n_clusters=4, n_init='auto') 
df['cluster'] = kmeans.fit_predict(df)

# 군집화 결과를 시각화
plt.scatter(df['feature1'], df['feature2'], c=df['cluster'])
plt.show()
