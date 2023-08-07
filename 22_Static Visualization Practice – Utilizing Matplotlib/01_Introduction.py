"""
- Matplotlib: 데이터 시각화 라이브러리. 2D 형태의 그래프와 이미지를 그릴 때 많이 사용.
* 그래프 그리기
1) plt.figure()
2) plt.plot(): 데이터 시각화 기능 담당.
3) plt.show()
"""

import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y, label="Prime numbers")  # x와 y 데이터를 사용해 선 그래프 그리기
plt.title("Basic Plot with Matplotlib")  # 그래프 제목 설정
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()  # 범례 표시
plt.show()
