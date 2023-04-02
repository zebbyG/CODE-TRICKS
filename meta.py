import turtle

turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.fillcolor("white")


def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


go(0, -100)
t.begin_fill()
t.circle(200)
t.end_fill()

t.pencolor("#2272f2")
t.fillcolor("#2272f2")
t.pensize(30)

go(-45, 80)
t.seth(50)
t.forward(100)
t.circle(-50, 90)
t.circle(-120, 60)
t.circle(-30, 130)
t.forward(160)
t.circle(50, 90)
t.circle(120, 60)
t.circle(32, 130)
t.forward(50)


turtle.done()
