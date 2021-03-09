#num = 1
#while num <= 100:
#    print("Hello World")
#    # num = num + 1
#    num += 1

# 나무그림
import turtle

t = turtle.Turtle(shape="turtle")
t.lt(90)

lv = 13
l = 120
s = 17

t.width(lv)
t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

