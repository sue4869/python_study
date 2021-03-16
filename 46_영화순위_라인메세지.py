#23_CGV_영화예매순위활용 + 포스터 이미지 가져오기
#단톡방에 알림 가게 하겠다. --> 라인앱에 그룹만들기(반드시 line Notify 추가시켜야함) 단독방 이름 :파이썬봇
# line Notify api >> 로그인 >>마이페이지 >> generate token >> 파이썬 봇 클릭 > token 복사
#hT0r5nbSPT3ihcWyO1Oh2ztwnI6Pf7SnoMrFK4aZr07

import urllib.request as req
from bs4 import BeautifulSoup
import requests

##서버에게 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/") #ctrl 누르고 url주소 누르면 들어가진다
soup = BeautifulSoup(code, "html.parser")
title = soup.select("strong.title")
img = soup.select("span.thumb-image > img")


headers = {'Authorization':'Bearer hT0r5nbSPT3ihcWyO1Oh2ztwnI6Pf7SnoMrFK4aZr07'}#라인 API token 변경
for i in range(len(title)):
     print(title[i].string)
     print(img[i].attrs["src"])
     data = {"message":"{}위 : {}".format( i+1, title[i].string),
             "imageThumbnail":img[i].attrs["src"],
             "imageFullsize":img[i].attrs["src"]} # 영화제목 보내기
     requests.post(" https://notify-api.line.me/api/notify", headers=headers, data=data)
     print()
     if i == 4 : # 1~5위까지만 출력시키기
         break





