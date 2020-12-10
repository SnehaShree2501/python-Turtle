import turtle
screen = turtle.Screen()
point = turtle.Turtle()
screen.bgcolor("black")
point.color("white")
point.speed(0)
point.pensize(2)
for r in range (15):
    point.circle(90)
    point.right(24)
point.color("red")    
for r in range (15):
    point.circle(120)
    point.right(24)
point.color("white")
point.pensize(3)
for r in range (15):
    point.circle(90)
    point.right(24)
screen.exitonclick()
