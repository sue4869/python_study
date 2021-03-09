import turtle as t
import random

t.shape("turtle")
t.speed(100)
color = ["red","blue","green","yellow","purple","orange"]
function_list = [t.forward,t.backward,t.left,t.right,t.dot,t.circle]
while True:
    r = random.randint(0,50) #0~50까지 랜덤 숫자
    t.color(random.choice(color)) # random.choice : 데이터들 중 무작위로 1개 선택하는 함수
    random.choice(function_list)(r)

t.done()