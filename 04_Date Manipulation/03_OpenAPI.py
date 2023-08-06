import pandas as pd
from tabulate import tabulate
import requests
import json


def get_auth_key():
    with open('03_Date Manipulation/auth_key.txt', 'r') as f:
        return f.read().strip()


# API 인증키 입력 (본인의 인증키로 대체해주세요)
auth_key = get_auth_key()

# API 호출을 위한 Base URL
url = 'http://apis.data.go.kr/B551177/StatusOfPassengerWorldWeatherInfo/getPassengerDeparturesWorldWeather'
params = {'serviceKey': auth_key, 'numOfRows': '10', 'pageNo': '1', 'from_time': '0000',
          'to_time': '2400', 'airport': '', 'flight_id': '', 'airline': '', 'lang': 'K', 'type': 'json'}

response = requests.get(url, params=params)

# 바이트 데이터를 문자열로 변환
response_text = response.content.decode('utf-8')

# 문자열을 딕셔너리로 변환
data = json.loads(response_text)

# 필요한 항목 추출
items = data['response']['body']['items']

# 필요한 항목들을 담을 빈 리스트 생성
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

# None 값을 '-'로 대체
df.fillna('-', inplace=True)

pd.set_option('display.max_colwidth', 1)

# 데이터 출력
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

# ref: https://www.data.go.kr/data/15095086/openapi.do
