var width = Math.max(960, window.innerWidth)
var height = Math.max(500, window.innerHeight)
var x1 = width / 2
var y1 = height / 2
var x0 = x1
var y0 = y1
var i = 0
var r = 200
var tau = Math.PI * 2

var canvas = d3.select("body").append("canvas")

canvas.attr("width", width).attr("height", height)

d3.select("canvas").style("background-color", "#222")

function move(data: any, index: number) {
    var mouse = d3.mouse(canvas.node())
    x1 = mouse[0]
    y1 = mouse[1]
    d3.event.preventDefault()
}

canvas.on("mousemove", move)

var element: any = canvas.node();
var elemCanvas = element;

var workbench = new visual.Workbench2D(elemCanvas, window)

var context = elemCanvas.getContext("2d")
context.globalCompositionOperation = "lighter"
context.lineWidth = 2

function setUp() {
    workbench.setUp()
}

function tick(t) {
    i += 1
    context.clearRect(0,0,width,height)
    var z = d3.hsl(i % 360, 1, 0.5).rgb()
    var c = "rgba(" + z.r + "," + z.g + "," + z.b + ","
    x0 += (x1 - x0) * .1
    y0 += (y1 - y0) * .1
    var x = x0
    var y = y0
    function tweeny(unused1, unused2) {
        function circle(t) {
            var s = c + "" + (1-t) + ")"
            context.strokeStyle = s
            context.beginPath()
            context.arc(x, y, r * t, 0, tau)
            context.stroke()
        }
        return circle
    }
    // The following is correct. Maybe an error in the TypeLibrary definitions?
    d3.select({}).transition().duration(2000).ease(Math.sqrt).tween("circle", tweeny)
}

function terminate(t) {
    return t > 60
}
    
function tearDown(e) {
    workbench.tearDown()
}

var war = eight.animationRunner(tick, terminate, setUp, tearDown, window)
war.start()
