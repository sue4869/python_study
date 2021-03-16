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
#가입인사 게시판 클릭
#웹페이지안의 또다른 프레임이 존재 :iframe
#따라서 프레임 전환을 해야함
browser.switch_to.frame(browser.find_element_by_css_selector("#down"))
browser.find_element_by_css_selector("#fldlink_lF1R_309").click()
time.sleep(3)
#글쓰기 버튼 클릭
browser.find_element_by_css_selector("#article-write-btn").click()
time.sleep(3)
#제목 작성
subject= browser.find_element_by_css_selector("#title-input")
subject.send_keys("안녕하세요")
#본문 작성 #프레임전환
browser.switch_to.frame(browser.find_element_by_css_selector("#keditorContainer_ifr"))
content= browser.find_element_by_css_selector("#tinymce")
content.send_keys("하이하이하이")
#글 등록 버튼 클릭 #프레임 전환 # 안에서 밖으로 전환 불가능 --> 젤 밖으로 나가서 안으로 들어가기
browser.switch_to.default_content()# 젤 밖 프레임으로 나가는 것
browser.switch_to.frame(browser.find_element_by_css_selector("#down"))
browser.find_element_by_css_selector("button.btn_g.full_type1").click()
time.sleep(3)
browser.close()

#No such element 에러 해결법
#1)css선택자를 정확하게 잘 작성했나 확인
#2)time.sleep()을 더 길게 조정
#3)프레임 안에 들었나 확인 --> <html이 중간에 있고, 위에 ifame확인 --> 프레임 전환 코드 넣어주기

#정해진 시간에 프로그램 작동하게 하기
#작업 스케줄러 --> 기본 작업만들기 -...-> 프로그램/스크립트 : venv >>script>>python.exe 경로 복사 넣기
#                                    인수 추가 : 돌릴 프로그램 경로 복사해서 붙여넣기 : 다음카페_자동글게시
#                                    시작 위치 : 돌릴 프로그램을을 담고 있는 폴더 경로 : python_study