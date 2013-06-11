# sierpinski-e2ga.py
from browser import *
from sprite import *
from e2ga import *

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
    sprite.location = points[0]
    sprite.down()
    sprite.begin_fill()
    sprite.location = points[1]
    sprite.location = points[2]
    sprite.location = points[0]
    sprite.end_fill()

def getMid(p1,p2):
    return 0.5 * (p1 + p2)

def sierpinski(points, degree, sprite):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points, colormap[degree], sprite)
    if degree > 0:
        sierpinski([points[0],
                        0.5 * (points[0] + points[1]),
                        0.5 * (points[0] + points[2])],
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
    points = [Vector2(-100, -50), Vector2(0, 100), Vector2(100,-50)]
    sierpinski(points, 3, sprite)
    screen.exitonclick()

main()
