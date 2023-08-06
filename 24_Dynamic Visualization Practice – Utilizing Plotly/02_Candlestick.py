"""
- Candlestick 차트: 주로 주식의 시가(Open), 최고가(High), 최저가(Low), 종가(Close) 데이터를 사용.
"""

import yfinance as yf
import plotly.graph_objects as go

# Yahoo Finance로부터 Apple 주식 데이터를 가져옴
data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')

# 가져온 데이터 중에서 종가 데이터만을 시각화할 것입니다.
fig = go.Figure()  # 새로운 그래프 객체를 생성합니다.

# Candlestick 그래프에 필요한 데이터를 추가합니다.
fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name='AAPL Candlesticks'))

# 그래프의 레이아웃을 업데이트합니다.
fig.update_layout(title='Apple 주식 종가 (2020)',
                  xaxis_title='날짜', yaxis_title='종가 (USD)')

# 그래프를 출력합니다.
fig.show()
