var popUp: Window = window.open("","","width=1200,height=800");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Geometry Zen";

var w: any = window;
w.Sk.output("visual.VERSION: " + visual.VERSION + "\n");
var vz = visual;

var viz = new vz.Visual(popUp);


var title = new createjs.Text("Visualizing Geometric Algebra with WebGL", "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
var help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

function point(u: number, v: number): THREE.Vector3
{
    return new THREE.Vector3(u,v,u*v);
}

var g = new THREE.ParametricGeometry(point, 10, 10);
var s = new visual.VisualElement(g, 0xFFFFFF, 1.0, false);
viz.scene.add(s);

var e1: any = vz.vectorE3(1, 0, 0);
var e2: any = vz.vectorE3(0, 1, 0);
var e3: any = vz.vectorE3(0, 0, 1);
var frequency = 1/20;
var omega = 2 * Math.PI * frequency * e3 ^ e1;

function setUp() { viz.setUp(); }

function tick(time: number) {
    var theta = omega * time

    help.text = viz.camera.position.x + ", " + viz.camera.position.y;

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
