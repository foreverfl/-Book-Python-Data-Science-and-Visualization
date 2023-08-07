"""
- 독립표본 t검정(Independent two-sample t-test): 두 독립된 집단의 평균값이 서로 다른지를 판단하기 위한 검정.
* 가설 설정
1) 귀무가설 (H0): 집단 A의 평균 = 집단 B의 평균
2) 대립가설 (H1): 집단 A의 평균 ≠ 집단 B의 평균
* 가정: 독립성, 정규성 확인, 등분산성 확인
"""

import pandas as pd
from scipy import stats

# Group_A와 Group_B의 평균이 다른지를 검증
# 예시 데이터 생성
data = {
    'Group_A': [85, 88, 75, 66, 90, 78, 77, 79, 80],
    'Group_B': [72, 79, 83, 69, 85, 76, 73, 78, 85]
}
df = pd.DataFrame(data)

# 독립표본 t검정 수행
# ttest_ind 함수는 독립표본 t검정을 수행하는 함수
t_stat, p_value = stats.ttest_ind(df['Group_A'], df['Group_B'])

# 결과 출력
# 계산된 t-통계량 값을 반환. t-통계량은 두 집단의 평균 차이가 표준오차로 얼마나 떨어져 있는지를 나타내는 값
print(f"t-통계량: {t_stat}")
# p-value는 귀무가설이 참일 때 현재의 표본 데이터나 더 극단적인 데이터를 관측할 확률
print(f"p-value: {p_value}")

if p_value < 0.05:
    print("귀무가설을 기각합니다. 두 집단의 평균은 유의하게 다릅니다.")
else:
    print("귀무가설을 채택합니다. 두 집단의 평균은 유의하게 다르지 않습니다.")
