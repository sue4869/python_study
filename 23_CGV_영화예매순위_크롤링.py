import urllib.request as req # urllib.request 모듈 : 웹페이지의 HTML 소스코드를 들고오도록 도와주는 함수가 들어있다
from bs4 import BeautifulSoup # BeautifulSoup 모듈 불러오기

##서버에게 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

##HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser") # 이 함수는 어떤 언어도 다 가능해서 HTML지정해줘야함
#print(soup)                              # HTML을 해석할 수 있는 전용 번역가

##내가 원하는 요소 찾게 하기
# title = soup.select_one("ol div.box-contents > a > strong.title")
# #print(title)
# title2 = soup.select_one("") #2.3.4등의 속성요소가 다 똑같다
# title3 = soup.select_one("")
# title4 = soup.select_one("")
# # select_one : 요소 하나만 가져옴. 필요한 정보의 요소위치를 css 선택자를 이용해 알려줌

title = soup.select("strong.title")#요소 여러개 한번에!

#요소의 내용만 출력하기 : .string
##print(title.string) # .string: html요소를 가지고 있는 변수 뒤에만 쓸수 있다
                      # title : 그냥 리스트 자료형만 존재

for i in title:      #여러개 요소들이 리스트 자료형 형태로 불러와진다. 리스트 --> for문
    #print(i)        # i를 출력하면 리스트 자료형의 요소를 하나씩 빼와진다. 태그명.속성값등 다 출력
     print(i.string) #요소 내용만 출력됨