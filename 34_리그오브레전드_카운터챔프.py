#웹페이지마다 url주소가 같은 경우 bs4보다 selenium이 좋다

from selenium import webdriver
import time

your_champ = input("상대가 고른 챔프 입력 >> ")

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.op.gg/champion/statistics")
time.sleep(3)

champs = browser.find_elements_by_css_selector("div.champion-index__champion-item__name")
for i in champs:
    if i.text == your_champ:
        i.click() #요소를 클릭하게 된다
        time.sleep(3) #클릭하면 웹페이지 이동하니 기달
        break

#카운터 메뉴 클릭
browser.find_element_by_css_selector("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a").click()
# 꼭 .click 써주기
time.sleep(2)

#카운터 챔프 크롤링
counter = browser.find_elements_by_css_selector("div.champion-matchup-list__champion > span:nth-child(2)")
# nth-child(2) : 자손 중에 2번째에 위치한 자손

for i in counter:
    print(i.text)

browser.close()

