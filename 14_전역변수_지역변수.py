#1
def func1():
    a = 1 # 지역변수 : 함수 안에서 만들어진 변수
          # 함수 안에서만 접근 가능
func1()
print(a) # 접근할 수 없으니 에러

#2
num = 10 # 전역변수 : 함수 밖에서 만들어진 변수
         # 모든 지역에서 접근 가능 (read-only: 값의 수정불가)
def func2():
    global  num # num 변수 값 수정 허락맡기 : global 명령어
    num += 1 # 위에 줄 안쓰면 에러뜬다 (read-only: 값의 수정불가)
    print(num)

#lambda

def sum(a,b):
    return a+b
result = sum(10,20)

#위에 것을 간단히
result = lambda a, b: a+b