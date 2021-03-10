import random

ans = random.randint(1,100) # 1~100사이의 랜덤한 숫자를 뽑아줌
print(ans)

print("-----업 다운 게임을 시작합니다-----")
cnt = 0

while True :
    num = int(input("몇번이게? >>"))
    cnt+=1
    if num == ans:
         print("{}회 만에 정답!".format(cnt))
         break
    elif num > ans:
        print("Down")
    else:
        print("UP")

