#터틀런
import turtle as t
import random

joker = t.Turtle()
joker.shape("turtle")
joker.color("red")
joker.speed(0)
joker.up()
joker.goto(0,200)

food = t.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0,-200)


def turn_right(): #오른쪽으로 방향을 바꿔준다
    t.setheading(0) #바라보는 각도. 머리방향 각도
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    #악당거북이가 주인공 거북이를 쫓도록 설정하기
    ang = joker.towards(t.pos()) # towards() : 특정 방향으로 향하는 각도를 구하기 원할경우  사용
                                 # pos() : 현재 거북이의 좌표를 알려준다
    joker.setheading(ang)
    joker.forward(9)
    if t.distance(food) < 12:
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,230)
        food.goto(star_x,star_y)
    if t.distance(joker) >= 12:
        t.ontimer(play,100) #일정 시간이 흐른 후에 정해진 함수를 실행하는 타이머 기능
                            #게임 플레이중이면 0.1초 후 play함수 실행

t.setup(500,500) #화면 크기 설정 (너비,높이)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.listen() #거북이 그래픽 창이 키보드 입력을 받도록 한다
play()
t.mainloop() #창이 닫치지 않도록 함
             #없으면 컴퓨터가 할일 끝나면 자동으로 창이 닫힘.