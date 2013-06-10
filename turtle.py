# turtle.py
from turtle import *
from browser import *

# Discard the old canvas if it exists.
canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)

# Create a new canvas, setting the attributes in three ways! 
canvas = document.createElement("canvas", {"id": "canvas"})
canvas.width = 400
canvas.setAttribute("height", "300")

# Append the canvas to the provided container (the content of the widget).
container = document.getElementById("canvas-container")
container.appendChild(canvas)

# The turtle code will be happy that it now has a canvas element!

screen = Screen()
screen.bgcolor("black")

tess = Turtle()
tess.color("yellow")
tess.shape("turtle")

print(range(5,60,2))
tess.penup()
for size in range(5,60,2):
    tess.stamp()
    tess.forward(size)
    tess.right(24)

screen.exitonclick()