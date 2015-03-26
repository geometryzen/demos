function removeElementsByTagName(tagName) {
  var elements = document.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
  }
}

class Workbench2D
{
  public canvas;
  private sizer: EventListener;
  constructor(canvas: HTMLCanvasElement)
  {
    this.canvas = canvas;
    function onWindowResize(event)
    {
      var width  = window.innerWidth;
      var height = window.innerHeight;
      canvas.width  = width;
      canvas.height = height;
    }
    this.sizer = onWindowResize;
  }
  setUp()
  {
    document.body.insertBefore(this.canvas, document.body.firstChild);
    window.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  }
  tearDown()
  {
    window.removeEventListener('resize', this.sizer, false);
    removeElementsByTagName("canvas");
  }
}

var canvas = document.createElement("canvas")

var stage = new createjs.Stage(canvas, "", {})

var target:any = stage.addChild(new createjs.Shape())
target.graphics.beginFill("blue").drawCircle(0, 0, 50).endFill()
target.graphics.beginFill("white").drawCircle(0, 0, 30).endFill()
target.graphics.beginFill("red").drawCircle(0, 0, 10).endFill()
target.x = 100
target.y = 180

var arm: any = stage.addChild(new createjs.Shape())
arm.graphics.beginFill("black").drawRect(-2, -2, 100, 4).endFill()
arm.graphics.beginFill("black").drawCircle(100, 0, 8).endFill()
arm.x = 180
arm.y = 100

var workbench2D = new Workbench2D(canvas)

function setUp() {
    workbench2D.setUp()
}

function tick(t) {
    arm.rotation = 180 * t
    target.alpha = 0.2
    var point = arm.localToLocal(100, 0, target)
    if (target.hitTest(point.x, point.y)) {
        target.alpha = 1
    }
    stage.update()
}

function terminate(t) {
    return t > 10
}

function tearDown(e) {
    workbench2D.tearDown()
}

eight.animationRunner(tick, terminate, setUp, tearDown, window).start()
