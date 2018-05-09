#값을 입력받아 도형을 그리기

import turtle
t = turtle.Turtle()

s = turtle.textinput("","몇각형을 원하시나요?:")
n = int(s)

for i in range(n):
    t.forward(30)
    t.left(360/n)
