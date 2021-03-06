/**
 * The unit vector in the x-direction.
 */
var e1 = blade.vectorE3(1, 0, 0);
/**
 * The unit vector in the y-direction.
 */
var e2 = blade.vectorE3(0, 1, 0);
/**
 * The unit vector in the z-direction.
 */
var e3 = blade.vectorE3(0, 0, 1);
/**
 * Computes the exponential function for a bivector argument.
 * @param x The argument to the exponential function, a bivector is expected.
 */
function exp(x: blade.Euclidean3): blade.Euclidean3 {
    // Really? norm yields a Euclidean3?
    // We now have to extract the scalar component to calculate cos, sin.
    // Of course, we could have universal functions instead.
    var angle = x.norm().w;
    /**
     * A unit bivector representing the generator of the rotation.
     */
    var B = x / angle;
    return Math.cos(angle) + B * Math.sin(angle);
}

class Popup {
  public wnd: Window;
  constructor(title: string, width: number=1200, height: number=800) {
    this.wnd = window.open("","","width="+width+",height="+height);
    this.wnd.document.body.style.backgroundColor = "080808";
    this.wnd.document.body.style.overflow = "hidden";
    this.wnd.document.title = title;
  }
  close() {
    this.wnd.close();
  }
}

console.log("visual.VERSION: " + visual.VERSION + "\n");

var popUp = new Popup("Geometry Zen");
var viz = new visual.Visual(popUp.wnd);

var title = new createjs.Text("Visualizing Geometric Algebra with WebGL", "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
var help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

var box1 = new visual.Box({height: 0.02, color: 0x00FF00});
box1.pos = -2 * e2 / 5;
viz.scene.add(box1);

var arrow = new visual.Arrow({color: 0xFFFF00});
viz.scene.add(arrow);

var box2 = new visual.Box({width:0.2, height:0.4, depth:0.6, color:0xFF0000, opacity:0.25});
viz.scene.add(box2);
box2.position.set(0.6,-0.6,0.6);

var vortex = new visual.Vortex({radius:0.8,radiusCone:0.07,color:0x00FFFF});
viz.scene.add(vortex)

var box3 = new visual.Box({width:2, height:2, depth:0.02, color:0x0000FF, opacity:0.25, transparent:true});
viz.scene.add(box3);

var ball = new visual.Sphere({radius:0.2, color:0x0000FF});
viz.scene.add(ball);

/**
 * The frequency of the rotation.
 */
var frequency = 1/10;
/**
 * The angular velocity, represented as a bivector.
 */
var omega = 2 * Math.PI * frequency * e3 ^ e1;

function setUp() {
  viz.setUp();
  viz.camera.position.set(2, 2, 2);
}

/**
 * Called repeatedly by the animation runner.
 */
function tick(time: number) {
    var theta = omega * time;
    var R = exp(-theta/2);

    ball.pos = R * e3 * ~R;
    arrow.attitude = R;
    box2.attitude = R;
    box3.attitude = R;
    vortex.attitude = R;

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp.wnd).start();
