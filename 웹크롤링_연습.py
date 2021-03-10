#역대 로또 번호 수집, 그래프로 띄우기
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

# lotto 변수는 0이 45개가 들어있는 리스트 자료형.
from numpy import arange

lotto = [0 for _ in range(45)]
num =0
f = open("Lotto.txt","a")


while True :
    num +=1
    query = par.quote("로또" + str(num) + "회")#한글을 특수한 문자로 변환
    url = "https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={}".format(query)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    lotto_number = soup.select("#_lotto > div.lotto_wrap > div.num_box > span")
    if len(lotto_number) == 0:
        break

    #수집된 데이터 가공
    print("{}회:".format(num),end="")
    f.write("{}회:".format(num))
    for i in lotto_number:
        if i.string == "보너스번호":
            print("+",end='') #end='' : 출력의 끝을 지정
            continue
        print(i.string, end =" ")
        f.write(i.string + " ")
        #로또 번호의 출현 빈도수를 카운트하는 부분
        lotto[int(i.string)-1] += 1
        print()
        f.write("\n")

import matplotlib.pyplot as plt

x = arange(1,46) # 가로축에 들어갈 데이터
plt.bar(x, lotto, tick_label=x)   # bar() : 그래프를 만들어주는 함수
                                  # 첫번째 매개변수: 가로축의 데이터, 두번째 매개변수: 세로축의 데이터
plt.show()