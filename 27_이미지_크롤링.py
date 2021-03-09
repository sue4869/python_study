import urllib.request as req
from bs4 import BeautifulSoup
import os
import  urllib.parse as par #한글을 특수한 문자로 변환

keyword = input("키워드 입력 >> ") #사용자가 검색한 것의 이미지 확보
#특수한 문자로 변환
encoded = par.quote("keyword")

#폴더 만들기
if os.path.exists("./이미지_크롤링") == False: # 현재 폴더안에 제시한 폴더명의 폴더가 존재하는지 확인
    os.mkdir("./이미지_크롤링")               #if not os.path.exists("./이미지크롤링")  과 같은 말
                                            # 존재 : True 무존재 : False

#이미지_크롤링 안에 폴더 만들기
if not os.path.exists("./이미지_크롤링/{}".format(keyword)):
    os.mkdir("./이미지_크롤링/{}".format(keyword))


code = req.urlopen("https://images.search.yahoo.com/search/images;_ylt=Awr9GjBDEUJg71gA8zpXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZANCMjk0NF8xBHNlYwNwaXZz?p={}&fr2=piv-web&fr=yfp-t".format(encoded))
soup = BeautifulSoup(code, "html.parser")
img = soup.select("li > a > img")
cnt = 1
for i in img:
    #print(i.attrs) #attrs : 요소의 속성명과 속성값을 가져온다
                   #string : 요소의 내용
                   # {}로 이루어진것을 보아 딕션어리 자료형이다
    img_url =i.attrs['data-src'] #인덱스 이름을 불러서 url주소를 가져온다
                                 #이미지를 크롤링할때는 요소안에 들어있 는 url주소를 가져와야한다
    req.urlretrieve(img_url,"./이미지_크롤링/{}/{}.png".format(keyword, cnt)) #urlretrieve : 이미지들 다운받는 함수
    print("이미지 크롤링 완료 {}".format(cnt))
    cnt += 1