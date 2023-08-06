"""
- Seaborn: Matplotlib을 기반으로 하며 디자인 테마와 통계용 차트가 추가된 시각화 라이브러리.
* 특징
1) 변수가 추가될 수록 메모리 부족 이슈 및 가독성이 떨어짐.
2) 고수준 시각화에 특화: 산점도 구현, 추세선 출력, jointplot을 포함한 여러 플롯, statsmodels를 이용한 데이터 분포 시각화.
3) 다채로운 시각화 기능을 제공.

- Seaborn으로 그래프 그리기: 댜양한 그래프 종류와 인수로 효과적인 시각화 가능.
"""

# 라이브러리 임포트
import seaborn as sns
import matplotlib.pyplot as plt

# 내장 데이터셋 'tips' 불러오기
tips = sns.load_dataset('tips')

# 데이터의 처음 5행 출력
print(tips.head())

# lmplot을 사용하여 총 금액(total_bill) 대비 팁(tip)의 관계를 선형 회귀로 표시
sns.lmplot(x='total_bill', y='tip', data=tips)

# 그래프 표시
plt.show()
