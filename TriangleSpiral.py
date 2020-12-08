import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
candy = turtle.Turtle()
candy.color("red")
candy.shape("square")
dist = 5
candy.up()
for x in range(45):
    candy.stamp()
    candy.forward(dist)
    candy.right(24)
    dist = dist +2
wn.exitonclick()  