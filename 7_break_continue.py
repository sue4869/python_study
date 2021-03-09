# num = 0
# while True: #무한 루프
#     num += 1
#     if num % 2 == 1: # 만약 num이 홀수라면?
#         continue # 반복문의 조건부 문장으로 돌려보냄 즉 print문장으로 안가고 조건문으로 간다
#     print(num)
#     if num == 20 : # == : 양쪽 값이 같냐? 비교연산자
#         break # 반복문(while문)을 강제 탈출시킴

# sum = 0
# while True:
#     number = int(input('돈을 저금하세요.(0 누르면 종료):'))
#     if number == 0:
#         while True:
#             print("현재까지 저금한 돈 : {}원".format(sum))
#             print("종료합니다")
#             break
#             #다중 들여쓰기 : tab
#     sum = sum + number

# 가져온_물건들 = ["생선","상한 달걀","우유","두부","상한고기","소시지", "상한 고등어","돼지고기"]
# 상한물건개수 = 0
# for 물건확인 in 가져온_물건들:
#     if 물건확인[:2] == "상한": #글자중에서 앞에 두글자에 상한이 존재하면
#         상한물건개수 += 1
#         print("{}: 불량!!!".format(물건확인))
#         continue
#     if 상한물건개수 ==3:
#         print("돌려보내!!")
#         break
#     print("{} : 양호~~".format(물건확인))


result = []
for num in [1,2,3,4,5,6]:
    result.append(num*2)

result = [num*2 for num in [1,2,3,4,5,6]]

result = []
for num in [1,2,3,4,5,6]:
    if num%2 == 0:
        result.append(num)
result = [num for num in [1,2,3,4,5,6] if num%2 == 0]