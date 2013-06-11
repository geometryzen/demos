# sierpinski.py by Brad Miller
from sprite import *
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

# The turtle code will be happy now that it now has a canvas element!

def drawTriangle(points, color, sprite):
    sprite.fillcolor(color)
    sprite.up()
    sprite.goto(points[0][0], points[0][1])
    sprite.down()
    sprite.begin_fill()
    sprite.goto(points[1][0], points[1][1])
    sprite.goto(points[2][0], points[2][1])
    sprite.goto(points[0][0], points[0][1])
    sprite.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, sprite):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree], sprite)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, sprite)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, sprite)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, sprite)

def main():
    sprite = Sprite()
    screen = Screen()
    points = [[-100,-50],[0,100],[100,-50]]
    sierpinski(points, 3, sprite)
    screen.exitonclick()

main()
