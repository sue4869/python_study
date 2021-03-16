from selenium import webdriver
import time
import random

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
time.sleep(3)
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")

pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")#카페주소로 이동
time.sleep(3)
#중고나라 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down"))
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(3)
#메모장에 과거의 글제목 저장
try:
    f = open("./중고나라.txt","r") #존재하지 않는 파일이면 에러가 난다.
    ref = f.readline()#각줄을 리스트 자료형으로 저장
except:
    f = open("./중고나라.txt","w") # 존재 하지 않으면 파일을 새로 생성
    ref = []
f.close()
#게시판 제목 크롤링 ( 새로운 글이 올라왔는지 판단 )
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref:#게시글의 제목 # 만약에 i라는 제목이 ref라는 리스트에 없다면 # 새로 올라온 글이라면?
        with open("./중고나라.txt","a") as f: #with ~ as 를 써주면 f.close를 안해도 자동으로 해준다
            f.write(i.text + "\n") #write()함수의 특징 : \n을 직접써줘야 함.
            #f.close()
            if "노트북" in i.text: #in연산자 뒤에 문자열이 들어가면 문자열 중에 그 글자가 들었는지
                new_one +=1

print("{} 관련 글이 {}개 올라왔습니다.".format("노트북",new_one))
browser.close()

# #알고리즘
#새로운 글이 올라왔는지 판단 -> 새로운 글이 "중고 노트북" 관련 글이라면? --> 문자보내기
#메모장에 과거의 글제목들을 넣어놓아 --> 크롤링해서 메모장의 문자열과 비교 --> 메모장의 문장에 없다면

#문자메세지 보내기 #구글에 Twillo 검색 --> 받은 코드 넣기
#+12016032861
#
#

# Download the helper library from https://www.twilio.com/docs/python/install
if new_one >= 1:
    from twilio.rest import Client
    import os



    account_sid = os.environ['AC103c9e010cf423008b428811208bac36']
    auth_token = os.environ['7d39aa0e114f2d1f9d483defd84571ea']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body="{} 관련 글이 {}개 올라왔습니다.https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F".format("노트북",new_one),
             to='+821065394869',
            from_= "+12016032861" #twillo에서 받은 임시 번호

         )
    #항공권 특가 알림#수강신청 프로그램

