import turtle

def draw_olympic_symbol():
    position=[[0,0,"blue"],[-120,0,"purple"],[60,60,"red"],[-60,60,"yellow"],[-180,60,"green"]]
    for x,y,c in position:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.color(c,c)
        t.begin_fill()
        t.circle(30)
        t.end_fill()
t = turtle.Turtle()
draw_olympic_symbol()
