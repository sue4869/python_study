from bs4 import BeautifulSoup
import urllib.request as req

print("====국가선택====")
print("1.미국")
print("2.일본")
print("3.유럽")
print("4.중국")
menu = int(input("번호 선택 >> "))
unit = ["달러","엔","유로","위안"]
user_price = int(input("금액 입력(단위 : {} >> ".format(unit[menu-1]))) #사용자가 입력한 금액
if menu == 2:
    # user_price = user_price / 100
    user_price /= 100
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code,"html.parser")
price = soup.select("span.value") # 환율
#print(int(price[menu-1].string) * user_price) # 우리가 필요한 환율 * 사용자가 입력한 금액
                                              # 숫자 사이에 , 가 있으면 문자열에서 숫자형으로 변환 안된다
                                              # 1,865.00
print("환전 결과 : {}원" .format(float(price[menu-1].string.replace(",","")) * user_price)) # int : 정수형
                                                              # float : 실수형 1865.00도 실수형
