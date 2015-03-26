removeElementsByTagName = (tagName) ->
  elements = document.getElementsByTagName(tagName)
  for element in elements
    element.parentNode.removeChild element

class Workbench2D
  constructor: (canvas: HTMLCanvasElement) ->
    this.canvas = canvas;
    onWindowResize = (event) ->
      width  = window.innerWidth
      height = window.innerHeight
      canvas.width  = width
      canvas.height = height
    this.sizer = onWindowResize

  setUp: () ->
    document.body.insertBefore(this.canvas, document.body.firstChild);
    window.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  tearDown: () ->
    window.removeEventListener('resize', this.sizer, false)
    removeElementsByTagName("canvas")

canvas = document.createElement("canvas")

stage = new createjs.Stage(canvas, "", {})

font = "20px Helvetica"

output = new createjs.Text(document.title + ". Hit Esc key to exit.", font, "black")
output.x = 100
output.y = 60
stage.addChild(output);

target = stage.addChild(new createjs.Shape())
target.graphics.beginFill("blue").drawCircle(0, 0, 50).endFill()
target.graphics.beginFill("white").drawCircle(0, 0, 30).endFill()
target.graphics.beginFill("red").drawCircle(0, 0, 10).endFill()
target.x = 100
target.y = 180

arm = stage.addChild(new createjs.Shape())
arm.graphics.beginFill("black").drawRect(-2, -2, 100, 4).endFill()
arm.graphics.beginFill("black").drawCircle(100, 0, 8).endFill()
arm.x = 180
arm.y = 100

workbench2D = new Workbench2D(canvas)

setUp = () -> workbench2D.setUp()

tick = (t) ->
    arm.rotation = 180 * t
    target.alpha = 0.2
    point = arm.localToLocal(100, 0, target)
    if target.hitTest(point.x, point.y)
        target.alpha = 1
    stage.update()

terminate = (t) -> t > 10

tearDown = (e) -> workbench2D.tearDown()

eight.animationRunner(tick, terminate, setUp, tearDown, window).start()
