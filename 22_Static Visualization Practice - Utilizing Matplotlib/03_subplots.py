"""
- subplots: axes 객체의 twinx메소드를 이용하면 x축을 공유하는 2개의 그래프를 통시에 그릴 수 있음.
* 동일한 유형의 그래프를 여러 개 그릴 때, 또는 그래프 전체에 대한 제어가 필요할 때 효과적.
"""

import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)  # 0부터 10까지 100개의 값 생성
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
y4 = np.cos(x) * np.sin(x)

# 2x2 형태의 그래프 생성
fig, axes = plt.subplots(2, 2)

# 첫 번째 그래프 (1행 1열 위치)
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("sin(x)")

# 두 번째 그래프 (1행 2열 위치)
axes[0, 1].plot(x, y2)
axes[0, 1].set_title("cos(x)")

# 세 번째 그래프 (2행 1열 위치)
axes[1, 0].plot(x, y3)
axes[1, 0].set_title("sin(x) * cos(x)")

# 네 번째 그래프 (2행 2열 위치)
axes[1, 1].plot(x, y4)
axes[1, 1].set_title("cos(x) * sin(x)")

# 그래프를 깔끔하게 보이게 하기 위해 공간 확보
plt.tight_layout()

# 그래프 보이기
plt.show()
