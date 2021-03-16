#list.xlsx 파일 넣어줌

#네이버 이메일을 보내기 전 설정 : 메일 >> 환경설정 ( 맨 아래 왼쪽 위치) >> POP3/IMAP 설정
#POP3/IMAP사용 :사용함 , 원본저장 : 아무거나 하나, 채크

import openpyxl
import smtplib
from email.mime.text import MIMEText

#이메일을 관리하는 서버에 접속해 로그인함 >> 네이버 이메일 환경설정에 SMTP 포트 : 465, 보안 연결(SSL) 필요
naver_server = smtplib.SMTP_SSL("smtp.naver.com",465) #>> 네이버 이메일 환경설정에 SMTP 포트 : 465, 보안 연결(SSL) 필요
                                                      #>>SSL 써주기
naver_server.login("sue4869","비밀번호")

#이메일 내용 읽어오기
book = openpyxl.load_workbook("./list.xlsx") #해당 엑셀파일 읽어오기
sheet = book.active #활성화 되어있는 시트 불러오기
num = 0

for row in sheet.rows: #시트의 각 행을 변수 row가 가져온다
    # 결제칸에 O로 된 사람에게만 보내기
    if row[4].value == "X":
        continue # 바로 다음 행 가져오기
    date = row[0].value #행의 0번째 칸을 가져온다 #.value를 붙여줘야 셀의 값을 가져온다.
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = "{}님, XX 쇼핑몰입니다".format(name)
    content = """안녕하세요, XX 쇼핑몰에서 결제 완료 안내 메일 보내드립니다.
성함 : {}
구매 날짜 : {}
구매 물건 : {}

감사합니다.
""".format(name, date, product)

#러줄의 문자열을 통채로 보내고 싶을때는 """
#  """개가
#     멍멍
#     짖는다."""
    #이메일 보내기                                  # _charset = "euc-kr" : 한글이 깨지지 않도록
    msg = MIMEText(content, _charset = "euc-kr") #MIMIEText(): 편지봉투같은것
    msg["From"] = "sue4869@naver.com"
    msg["To"] = your_mail
    msg["Subject"] = title

    naver_server.sendmail("sue4869@naver.com",your_mail,msg.as_string())
    print("{}님께 이메일을 보냈습니다".format(name))
    num +=1
    if num % 20 == 0:
        naver_server.quit() #20개씩 보내면 로그아웃 # 너무 많이 보내면 서버차단 당함
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465) #재로그인
        naver_server.login("sue4869", "비밀번호")

