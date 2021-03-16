import pandas as pd
from pandas import ExcelWriter #시트별로 나눠주라고 했는데 안됨 엑셀 기능이 없어서 그럼
                               #엑셀을 좀더 디테일하게 제어할 엔진 가져오기

writer = ExcelWriter("./장사시설_병합.xlsx") #위에 엔진과 같이 추가시킴
for year in range(2017,2021): #2017~2020까지 가져온다
    #여러개의 sheet중 원하는 시트만 꺼내려고 할때, 끝에 시트이름 붙여넣기
    df = pd.read_excel("./엑셀데이터/장사시설현황_2017년_2020년/{}년 장사시설 현황/전국장사시설현황.xlsx".format(year),sheet_name="장례식장 시설정보")
    # 두개의 데이터열을 가져올때, 여기서는 시설명,
    df = df[["시설명","주소"]]#2개이상의 열을 가져오려면 리스트자료형으로 넣는다,꼭 []한번 더!!
    #df.to_excel("./장사시설_병합.xlsx", sheet_name="{}년".format(year))
    df.to_excel(writer, sheet_name="{}년".format(year))
    print("{}년 데이터 병합 완료".format(year))
writer.save()
