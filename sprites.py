# sprites.py
from browser import *
from sprite import *
from e2ga import *

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

a = Sprite({"color": "red"})
b = Sprite({"color": "yello"})
c = Sprite({"color": "green"})
d = Sprite({"color": "blue"})
sprites = [a, b, c, d]

a.up()
for size in range(5,60,2):
    for s in sprites
        s.stamp()
        s.forward(size)
        s.right(24)

screen.exitonclick()
