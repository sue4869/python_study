#로그인이 필요한 웹페이지에서도 bs4를 쓸수 있다 >>import requests  모듈 사용
#로그인페이지 > 검사 > Network > 아이디비밀번호를 써놓은 상태로 두기 >>preserve log 채크한 후 All버튼 누른후 >> 로그인 버튼 누르기
#id : talingpython pw : 탈잉파이썬2(영어로)
#서버와 통신한 기록을 볼수 있다

#요청방식 1) get 방식: 쪽지 방식(보안성 취약, 적은 내용) 2)post 방식 : 택배 방식(보안성 G, 많은 내용가능)
#로그인을 하기위에 서버와  통신한 기록 : trans_exe.php >> Request Method (headers)--> post가 로그인을 할때 서버와 통신한 기록

from bs4 import BeautifulSoup
import requests

#로그인
sess = requests.session()

#request Header >> referer : 로그인 웹페이지에서 왔다는 정보
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19940311%26mode%3D19940311%2F0001885179%2F1"}
#Form Data >> gourl
post_data ={"gourl":"https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19940311%26mode%3D19940311%2F0001885179%2F1"
,"bid": "talingpython"
,"bpw": "xkfdldvkdlTjs2"}
#택배 post는 딕션어리 자료형으로 넣어줘야 한다.
#택배에 어떤 정보를 넣었나? 택배상자 표현 : Form Data 에 내가 친 아이디와 비밀번호 있다
#gourl : 내가 로그인에 성공했을때 받고 싶은 주소
# 복사해서 {}안 넣는다. 단어를 문자열로 한번에 --> 단어 더블클릭 + "" 버튼
#요청상대인 서버주소를 넣은다 검사 > Header >> Request url
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=h, data=post_data)


# # 뉴스기사 본문 하나 크롤링
# # req.urlopen() : 이거 쓰면 로그인상태 취소된다 ---> sess.get() 사용
# code = sess.get("https://www.donga.com/archive/newslibrary/view?idx=19770310%2F0000216858%2F1") #검사>>network>>request url
# soup = BeautifulSoup(code.text, "html.parser") # get함수는 urlopen함수와 다르게 .text를 붙여줘야 한다
# content = soup.select_one("div.article_txt") #기사 본문#
# print(content.text)

# 뉴스기사 본문 여러개 크롤링

# 뉴스 기사제목 요소들 가졍오기
#로그인 상태 유지 # 웹브라우져 주소
code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19940311&mode=19940311/0001885179/1")
soup = BeautifulSoup(code.text, "html.parser")
a = soup.select("ul.news_list a")
for i in a:
    #onclick의 속성의 해당부분을 빈부분으로 바꿔라
    #원래 i.attrs["onclick"] 의 결과로 avascript:getNewsArticle('19940311/0001885179/1'); return false; 나온다.
    article_num = i.attrs["onclick"].replace("javascript:getNewsArticle('19940311/", "").replace("/1'); return false;","")
    # network>>request url
    url = "https://www.donga.com/archive/newslibrary/view?idx=19940311%2F{}%2F1".format(article_num)
    code = sess.get(url)
    soup = BeautifulSoup(code.text, "html.parser") # get함수는 urlopen함수와 다르게 .text를 붙여줘야 한다
    content = soup.select_one("div.article_txt") #기사 본문#
    print(content.text)

# bs4 크롤링 시도 -> 근데 안되네? -> selenium으로 갈아탐.
# ===> 크롤링 속도를 높이고 싶다 -> requests모듈, bs4모듈 + 웹사이트 분석