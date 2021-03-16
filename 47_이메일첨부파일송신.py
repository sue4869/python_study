#47_이메일자동송신에서 첨가

import openpyxl
import smtplib
from email.mime.text import MIMEText #편지봉투
from email.mime.base import MIMEBase #택배상자
from email.mime.multipart import MIMEMultipart # 택배 + 편지
from email import encoders
import os


naver_server = smtplib.SMTP_SSL("smtp.naver.com",465)
naver_server.login("sue4869","비밀번호")

book = openpyxl.load_workbook("./list.xlsx")
sheet = book.active
num = 0

for row in sheet.rows:
    if row[4].value == "X":
        continue
    date = row[0].value
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

    email_content = MIMEMultipart() # 추가 # 젤 큰 상자
    #젤 큰상자에 받는사람, 보내는사람. 제목을 보낼 수 있도록
    email_content["From"] = "sue4869@naver.com" #수정
    email_content["Cc"]="asdfad@naver.com"#참조자 넣고 싶을 때
    email_content["To"] = your_mail #수정
    email_content["Subject"] = title #수정
    msg = MIMEText(content, _charset="euc-kr") #이동
    email_content.attach(msg) #편지봉투 보내기

    path = "./list.xlsx"
    file = open(path, "rb") #read binary file = 0과 1로만 이루어진 파일 # 이진수로만 읽는다
    #-----------택배상자에 첨부파일 넣기---------------
    part = MIMEBase("application","octet-stream") #빈 택배상자 만들기 #그냥 형식
    part.set_payload(file.read()) #빈 택배 상자에 엑셀파일 실어넣기
    encoders.encode_base64(part) #이진수로 된것을 텍스트파일화
    # 첨부파일 보낼때 같이 보내야 하는 약속 코드
    part.add_header("Content-Disposition","attachment; filename=" + os.path.basename((path)))
    #----------------------------------------------
    email_content.attach(part) # 완성된 택배상자를 젤 큰 상자에 편지봉투와 넣기

    # msg.as_string() -> email_content.as_string()
    naver_server.sendmail("sue4869@naver.com",your_mail,email_content.as_string()) #your_mail->
    print("{}님께 이메일을 보냈습니다".format(name))
    num +=1
    if num % 20 == 0:
        naver_server.quit()
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
        naver_server.login("sue4869", "비밀번호")

