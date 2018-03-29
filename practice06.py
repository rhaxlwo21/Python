import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(3)
t.shapesize(3,3)

a=True
while a:
    command=input("명령어를 입력하시오:")
    if command == "l":#사용자가 "l"을 입력하였으면
        t.left(90)
        t.forward(100)
    if command == "r":#사용자가 "r"을 입력하였으면
        t.right(90)
        t.forward(100)
    if command == "f":
        t.forward(100)
    if command == "b":
        t.back(100)
    if command =="q":
        a=False
