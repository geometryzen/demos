# Sierpinski Gasket demonstration
# Original program by Brad Miller.
# While using the sprite module is amusing, it would probably better
# to use the HTML5 Canvas API provided through the browser module.
from browser import *
from sprite import *
from blade import *

# Make the sprite code happy - give it a canvas element.
def initCanvas():
    # Discard the old canvas if it exists. 
    canvas = document.getElementById("canvas")
    if (canvas):
        canvas.parentNode.removeChild(canvas)

    canvas = document.createElement("canvas", {"id": "canvas"})
    canvas.width = 250
    canvas.height = 250

    container = document.getElementById("canvas-container")
    container.appendChild(canvas)

def drawTriangle(points, color, sprite):
    
    sprite.fillcolor = color
    sprite.up()
    sprite.position = points[0]
    sprite.down()
    sprite.begin_fill()
    sprite.position = points[1]
    sprite.position = points[2]
    sprite.position = points[0]
    sprite.end_fill()

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
                        0.5 * (points[0] + points[1]),
                        0.5 * (points[1] + points[2])],
                   degree-1, sprite)
        sierpinski([points[2],
                        0.5 * (points[2] + points[1]),
                        0.5 * (points[0] + points[2])],
                   degree-1, sprite)
def Vector(x, y):
    return Euclidean2(0, x, y, 0)

def main():
    initCanvas()
    sprite = Sprite()
    screen = Screen()
    points = [Vector(-100, -50), Vector(0, 100), Vector(100,-50)]
    sierpinski(points, 3, sprite)
    screen.exitonclick()

main()
