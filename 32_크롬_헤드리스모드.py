# 다음이메일 크롤링 한 것을 적용
# 크롬 브라우져 창이 띄지 않기 때문에 좀더 빨라지고 깔끔하다.
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("headless") # add_argument : 내가 원하는 옵션들을 넣을 수 있다.

browser = webdriver.Chrome("./chromedriver.exe", options = option)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

id = browser.find_element_by_css_selector("input#id")
id.send_keys("sue4869")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("yjs815923!")

browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)


browser.get("https://mail.daum.net/")
time.sleep(2)

title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)
browser.close()

