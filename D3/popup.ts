
var popUp: Window = open("", "", "width=800, height=600");

popUp.document.body.style.backgroundColor = "202020";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "D3";

var width = Math.max(960, popUp.window.innerWidth)
var height = Math.max(500, popUp.window.innerHeight)
var x1 = width / 2
var y1 = height / 2
var x0 = x1
var y0 = y1
var i = 0
var r = 200
var tau = Math.PI * 2

var canvas = d3.select(popUp.document.body).append("canvas")

canvas.attr("width", width).attr("height", height)

d3.select(popUp.document.body).select("canvas").style("background-color", "#222")

function move(data: any, index: number) {
    var mouse = d3.mouse(canvas.node())
    x1 = mouse[0]
    y1 = mouse[1]
    d3.event.preventDefault()
}

canvas.on("mousemove", move)

var element: any = canvas.node();
var elemCanvas: HTMLCanvasElement = element;

var workbench = new visual.Workbench2D(elemCanvas, popUp.window)

var context = elemCanvas.getContext("2d")
context.globalCompositeOperation = "lighter"
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
    d3.select(popUp.document.body).transition().duration(2000).ease(Math.sqrt).tween("circle", tweeny)
}

function terminate(t) {
    return t > 60
}
    
function tearDown(e) {
    workbench.tearDown()
}

var war = eight.animationRunner(tick, terminate, setUp, tearDown, popUp.window)
war.start()
