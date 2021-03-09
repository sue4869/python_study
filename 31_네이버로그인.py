# 네이버 셀레니움 로그인
from selenium import webdriver
import pyperclip    # pip install pyperclip 입력하여 모듈 설치! alt + enter + enter
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

def input_id_pw(browser, css, user_input):
    pyperclip.copy(user_input)  # input을 클립보드로 복사
    browser.find_element_by_css_selector(css).click()  # element focus 설정
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # 윈도우 : Ctrl+V 전달
    time.sleep(1)


browser = webdriver.Chrome('./chromedriver')

browser.get("https://nid.naver.com/nidlogin.login")

input_id_pw(browser, "#id", "sue4869")
time.sleep(1)
input_id_pw(browser, "#pw", "dbtnals0312!")
time.sleep(1)

browser.find_element_by_css_selector("#frmNIDLogin > fieldset > input").click()
time.sleep(3)
