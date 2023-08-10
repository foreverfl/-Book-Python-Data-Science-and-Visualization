"""
- scatterplot: 두 변수 간의 관계를 나타내는 산점도.

- regplot: 산점도와 선형 회귀 모델의 선을 함께 그림.
* 선형 회귀선을 그리는 기본 기능을 제공하며, 더 단순하고 유연함.
* matplotlib의 축 객체에 그릴 수 있어서, 다중 서브플롯 등에서 사용하기 좋음.

- rugplot: 단변량 분포를 1차원으로 나타냄.
* 단변량 분포:
1) 하나의 변수에 대한 데이터의 분포를 나타냄.
2) 단변량 분포에서는 해당 변수의 중심 경향, 퍼짐, 왜도 등을 살펴볼 수 있음.
3) rugplot은 이러한 단변량 분포를 시각적으로 나타내주어, 데이터가 어디에 얼마나 집중되어 있는지 살펴보는 데 유용함.

- lmplot: regplot과 비슷하지만, 더 복잡한 모델을 만드는 데 유용함.
* regplot과 기본 기능은 유사하나, FacetGrid를 사용하여 추가적인 카테고리 변수를 적용할 수 있음.
* hue, col, row 등의 매개변수를 사용해 복잡한 모델을 표현할 수 있어 다변량 데이터를 분석하기에 좋음.
* 상대적으로 더 높은 수준의 인터페이스를 제공함.

- pairplot: 데이터셋 내의 여러 변수 간의 관계를 시각화. 전체 판에 그려짐.

- pivot_table: pivot_table 메서드를 사용하여 피벗 테이블을 만듬.

- heatmap: 데이터의 밀도나 빈도를 시각화.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn의 내장 데이터셋 'tips' 불러오기
tips = sns.load_dataset('tips')
print(tips.head()) # 데이터의 처음 5행 출력

plt.figure(figsize=(5, 5))
plt.suptitle("scatterplot / regplot / rugplot / lmplot", fontsize=14)

# scatterplot
plt.subplot(2, 2, 1)
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("scatterplot")

# regplot 
plt.subplot(2, 2, 2)
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title("regplot")

# rugplot
plt.subplot(2, 2, 3)
sns.rugplot(x='total_bill', data=tips)
plt.title("rugplot")

# lmplot 대신 regplot 사용
plt.subplot(2, 2, 4)
sns.regplot(x='total_bill', y='tip', data=tips, color='blue')
sns.regplot(x='total_bill', y='tip', data=tips[tips['sex'] == 'Female'], color='red')
plt.title("lmplot")

plt.tight_layout()
plt.show()

# pairplot
sns.pairplot(tips)
plt.show()

# pivot_table
# 성별과 요일별로 총 결제 금액의 평균을 한 눈에 확인할 수 있는 형태로 정리한 것
# values='total_bill': 피벗 테이블의 값 부분에 쓰일 열을 지정. 여기서는 'total_bill' 열을 사용하므로 총 결제 금액의 정보가 표시됨
# index='sex': 피벗 테이블의 행 인덱스로 사용할 열을 지정함. 여기서는 'sex' 열을 사용하므로 행은 성별에 따라 나눠짐
# columns='day': 피벗 테이블의 열 인덱스로 사용할 열을 지정함. 여기서는 'day' 열을 사용하므로 열은 요일에 따라 나눠짐
# aggfunc='mean': 집계 함수로, 여기서는 'mean'을 사용하므로 해당 성별과 요일의 조합에서 'total_bill' 값의 평균이 계산됨
pivot_tips = tips.pivot_table(values='total_bill', index='sex', columns='day', aggfunc='mean')
print(pivot_tips)

# heatmap
plt.figure()
sns.heatmap(pivot_tips, annot=True)
plt.show()