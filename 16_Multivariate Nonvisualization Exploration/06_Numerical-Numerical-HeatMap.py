"""
- 연속형 - 연속형
* 히트맵(HeatMap): 히트맵은 데이터 매트릭스를 색상으로 표현하여 변수 간의 관계나 데이터의 분포를 시각적으로 파악할 수 있게 해주는 시각화 방법. 
1) 대량의 데이터를 한 눈에 파악할 수 있음.
2) 변수 간의 관계의 강도를 색의 진하기로 쉽게 파악할 수 있음
3) 데이터의 패턴이나 클러스터를 빠르게 확인할 수 있음.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 예제 데이터 생성
np.random.seed(0)
df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100) + 1,
    'C': np.random.randn(100) - 1,
    'D': np.random.randn(100) * 2
})

# 상관계수 매트릭스 생성
corr_matrix = df.corr()
print(corr_matrix)

# 히트맵 생성
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("HeatMap of Correlation Matrix")
plt.show()
