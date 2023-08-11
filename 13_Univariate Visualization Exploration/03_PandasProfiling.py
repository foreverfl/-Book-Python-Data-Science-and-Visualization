"""
- Pandas Profiling: 데이터프레임에 대한 탐색적 데이터 분석을 빠르게 수행하는 도구.
* Pandas Profiling을 사용하면 데이터의 전반적인 구조, 각 변수의 통계량, 결측치, 상관관계, 히스토그램 등 많은 정보를 한 번에 얻을 수 있음.
* 이는 초기 데이터 분석 단계에서 데이터에 대한 이해를 빠르게 돕는데 매우 유용함.
"""

import pandas as pd
from pandas_profiling import ProfileReport

# 예시 데이터프레임 생성
data = {
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'b': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'c': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
}
df = pd.DataFrame(data)

# Pandas Profiling Report 생성
profile = ProfileReport(df, title="Pandas Profiling Report")

# Report를 HTML 파일로 저장
profile.to_file("report.html")
