#LG전자,삼성,현대자동차 회사들 각각의 total들을 새 엑셀파일에 병합
import pandas as pd

#새 회사 데이터를 합칠 빈 엑셀파일 만들기
df_merge = pd.DataFrame()

#LG전자
df = pd.read_excel("./엑셀데이터/2017년_광고비_LG전자.xlsx") #해당 엑셀파일 우클릭 >> copy >> path from content Root
df.set_index("date",inplace = True)#인덱스 번호 대신 날짜를 넣고 싶음
# df = df.set_index("date") --> 윗줄과 같은 말, inplace = True의 역활 확인
#print(df["total"]) # 먼저 윗줄에서 인덱스 지정한 후, 원하는 데이터 헤더의 이름만 가져오면 된다
df_merge["LG전자"] = df["total"] #LG전자의 total을 df_merge의 LG전자 열에 넣는다
                                #빈 엑셀 파일에서 LG전자라는 이름의 열이 없으면 만들어줌

#삼성전자
df = pd.read_excel("./엑셀데이터/2017년_광고비_삼성전자.xlsx")
df.set_index("date",inplace = True)
df_merge["삼성전자"] = df["total"]

#현대자동차
df = pd.read_excel("./엑셀데이터/2017년_광고비_현대자동차.xlsx")
df.set_index("date",inplace = True)
df_merge["현대자동차"] = df["total"]

# 반복문 써야할듯???