# 사용자에게 값을 입력받아 음수,0,양수를 그래픽화면에 출력하기

import turtle
t=turtle.Turtle()
t.shape("turtle")

t.penup()#펜을 들고 이동, 그림이 그려지지 않음.
t.goto(100,100) #거북이를 100,100 좌표로 이동
t.write("거북이가 여기에오면 양수 입니다.")
t.goto(100,0)
t.write("거북이가 여기에오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기에오면 음수 입니다.")

t.goto(0,0) #원상태로 보냄
t.pendown() #penup상태를 해제
s=turtle.textinput("","숫자를 입력하세요")
n=int(s)

if n>0:
    t.goto(100,100)
if n==0:
    t.goto(100,0)
if n<0:
    t.goto(100,-100)
