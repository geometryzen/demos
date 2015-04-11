width = Math.max(960, window.innerWidth)
height = Math.max(500, window.innerHeight)
x1 = width / 2
y1 = height / 2
x0 = x1
y0 = y1
i = 0
r = 200
tau = Math.PI * 2

canvas = d3.select("body").append("canvas")

canvas.attr("width", width).attr("height", height)

d3.select("canvas").style("background-color", "#222")

move = (data, index) ->
    mouse = d3.mouse(canvas.node())
    x1 = mouse[0]
    y1 = mouse[1]
    d3.event.preventDefault()

canvas.on("mousemove", move)

element = canvas.node();
elemCanvas = element;

workbench = new visual.Workbench2D(elemCanvas, window)

context = elemCanvas.getContext("2d")
context.lobalCompositionOperation = "lighter"
context.lineWidth = 2

setUp = () -> workbench.setUp()

tick = (t) ->
    i += 1
    context.clearRect(0,0,width,height)
    z = d3.hsl(i % 360, 1, 0.5).rgb()
    c = "rgba(" + z.r + "," + z.g + "," + z.b + ","
    x0 += (x1 - x0) * .1
    y0 += (y1 - y0) * .1
    x = x0
    y = y0
    tweeny = (unused1, unused2) ->
        circle = (t) ->
            s = c + "" + (1-t) + ")"
            context.strokeStyle = s
            context.beginPath()
            context.arc(x, y, r * t, 0, tau)
            context.stroke()
        return circle
    # The following is correct. Maybe an error in the TypeLibrary definitions?
    d3.select({}).transition().duration(2000).ease(Math.sqrt).tween("circle", tweeny)

terminate = (t) -> t > 60
    
tearDown = (e) -> workbench.tearDown()

war = eight.animationRunner(tick, terminate, setUp, tearDown, window)
war.start()
