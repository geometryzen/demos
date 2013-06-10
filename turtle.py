# turtle.py
import turtle
from browser import *

canvas = document.createElement("canvas")
canvas.id = "canvas"
canvas.setAttribute("id", "canvas")
print canvas
container = document.getElementById("canvas-container")
print container
container.appendChild(canvas)



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