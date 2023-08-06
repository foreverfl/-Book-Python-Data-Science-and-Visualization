"""
- 차원 축소: 원본 데이터로부터 새로운 특징의 집합을 생성. 고차원 원시 데이터 셋을 저차원으로 축소.
* 프로세스
1) PCA(Principal Compnent Analysis): 변수들이 지닌 정보를 최대한 확보하는 저차원 데이터로 생성. 서로 연관된 변수들이 관측되었을 때, 원본 데이터 분산 기반의 특징을 생성함. 주성분 간이 서로 독립을 이루도록함.
2) Featurization via Clustering: 군집 분석 기반의 고차원 데이터를 하나의 특징으로 차원 축소. 이렇게 획득한 군집결과 특징을 분류/회귀 등 문제해결을 위한 입력변수로 활용(Stacking). 여러개의 특징을 하나의 특징으로 축소하여 모델 연산 비용 감소 추구.
"""

import pandas as pd
from sklearn.decomposition import PCA

data = {
    'score1': [90, 85, 78, 92, 80],
    'score2': [88, 95, 79, 88, 90],
    'datetime': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05']
}

df = pd.DataFrame(data)
print(df)

# PCA를 위해 'datetime' 열은 제외. 'score1'과 'score2' 열만을 추출.
X = df.drop('datetime', axis=1)

# PCA 모델 생성. n_components=1로 설정하여 'score1'과 'score2'를 1차원으로 축소.
pca = PCA(n_components=1)

# PCA 모델을 사용하여 'score1'과 'score2'를 저차원으로 축소
df['new_feature'] = pca.fit_transform(X)

print('\n', df)
