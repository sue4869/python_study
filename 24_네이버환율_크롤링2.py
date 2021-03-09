from bs4 import BeautifulSoup
import urllib.request as req

##2.데이터 가공
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code,"html.parser")
price = soup.select("span.value")
cnt = 0
for i in price:
    print(i.string)
    cnt += 1
    if cnt == 4: #데이터 수집된게 4개면 반복 멈춤
        break

# 또다른 방법
for i in price:
    print(i.string)
    if price.index(i) == 3: # 리스트형인 i의 요소들 인덱스가 3이면
        break

#정리 - bs4 이용해서 크롤링하는 방법 순서
#1. 서버로부터 HTML 코드 받아오기 : code = req.urlopen()
#2. HTML코드 이쁘게 정리하기 : soup = BeautifulSoup()
#3. 원하는 요소 가져오게 하기 : soup.select() 또는 soup.select_one()