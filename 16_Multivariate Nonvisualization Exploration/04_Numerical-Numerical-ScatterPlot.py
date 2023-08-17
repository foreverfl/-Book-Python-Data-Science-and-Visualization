"""
- 연속형 - 연속형
* 산점도
1) 연속형 변수 간 관계성을 개략적으로 파악(선형/비선형 및 음양 방향 등).
2) 연속형 데이터 간의 관계를 그래프 상으로 어떠한 관계까 있는지 파악하기 위함.
3) 변수 간 분포를 통해 선형 또는 비선형 관계 및 음양의 방향 등을 빠르게 파악할 수 있음.
4) 범주 Label 간 비교가 필요할 경우, 해당 부분의 그룹 정보르 ㄹ표시하면 변수 간 관계 및 범주 그룹 간 관계를 함께 파악 가능.
"""

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

# 폰트 찾기
font_list = [(f.name, f.fname)
             for f in fm.fontManager.ttflist if 'Gulim' in f.name]
print(font_list)

if len(font_list) > 0:
    plt.rcParams['font.family'] = font_list[0][0]
else:
    print("Gulim 폰트가 설치되어 있지 않습니다.")

# 예제 데이터 생성
np.random.seed(0)
# np.random.rand(100)는 0과 1 사이의 균일 분포에서 무작위로 생성된 100개의 실수를 배열로 반환
# 0~10 사이의 무작위 데이터 100개
x = np.random.rand(100) * 10  
y = 2.5 * x + np.random.normal(0, 2, 100)  # x에 대한 선형 관계를 갖는 y 데이터 생성

# 범주 데이터 추가 (예제: 두 개의 그룹 'A', 'B')
# list comprehension을 이용해서 값이 작으면 A, 크면 B를 할당
labels = ['A' if value < 5 else 'B' for value in x]

# 산점도 그리기
for label in set(labels):  # labels에서 중복들 제거한 값을 반환
    mask = [l == label for l in labels]
    # mask 리스트를 이용해 x와 y에서 해당하는 값만 선택하여 산점도에 표시
    plt.scatter(x[mask], y[mask], label=label)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('scatter')
plt.legend()
plt.show()
