# This program is under development.
popUp = window.open("","","width=1200,height=800")
popUp.document.body.style.backgroundColor = "080808"
popUp.document.body.style.overflow = "hidden"
popUp.document.title = "Visualizing Geometric Algebra with WebGL"

viz = new visual.Visual(popUp)

title = new createjs.Text(popUp.document.title, "24px Helvetica", "white")
title.x = 100; title.y = 60;
viz.stage.addChild(title)
help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white")
help.x = 140; help.y = 100
viz.stage.addChild(help)

box1 = new visual.Box(5.0, 0.1, 5.0, 0x00FF00)
box1.position.set(0, -2, 0)
viz.scene.add(box1)

arrow = new visual.Arrow(scale: 2.0, axis: x:0, y:0, z:1, color: 0xFFFF00)
viz.scene.add(arrow)

box2 = new visual.Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false)
viz.scene.add(box2)
box2.position.set(3,-3,3)

vortex = new visual.Vortex(1.0, 0x00FFFF, 0.3)
viz.scene.add(vortex)

box3 = new visual.Box(8.0, 8.0, 0.1, 0x0000FF, 0.25, true)
viz.scene.add(box3)

tau = 2 * Math.PI
omega = tau / 20
# A unit bivector rotating from k to i
B = new blade.Euclidean3(0, 0, 0, 0, 0, 0, 1, 0);
# Just make sure that we really do have a unit bivector.
B = B / B.norm();

setUp = () -> viz.setUp()

tick = (time) ->
    theta = omega * time
    s = new blade.Euclidean3(Math.cos(theta/2), 0, 0, 0, 0, 0, 0, 0)
    rotor = s - B * Math.sin(theta/2)
    arrow.attitude = rotor
    box2.attitude = rotor
    box3.attitude = rotor
    vortex.attitude = rotor
    viz.update()

terminate = (time) -> false

tearDown = (e) ->
  viz.tearDown()
  popUp.close()

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start()
