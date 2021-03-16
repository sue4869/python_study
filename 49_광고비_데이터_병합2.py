#49_광고비_데이터_병합을 반복문으로 쓴것 -------------------
import pandas as pd

company = ["LG전자","삼성전자","현대자동차"]
df_merge = pd.DataFrame()

for i in company:
    df = pd.read_excel("./엑셀데이터/2017년_광고비_{}.xlsx".format(i))
    df.set_index("date",inplace = True)
    df_merge["{}".format(i)] = df["total"]
print(df_merge)
#---------------------------------
#새로운 엑셀에 파일에 넣을 것
df_merge.to_excel("./2017년_광고비_병합.xlsx")