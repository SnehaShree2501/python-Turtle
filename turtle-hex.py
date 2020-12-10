import turtle
screen = turtle.Screen()
screen.bgcolor("black")
point = turtle.Turtle()
point.color("white")
point.pensize(2)
point.speed(0)
point.penup()
point.right(45)
point.forward(90)
point.right(135)
point.pendown()
for x in range(120):
    for y in range (6):
        point.forward(200)
        point.right(61)

    point.right(11.1111)
screen.exitonclick()    