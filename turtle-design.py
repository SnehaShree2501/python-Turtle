import turtle
screen = turtle.Screen()
point = turtle.Turtle()
point.speed(0)
screen.bgcolor("black")
for x in range (1,100):
    point.color("white")
    point.circle(4*x)
    point.right (90)
screen.exitonclick()