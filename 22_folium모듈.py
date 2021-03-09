import folium
# location이라느 함수에 위도경도 좌표 값 제시
map = folium.Map(location=[37.610620466878494, 127.05636008294118],zoom_start=17) #zoom_start:얼마나 확대
map.save("./map.html")

# 탐색기: show in explorer >> 위의 파일 찾기