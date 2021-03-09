num1 = int(input("첫번째 숫자 입력해주세요 >> ")) # int() : 문자열을 정수형으로 바꿔줌
num2 = int(input("두번째 숫자 입력해주세요 >> "))
print("곱셈 결과는 {} 입니다".format(num1*num2))

a = input("입력 >> ")
print(a.split())

a =['유튜브','페이스북','카카오톡']
a.append('인스타그램')
print(a)

Korea = ['독도는','일본','땅']
Korea[1]="한국"
print(Korea)

number = [1,1,1,1,1,1,1,111,1111,1,11,111,11111,1111,11111111,111,11,1,1]
print(number.count(1))

fruits = {"사과":300, "배":500, "포도":700}
print(fruits.values())

a = {"name":"앤트맨","age":35,"height":"10mm","weight":"50g"}
a["height"] = "12m"
a["weight"] = "10ton"
print(a)
