# sprite-e2ga.py
from sprite import *
from browser import *

# Discard the old canvas if it exists. 
canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)

# Create a new canvas, setting the attributes in three ways! 
canvas = document.createElement("canvas", {"id": "canvas"})
canvas.width = 400
canvas.height = 300
canvas.setAttribute("height", "300")

# Append the canvas to the provided container (the content of the widget).
container = document.getElementById("canvas-container")
container.appendChild(canvas)

# The turtle code will be happy now that it now has a canvas element!

screen = Screen()
screen.bgcolor("black")

alice = Sprite()
alice.color("yellow")
shapes = [
    "arrow",
    "blank",
    "circle",
    "classic",
    "square",
    "triangle",
    "turtle"
]
alice.shape(shapes[6]) 

alice.penup()
for size in range(5,60,2):
    alice.stamp()
    alice.forward(size)
    alice.right(24)
    # heading() is currently degrees, we want a vector.
    # It's also a method and we want a mutable property.
    print alice.heading()
    # position() looks like a tuple, we want a vector.
    print alice.position()

screen.exitonclick()
