// A shorthand for creating vectors...
/**
 * Constructs a vector from the specified Cartesian components.
 */
var vector: (x: number, y: number, z:  number)=>blade.Euclidean3 = visual.vectorE3;
/**
 * The unit vector in the x-direction.
 */
var e1 = vector(1, 0, 0);
/**
 * The unit vector in the y-direction.
 */
var e2 = vector(0, 1, 0);
/**
 * The unit vector in the z-direction.
 */
var e3 = vector(0, 0, 1);
/**
 * Computes the exponential function for a bivector argument.
 * @param x The argument to the exponential function, a bivector is expected.
 */
function exp(x: blade.Euclidean3): blade.Euclidean3 {
    // Really? norm yields a Euclidean3?
    var angle = x.norm().w;
    /**
     * A unit bivector representing the generator of the rotation.
     */
    var B = x / angle;
    return Math.cos(angle) + B * Math.sin(angle);
}

var popUp: Window = window.open("","","width=1200,height=800");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Geometry Zen";

var w: any = window;
w.Sk.output("visual.VERSION: " + visual.VERSION + "\n");

var viz = new visual.Visual(popUp);

var title = new createjs.Text("Visualizing Geometric Algebra with WebGL", "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
var help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

var box1 = new visual.Box({height:0.02, color:0x00FF00});
box1.position.set(0, -2, 0);
viz.scene.add(box1);

var arrow = new visual.Arrow({scale: 1.0, color: 0xFFFF00});
viz.scene.add(arrow);

var arrow2 = new visual.Arrow();
viz.scene.add(arrow2);

var box2 = new visual.Box({color:0xFF0000, opacity:0.25});
viz.scene.add(box2);
box2.position.set(2,-2,2);

var vortex = new visual.Vortex();
viz.scene.add(vortex)

var box3 = new visual.Box({depth:0.1, color:0x0000FF, opacity:0.25, transparent:true});
viz.scene.add(box3);

var sphere = new visual.Sphere({radius:0.4});
sphere.position.set(0,1.5,2);
viz.scene.add(sphere);

var ball = new visual.Sphere({radius:0.4, color:0x0000FF});
ball.position.set(0,1,1);
viz.scene.add(ball);

/**
 * The frequency of the rotation.
 */
var frequency = 1/20;
var omega = 2 * Math.PI * frequency * e3 ^ e1;

function setUp() { viz.setUp(); }

/**
 * Called repeatedly by the animation runner.
 */
function tick(time: number) {
    var theta = omega * time
    var x = theta / 2;
    var R = exp(-x);
    var S = exp(+x);
    S = ~R
    w.Sk.output(S + "\n");

    var r = R * e3 * S;
    ball.pos = r;
    arrow.attitude = R;
    box2.attitude = R;
    box3.attitude = R;
    vortex.attitude = R;

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
