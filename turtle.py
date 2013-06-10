# turtle.py
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.color("yellow")
tess.shape("turtle")

print(range(5,60,2))
tess.penup()
for size in range(5,60,2):
    tess.stamp()
    tess.forward(size)
    tess.right(24)

wn.exitonclick()