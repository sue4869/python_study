import pandas as pd

df = pd.read_excel("./엑셀데이터/전자기기매출액.xlsx") #pandas라는 모듈은 dataframe 자료형으로 값을 받음
#print(df) # 엑셀 값들 출력
df[::2].to_excel("./전자기기매출액_홀수행삭제.xlsx", index=None) #홀수행 삭제한 상태의 엑셀파일 저장됨
                                                            #index=None: 쓸데없이 들어간 인덱스 지워짐