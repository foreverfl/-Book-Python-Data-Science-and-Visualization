"""
- Seaborn: Matplotlib을 기반으로 하며 디자인 테마와 통계용 차트가 추가된 시각화 라이브러리.
* 변수가 추가될 수록 메모리 부족 이슈 및 가독성이 떨어짐.
* 고수준 시각화에 특화: 산점도 구현, 추세선 출력, jointplot을 포함한 여러 플롯, statsmodels를 이용한 데이터 분포 시각화.
* 다채로운 시각화 기능을 제공.
"""

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # 내장 데이터셋 'tips' 불러오기
print(tips.head()) # 데이터의 처음 5행 출력

# lmplot은 데이터를 사용하여 이 선형 관계를 찾고, 이 관계를 표현하는 선을 그래프에 그림
# 이 선은 최소제곱법을 사용하여 데이터 포인트들 사이의 거리를 최소화하는 방식으로 결정됨
# 코드에서 x는 독립 변수, y는 종속 변수, 데이터는 'tips' 데이터셋
sns.lmplot(x='total_bill', y='tip', data=tips) 
plt.show()
