# 따릉이 위치를 지도에 시각화하고 싶다

import requests
import json
import folium # 지도 모듈
import os
from selenium import webdriver #path를 실행하기 위해서 불러줘야 한다.

api_key = "50596b527a737565373177524f5967" #서울시따릉이에서 api키 받기
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/100/".format(api_key) #url에서 {}로 바꾸고 5를 100으로 바꿈
data = requests.get(url)# 서울시따릉이 샘플 url
#print(data.text) # .text를 써줘야 안에 있는 데이터를 꺼내서 볼수 있다.
result = json.loads(data.text) #json -> 딕션어리 형태로 바꿔준다 ...이것을 print하면 나오는게 너무 더러워
#print(json.dumps(result, indent ="\t")) # 더럽게 나오는 걸 이쁘게 정리
bikes = result["rentBikeStatus"]["row"]# 따릉이의 위치 데이터 #출력해보면 리스트자료형임을 알수 있다
#지도 만들기 전에 위도, 경도 좌표를 구해 좌표 중심값 구하기
lat_sum = 0
lon_sum = 0
for i in bikes:
    lat_sum += float(i["stationLatitude"])
    lon_sum += float(i["stationLongitude"])
lat_avr = lat_sum/len(bikes)
lon_avr = lon_sum/len(bikes)

map = folium.Map([lat_avr,lon_avr],zoom_start=14)# location : 어떤 위치에 지도를 띄울것이냐
                                                 # zoom_start : 지도를 얼마나 확대해서 보여줄것이냐냐
for i in bikes:
    station_Name = i["stationName"]#대여소이름
    bike_num = int(i["parkingBikeTotCnt"]) #자전거주차총건수 #문자열 -->정수형
    if bike_num < 3: # 주차된 자전거 개수대로 색깔을 바꾸고 싶다
        color = "red"
    elif 3 <= bike_num < 7:
        color = "blue"
    else:
        color = "green"
    lat = float(i["stationLatitude"]) #위도 print[i]를 해보면 위도가 ''로 둘러싸여 문자열 자료형임을 알수 있다 --> 실수형으로 바꿔주기
    lon = float(i["stationLongitude"])#경도 # 문자열 --> 실수형
    folium.Marker([lat,lon], popup=station_Name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map) # folium.Marker() : 지도에 마커를 찍을 수 있다. # folium 모듈 설명서 확인
map.save("./따릉이.html") #파일로 저장

# 브라우져 불러오기
path = os.path.abspath("./따릉이.html") # 이 파일의 전체 경로를 구해줌
browser = webdriver.Chrome("./chromedriver.exe") #html이 기본적으로 브라우져 창에서 실행되니 chrome 브라우져를 불러온다
browser.get(path) # 브라우져 열때의 url
