#API : application programing interface - 프로그램과 코딩을 이어준다. # 개발자 - 지도 API - 맛집 지도 서비스
#UI : User interface - 사용자와 제품을 연결지어준다

# 구굴: openweatherMap --> 날씨 api에서 apikey 받기
# 885cdc0fb0afb8aaa6b19aaacb5f1467
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


import requests
import json
api_key = "885cdc0fb0afb8aaa6b19aaacb5f1467"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul", api_key)
data = requests.get(url)# 보통의 api사이트들이 get방식으로 요청하게 되어있다.
result = json.load(data.text)#.text를 써야지 api를 받을 수 있다. -->json.load : json표현을 딕셔너리 자료형으로 변환
print(result["name"])
print(result["weather"][0]["main"]) #result["weather"]:리스트자료형으로 나온다. 인덱스번호 존재
                            # 인덱스 번호를 쓰니 result["weather"][0] --> 그 안의 딕셔너리가 나온다.
                            # result["weather"][0][main] --> 이제서야 현재 날씨 알수 있다

#데이터 표현 형식
#1.CSV (Comma Seperated Values) -> 모든 값을 , 로 구분 ex) 사과,배,포도 100,200,300
#2.json ex) {"사과":100, "배":200, "포도":300}

#크롤링 코드 짜기 전. Api 있는 지 확인 할것

