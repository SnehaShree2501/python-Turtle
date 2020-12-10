import turtle
screen= turtle.Screen()
screen.bgcolor("black")
point1 = turtle.Turtle()
point1.pensize(2)
point1.speed(0)
point1.color("red")
for x in range(120):
    point1.forward(x*5)
    point1.right(144)
screen.exitonclick()
