# turtle.py
import turtle
from browser import *

canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)
    
canvas = document.createElement("canvas")
canvas.id = "canvas"
canvas.width = 400
canvas.height = 300
#canvas.setAttribute("id", "canvas")
container = document.getElementById("canvas-container")
container.appendChild(canvas)

screen = turtle.Screen()
screen.bgcolor("black")
tess = turtle.Turtle()
tess.color("yellow")
tess.shape("turtle")

print(range(5,60,2))
tess.penup()
for size in range(5,60,2):
    tess.stamp()
    tess.forward(size)
    tess.right(24)

screen.exitonclick()