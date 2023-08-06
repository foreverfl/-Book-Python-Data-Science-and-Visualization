"""
- scatterplot
- regplot
- rugplot
- lmplot
- pairplot
- pivot_table
- heatmap
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn의 내장 데이터셋 'tips' 불러오기
tips = sns.load_dataset('tips')

# scatterplot 사용 예제
# 산점도 그래프로 'total_bill'과 'tip' 사이의 관계를 표시
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatterplot of Total Bill vs Tip")
plt.show()

# regplot 사용 예제
# 산점도 그래프와 함께 선형 회귀선을 표시
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title("Regplot of Total Bill vs Tip")
plt.show()

# lmplot 사용 예제
# FacetGrid를 사용하여 산점도와 선형 회귀선을 함께 표시, hue 옵션을 사용하여 'sex'에 따라 색상 구분
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.title("Lmplot of Total Bill vs Tip by Sex")
plt.show()
