# sprites.py
from browser import *
from sprite import *
from e2ga import *

# Discard the old canvas if it exists. 
canvas = document.getElementById("canvas")
if (canvas):
    canvas.parentNode.removeChild(canvas)

canvas = document.createElement("canvas", {"id": "canvas"})
canvas.width = 200
canvas.height = 250

# Append the canvas to the provided container (the content of the widget).
container = document.getElementById("canvas-container")
container.appendChild(canvas)

# The turtle code will be happy now that it now has a canvas element!

screen = Screen()
screen.bgcolor("black")

a = Sprite({"color": "red"})
b = Sprite({"color": "yellow"})
c = Sprite({"color": "green"})
d = Sprite({"color": "blue"})
sprites = [a, b, c, d]

for s in sprites:
    s.up()

a.position = Vector2(-50, -50)
b.position = Vector2( 50, -50)
c.position = Vector2( 50,  50)
d.position = Vector2(-50,  50)

for size in range(1,20,1):
    for s in sprites:
        s.stamp()
        s.forward(10)
        s.right(18)

screen.exitonclick()
