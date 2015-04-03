// This program is under development.
var popUp: Window = window.open("","","width=1200,height=800");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Visualizing Geometric Algebra with WebGL";

var viz = new visual.Visual(popUp);

var title = new createjs.Text(popUp.document.title, "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
var help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

var mono = new visual.Box(5.0, 0.1, 5.0, 0x00FF00);
mono.mesh.position.set(0, -2, 0);
viz.scene.add(mono.mesh);

var arrow = new visual.Arrow(4.0, 0xFFFF00);
viz.scene.add(arrow.mesh);

var box = new visual.Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
viz.scene.add(box.mesh);
box.mesh.position.set(3,-3,3);

var vortex = new visual.Vortex(1.0, 0x00FFFF, 0.3);
viz.scene.add(vortex.mesh)

var flat = new visual.Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
viz.scene.add(flat.mesh);

var tau = 2 * Math.PI;
var omega = (tau / 10);
// A unit bivector rotating from k to i
var B: any = new blade.Euclidean3(0, 0, 0, 0, 0, 0, 1, 0);
// Just make sure that we really do have a unit bivector.
B = B / B.norm();

function setUp() { viz.setUp(); }

function tick(time: number) {
    var theta = omega * time;
    var s: any = new blade.Euclidean3(Math.cos(theta/2), 0, 0, 0, 0, 0, 0, 0);
    var rotor: any = s - B * Math.sin(theta/2);

      arrow.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      box.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      flat.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      vortex.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
