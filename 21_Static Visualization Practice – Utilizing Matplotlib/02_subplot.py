"""
- plt.subplot(row, column, index)
* 특징: 각 subplot에 다른 종류의 그래프(예: 선 그래프, 막대 그래프)를 그릴 때 효과적.
"""

import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)  # 0부터 10까지 100개의 값 생성
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
y4 = np.cos(x) * np.sin(x)

# 첫 번째 그래프(1행 1열 위치)
plt.subplot(2, 2, 1)  # 2x2 형태의 첫 번째 그래프
plt.plot(x, y1)
plt.title("sin(x)")

# 두 번째 그래프(1행 2열 위치)
plt.subplot(2, 2, 2)  # 2x2 형태의 두 번째 그래프
plt.plot(x, y2)
plt.title("cos(x)")

# 세 번째 그래프(2행 1열 위치)
plt.subplot(2, 2, 3)  # 2x2 형태의 세 번째 그래프
plt.plot(x, y3)
plt.title("sin(x) * cos(x)")

# 네 번째 그래프(2행 2열 위치)
plt.subplot(2, 2, 4)  # 2x2 형태의 네 번째 그래프
plt.plot(x, y4)
plt.title("cos(x) * sin(x)")

# 그래프를 깔끔하게 보이게 하기 위해 공간 확보
plt.tight_layout()

# 그래프 보이기
plt.show()
