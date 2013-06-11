# sierpinski.py by Brad Miller
from sprite import *
from browser import *

# Make the sprite code happy - give it a canvas element.
def initCanvas():
    # Discard the old canvas if it exists. 
    canvas = document.getElementById("canvas")
    if (canvas):
        canvas.parentNode.removeChild(canvas)

    canvas = document.createElement("canvas", {"id": "canvas"})
    canvas.width = 400
    canvas.height = 300

    container = document.getElementById("canvas-container")
    container.appendChild(canvas)

def drawTriangle(points, color, sprite):
    sprite.fillcolor = color
    sprite.up()
    sprite.location.x = points[0][0]
    sprite.location.y = points[0][1]
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
    initCanvas()
    sprite = Sprite()
    screen = Screen()
    points = [[-100,-50],[0,100],[100,-50]]
    sierpinski(points, 3, sprite)
    screen.exitonclick()

main()
