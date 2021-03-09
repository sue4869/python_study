foo = input("문자열을 입력해주세요 >>")
print(len(foo))
#문자열 함수는 "변수이름.함수()" 형태
print("엑셀보다 쉬운 \"파이썬\"")

a = input("입력>> ")
print("{}".format("="*30) +a+"{}".format("="*30) )
print("{0:=^68}".format(a))
print("="*30 + a + "="*30)

a = input("입력>> ")
print(a[-1])

a = input("현재 년도>> ")
b = input("현재 월>> ")
c = input("현재 일>> ")
d = input("현재 요일>> ")
print("{}년 {}월 {}일 {}요일".format(a,b,c,d))

a = input("입력>> ")
print(a.replace(" ","\n"))

data = [1,2,"가나다",2.3,[5,6,7,8,"홍길동"]]
print(data[4][4]) #리스트 속의 리스트 원소 불러오기


