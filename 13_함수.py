def add(a,b): # def를 만나는 순간 인터프터는 번역 스킵해서 # 2.(10,20)을 가져옴
    c = a+b
    return c

result = add(10,20) # 1.인터프리터 번역 시작 . add함수로

#예제1
def STRING():
    str = "Hello, World!"
    return str

result = STRING()
print(result)

