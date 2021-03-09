#로그인을 하고 들어가면 BeautifulSoup로 크롤링을 할 수 없다
#1. 모듈 새로 설치 :pip install selenium -> 웹브라우져를 원격조정하는 모듈
#2.크롬에서 크롬드라이버 다운 - 크롬브라우져 버전 확인 방법 : chrome 정보 확인
#3. 다운받은거 파이참에 붙여넣기

from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe") #브라우져 창키기
# url이용하여 다음 사이트의 로그인 웹페이지로 이동시키기
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")


# 사용자가 마치 직접 아이디와 비밀번호 입력한것처럼 코딩
# id 입력 - id칸 위치 알려줘야함
id = browser.find_element_by_css_selector("input#id")# 아이디칸의 css 선택자 확인해야함. 태크명생략하고 #id라고만 써줘도 됨
id.send_keys("sue4869")#컴퓨터가 타이핑을 해준다         # 태그명이 input인 요소만 해당
# pw 입력
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("yjs815923!")
#로그인 버튼 클릭
browser.find_element_by_css_selector("#loginBtn").click() # 버튼위치지정.click()
time.sleep(3) # 로그인을 클릭한 후 크롬 브라우져가 로그인 될때까지 3초 기다림. 파이썬 빨라서 넣어야 함

# 이메일함으로 이동 - url이용하기
browser.get("https://mail.daum.net/")
time.sleep(2)

# 이메일 제목 크롤링 - bs4와 달리 selenium 은 한단계만 거친다
# 원하는 요소 가져오게 하기 #browser.find_element_by_css_selector() ----> bs4의 select_one과 같은 기능
                        #     ~      _elements_       ~         ----> select()
#title 변수는 리스트 자료형
title = browser.find_elements_by_css_selector("strong.tit_subject") # F12 >> ctrl+shift+c 누르면 요소확인 가능
for i in title:
    print(i.text) #요소 내용 데려오기
browser.close()

#selenium 단점 - 1) 많이 느리다. 2)time.sleep 문제
#selenium 장점 - bs4로 크롤링 못하는 곳들 전부 크롤링 가능
