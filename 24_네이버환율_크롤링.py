from bs4 import BeautifulSoup
import urllib.request as req

# 1.css선택자를 더 자세히 작성하는 방법으로 내가 원하는 것만 출력
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code,"html.parser") # html 분석
price = soup.select("ul#exchangeList span.value") # 원하는 데이터 추출
for i in price:
    print(i.string)


## Html
# class속성값은 중복가능
# id 속성값은 고유요소이다

##css 선택자
# " . " --> 속성명이 class
# "#＂--> 속성명이 id
# " " 공백 --> 후손(조부모)
# " > " --> 자손(부모)