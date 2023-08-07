import pandas as pd
import matplotlib.pyplot as plt
# 시간 그래프(Time Plot): 패턴, 이상치, 시간에 따른 변화, 계절성 등의 데이터의 많은 특징을 눈으로 볼 수 있게 해줌.

# 예제 데이터 생성
data = {
    'Date': pd.date_range(start='2023-07-01', periods=5, freq='D'),
    'Value': [10, 20, 15, 30, 25]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 'Date' 열을 인덱스로 설정
df.set_index('Date', inplace=True)

# 선 그래프 그리기
df.plot()
plt.title('Sample Line Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
