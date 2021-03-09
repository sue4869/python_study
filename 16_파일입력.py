#파일 열기모드
# r모드 : 읽기모드. 파일속에 입력해놓은 것을 읽는다
#       : 파일이 존재하지 않으면 에러!

f = open("./test.txt","r", encoding= "utf-8") # 혹시 에러나오면 encoding= "utf-8" 을 추가로 써준다. -> 한글이라 에러
result = f.read()
f.close()
print(result)