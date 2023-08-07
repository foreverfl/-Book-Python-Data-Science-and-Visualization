import pandas as pd
from tabulate import tabulate
import requests
import json


def get_auth_key():
    with open('04_Date Manipulation/auth_key.txt', 'r') as f:  # 파일 작업이 끝나면 자동으로 닫음
        return f.read().strip()  # 문자열의 앞뒤에 있는 공백 문자 제거


# 각 컬럼의 최대 길이를 기반으로 헤더의 크기를 조정하는 함수
def adjust_headers(dataframe, additional_padding=10):
    adjusted_headers = {}
    for col in dataframe.columns:
        padding = additional_padding
        adjusted_headers[col] = " " * padding + col + " " * padding
    return adjusted_headers


auth_key = get_auth_key()  # API 인증키


# API 호출을 위한 Base URL
url = 'http://apis.data.go.kr/B551177/StatusOfPassengerWorldWeatherInfo/getPassengerDeparturesWorldWeather'
params = {'serviceKey': auth_key, 'numOfRows': '10', 'pageNo': '1', 'from_time': '0000',
          'to_time': '2400', 'airport': '', 'flight_id': '', 'airline': '', 'lang': 'K', 'type': 'json'}

response = requests.get(url, params=params)
response_text = response.content.decode('utf-8')  # 바이트 데이터를 문자열로 변환
data = json.loads(response_text)  # 문자열을 딕셔너리로 변환
print(json.dumps(data, indent=4, ensure_ascii=False))

items = data['response']['body']['items']  # 필요한 항목 추출

# 필요한 항목들을 담을 빈 리스트
airlines = []
flight_ids = []
airports = []
temps = []
senstemps = []

# 항목들 추출하여 리스트에 추가
for item in items:
    airlines.append(item['airline'])
    flight_ids.append(item['flightId'])
    airports.append(item['airport'])
    temps.append(item['temp'])
    senstemps.append(item['senstemp'])

# 추출한 데이터로 DataFrame 생성
df = pd.DataFrame({
    'Airline': airlines,
    'Flight ID': flight_ids,
    'Airport': airports,
    'Temperature': temps,
    'Sensetemp': senstemps
})

adjusted_headers = adjust_headers(df)
adjusted_df = df.rename(columns=adjusted_headers)

print(tabulate(adjusted_df, headers='keys',
      tablefmt='pretty', showindex=False))  # 데이터 출력

# ref: https://www.data.go.kr/data/15095086/openapi.do
