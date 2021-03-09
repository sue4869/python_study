for i in range(100):
    if i%2 == 1:
        continue # 이로써 홀수는 출력이 안된다
    print(i)
    if i == 20:
        break