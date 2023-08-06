"""
- graph_objects: 데이터 시각화 모듈.
* 과정
1) fig = go.Figure()
2) fig.add_traces(graph)
3) fig.update_layout(option)
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 선 그래프 데이터 생성
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

# 막대 그래프 데이터 생성
x2 = ['A', 'B', 'C', 'D']
y2 = [10, 11, 12, 13]

# 서브플롯 객체 생성
fig = make_subplots(rows=2, cols=1)

# 각 그래프 추가
fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines+markers'), row=1,
              col=1)  # mode='lines+markers'는 그래프가 선과 마커(점) 모두를 표시
fig.add_trace(go.Bar(x=x2, y=y2), row=2, col=1)

# 그래프 표시
fig.show()
