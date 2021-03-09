#유튜브 댓글은 마우스를 이용해 스크롤을 내려야 해서 크롤링하기 쉽지 않다

from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://www.youtube.com/watch?v=BACal2A9zZw")
time.sleep(5) # 무거운 유튜브동영상을 불러오는데 시간이 걸리니까 시간 지연 필요

browser