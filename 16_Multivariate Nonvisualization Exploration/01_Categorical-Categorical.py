"""
- 범주형 - 범주형
* 모자이크 플롯
1) 두개 범주형 변수 내 범주 별 조합의 빈도 크기를 개략적으로 파악
2) 범주 그룹 간 비중의 차이를 전체적으로 파악 가능.
3) 범주 수가 많고, 각 조합별 비중 차이가 크지 않을 경우 전체적 파악이 어려울 수 있음.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from statsmodels.graphics.mosaicplot import mosaic

# 컴퓨터 내의 모든 폰트를 확인
# font_list = [(f.name, f.fname) for f in fm.fontManager.ttflist]
# font_list = sorted(font_list, key=lambda x: x[0])

# for font in font_list:
#     print(f"이름: {font[0]}, 경로: {font[1]}")
    
# 폰트 찾기
font_list = [(f.name, f.fname)
             for f in fm.fontManager.ttflist if 'Gulim' in f.name]
print(font_list)

if len(font_list) > 0:
    plt.rcParams['font.family'] = font_list[0][0]
else:
    print("Gulim 폰트가 설치되어 있지 않습니다.")

# 샘플 데이터 생성
data = {
    '성별': ['남자', '남자', '여자', '남자', '여자', '여자', '남자', '여자'],
    '제품': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'A']
}
df = pd.DataFrame(data)

# 모자이크 플롯 그리기
mosaic(df, ['성별', '제품'])
plt.show()
