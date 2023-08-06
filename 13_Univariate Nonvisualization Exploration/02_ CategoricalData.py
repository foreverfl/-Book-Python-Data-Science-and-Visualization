"""
- 파이차트
- 막대그래프: 범주별 비교는 막대 그래프 기반의 파악이 비교적 수월함.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 예제 데이터 생성
data = {
    'Fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
    'Count': [45, 30, 15, 10]
}
df = pd.DataFrame(data)

# 파이차트 그리기
plt.figure(figsize=(7, 7))  # 그래프의 크기 설정
# autopct: 조각의 퍼센트 값을 표시
# startangle: 파이 차트의 시작 각도를 90도로 설정함
plt.pie(df['Count'], labels=df['Fruits'], autopct='%1.1f%%', startangle=90)
plt.title('Fruit Count Pie Chart')
plt.show()

# 막대그래프 그리기
plt.figure(figsize=(8, 6))
plt.bar(df['Fruits'], df['Count'], color=[
        'red', 'yellow', 'pink', 'orange'])  # x, y, color
plt.xlabel('Fruits')
plt.ylabel('Count')
plt.title('Fruit Count Bar Chart')
plt.show()
