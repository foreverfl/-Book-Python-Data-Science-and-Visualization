"""
- 범주형 - 연속형
* 박스플롯
1) 범주 별 기술통계량 및 경향성을 개략적으로 파악.
2) 많은 데이터를 눈으로 직접 확인하기 어렵고, 대표적 통계 값만으로 파악하기 어려울때 용이함.
3) 범주 그룹(범주형 변수) 간 수치(연속형 변수)의 집합 범위와 중앙값, 이상치 등을 빠르게 확인할 수 있음.
4) 비시각화 기반의 단순 수치값 비교보다 데이터가 설명하는 많은 정보 획득 가능.

* 평행좌표
1) 범주형 - 연속형 변수 조합 간 경향성 파악
2) 연속형 데이터 기반으로 범주별 경향석 파악에 용이함.
3) 데이터의 트렌드 판단 가능
4) 연속형 변수 간 단위 표준화가 이루어지기 전의 데이터로 시각화할 경우 파악이 어려울 수 있음.
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from pandas.plotting import parallel_coordinates
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
data = {
    '범주': ['A', 'B', 'C'] * 50,
    '특성1': np.random.normal(20, 5, 150),
    '특성2': np.random.normal(60, 10, 150),
    '특성3': np.random.normal(30, 3, 150),
}
df = pd.DataFrame(data)
print(df)

# 평행좌표
plt.figure(figsize=(12, 6))
parallel_coordinates(df, '범주', color=('#FF9999', '#00FF00', '#0000FF'))
plt.title('평행 좌표 그래프')
plt.show()
