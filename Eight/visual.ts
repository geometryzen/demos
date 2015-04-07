// This program is under development.
var popUp: Window = window.open("","","width=1200,height=800");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Visualizing Geometric Algebra with WebGL";

var w: any = window;
w.Sk.output("visual.VERSION: " + visual.VERSION + "\n");
var vz = visual;

var viz = new vz.Visual(popUp);

var title = new createjs.Text(popUp.document.title, "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
var help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

var box1 = new visual.Box(5.0, 0.1, 5.0, 0x00FF00);
box1.position.set(0, -2, 0);
viz.scene.add(box1);

var arrow = new visual.Arrow(4.0, 0xFFFF00);
viz.scene.add(arrow);

var arrow2 = new visual.Arrow(4.0, 0xFFFFFF);
viz.scene.add(arrow2);

var box2 = new visual.Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
viz.scene.add(box2);
box2.position.set(3,-3,3);

var vortex = new visual.Vortex(1.0, 0x00FFFF, 0.3);
viz.scene.add(vortex)

var box3 = new visual.Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
viz.scene.add(box3);

var sphere = new visual.Sphere({radius:0.4});
sphere.position.set(0,3,4);
viz.scene.add(sphere);

var ball = new visual.Sphere({radius:0.4},{color:0x0000FF});
ball.position.set(0,2,2);
viz.scene.add(ball);

var e1 = vz.vector(1, 0, 0);
var e2 = vz.vector(0, 1, 0);
var e3 = vz.vector(0, 0, 1);
var tau = 2 * Math.PI;
var omega = (tau / 20);
// A unit bivector rotating from k to i
var B = e3 ^ e1;
// Just make sure that we really do have a unit bivector.
B = B / B.norm();
//Sk.output(B + "\n");

function setUp() { viz.setUp(); }

function tick(time: number) {
    var theta = omega * time;
    var rotor = Math.cos(theta/2) - B * Math.sin(theta/2);

    var r = e2;

    ball.position.set(r.x, r.y, r.z);
    arrow.attitude = rotor;
    box2.attitude = rotor;
    box3.attitude = rotor;
    vortex.attitude = rotor;

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
