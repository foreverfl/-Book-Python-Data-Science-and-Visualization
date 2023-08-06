"""
- 상관계수: 두 변수 간의 함께 변화하는 경향을 객관적으로 측정할 수 있는 척도.
* 피어슨 상관계수: 선형관계의 강도를 측정. 상관계수 r은 -1부터 1까지 값을 가짐
1) r=0: 두 변수간 선형관계가 없음.
2) r=1: 완벽한 우상향 직선의 관계. 양의 상관관계.
3) r=-1: 완벽한 우하향 직선의 관계. 음의 상관관계.
* 스피어맨 상관계수: 비선형 순위 상관관계를 측정.
1) 스피어맨은 정규분포가 아니어도 monotonic(단조) 증가/하락에 관한 비선형 관계 포함 가능.
"""
import pandas as pd

# 피어슨 상관계수
# 예제 데이터 생성
data = {
    'Variable_X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Variable_Y': [2, 4, 5, 4, 5, 7, 7, 8, 10, 11]
}
df = pd.DataFrame(data)

# 피어슨 상관계수 계산
pearson_corr = df['Variable_X'].corr(df['Variable_Y'])

print(f"피어슨 상관계수: {pearson_corr:.3f}")

# 스피어맨 상관계수 계산
spearman_corr = df['Variable_X'].corr(df['Variable_Y'], method='spearman')

print(f"스피어맨 상관계수: {spearman_corr:.3f}")
