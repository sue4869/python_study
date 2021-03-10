#로그인이 필요한 웹페이지에서도 bs4를 쓸수 있다 >>import requests  모듈 사용
#로그인페이지 > 검사 > Network > 아이디비밀번호를 써놓은 상태로 두기 >>preserve log 채크한 후 All버튼 누른후 >> 로그인 버튼 누르기
#id : talingpython pw : 탈잉파이썬2(영어로)
#서버와 통신한 기록을 볼수 있다

#요청방식 1) get 방식: 쪽지 방식(보안성 취약, 적은 내용) 2)post 방식 : 택배 방식(보안성 G, 많은 내용가능)
#로그인을 하기위에 서버와  통신한 기록 : trans_exe.php >> Request Method (headers)--> post가 로그인을 할때 서버와 통신한 기록

from bs4 import BeautifulSoup
import requests

sess = requests.session()

#request Header >> referer : 로그인 웹페이지에서 왔다는 정보
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19770310%26mode%3D19770310%2F0000216854%2F1"}
post_data ={"gourl":" https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19770310%26mode%3D19770310%2F0000216854%2F1"
,"bid": "talingpython"
,"bpw": "xkfdldvkdlTjs2"}
#택배 post는 딕션어리 자료형으로 넣어줘야 한다.
#택배에 어떤 정보를 넣었나? 택배상자 표현 : Form Data 에 내가 친 아이디와 비밀번호 있다
#gourl : 내가 로그인에 성공했을때 받고 싶은 주소
# 복사해서 {}안 넣는다. 단어를 문자열로 한번에 --> 단어 더블클릭 + "" 버튼
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=h, data=post_data)#요청상대인 서버주소를 넣은다 검사 > Header >> Request url

# req.urlopen() : 이거 쓰면 로그인상태 취소된다 대신 sess.get() 사용
code = sess.get("https://www.donga.com/archive/newslibrary/view?idx=19770310%2F0000216858%2F1") #검사>>network>>request url
soup = BeautifulSoup(code.text, "html.parser") # get함수는 urlopen함수와 다르게 .text를 붙여줘야 한다
content = soup.select_one("div.article_txt") #기사 본문#
print(content.text)