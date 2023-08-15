"""
- 히스토그램
* 연속형 테이터 값들의 분포 파악 가능
* 구간내 속하는 자료의 수가 많고 적음을 쉽게 파악 가능.

- 커널밀도추청
* 연속형 데이터 값을의 분포를 분석하여 연속성 있는 확률 밀도 함수를 추정.
* 변수가 가질 수 있는 모든 값의 확률을 추정하는 것.
* 히스토그램의 한계점을 극복하기 위해 고안된 방안.

- 박스플롯
* 연속형 데이터의 양상을 직관적으로 파악할 수 있는 방안으로 5가지 요약치를 기반으로 생성
1) 중앙값
2) 1분위수
3) 3분위수
4) 최댓값(IQR Value)
5) 최소값
* 데이터의 개략적인 흩어짐의 형태 파악 및 IQR 기반의 이상치 판단에 용이함
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# 임의의 데이터 생성
np.random.seed(42)  # 결과를 동일하게 재현하기 위한 random seed 설정
data = np.random.randn(1000)  # 표준 정규 분포에서 1000개의 무작위 샘플을 생성
df = pd.DataFrame(data, columns=['Value'])
print(df)

# 히스토그램
plt.figure(figsize=(10, 6))
 # 데이터를 50개의 구간으로 나누어서 히스토그램을 그림
 # alpha: 색상의 투명도
plt.hist(df['Value'], bins=50, color='blue', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 커널밀도추정
plt.figure(figsize=(10, 6))
# shade=True: 그래프의 아래를 칠하겠다는 의미
sns.kdeplot(df['Value'], shade=True, color='green')
plt.title('Kernel Density Estimation')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# 박스플롯
plt.figure(figsize=(10, 6))
plt.boxplot(df['Value'])
plt.title('Box Plot')
plt.ylabel('Value')
plt.show()
