#유튜브 댓글은 마우스를 이용해 스크롤을 내려야 해서 크롤링하기 쉽지 않다

from selenium import webdriver
import time
from selenium.webdriver .common.keys import Keys #.send_keys() 쓸때 불러와야하는 모듈

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://www.youtube.com/watch?v=BDwbfPBm8ng")
time.sleep(5) # 무거운 유튜브동영상을 불러오는데 시간이 걸리니까 시간 지연 필요

# 스크롤 살짝 내려서 댓글 생성시키기
#.send_keys(): 키보드로 무언가를 타이핑시키고 싶을 때 사용
# --> HTML요소가 앞에 붙여져야 한다. 여기서는 모든 HTML에 있는 태그 <html쓴다
# find_element_by_css_selector() : html요소를 가져오는 함수
#.PAGE_DOWN:스크롤 살짝 내린다.

#browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)

#스크롤 끝까지 내려야만 댓글 생성되는 경우 --> Keys.END
browser.find_element_by_css_selector("html").send_keys(Keys.END)
time.sleep(4)

comments = browser.find_elements_by_css_selector("#content-text") #리스트자료형
idx = 0
while True:
    try:
        print(comments[idx].text) # comments[idx]: 처음에 리스트 자료형의 0번째 원소를 꺼내오기 시작
    except: #에러가 날경우 이 문장을 출력해라
        print("===== 크롤링 완료! =====")
    idx +=1
    if idx % 20 ==0: #idx가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        # 그 다음 댓글들은 스크롤 끝까지 내려야만 다음 댓글 20개 새롭게 나온다.
        comments = browser.find_elements_by_css_selector("#content-text") #새로운 댓글 재크롤링