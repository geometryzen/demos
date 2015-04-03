# This program is under development.
popUp = window.open("","","width=1200,height=800");
popUp.document.body.style.backgroundColor = "080808";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Visualizing Geometric Algebra with WebGL";

viz = new visual.Visual(popUp);

title = new createjs.Text(popUp.document.title, "24px Helvetica", "white");
title.x = 100; title.y = 60;
viz.stage.addChild(title);
help = new createjs.Text("Hit Esc key to exit. Mouse to Rotate, Zoom, and Pan.", "20px Helvetica", "white");
help.x = 140; help.y = 100;
viz.stage.addChild(help);

box1 = new visual.Box(5.0, 0.1, 5.0, 0x00FF00);
box1.mesh.position.set(0, -2, 0);
viz.scene.add(box1.mesh);

arrow = new visual.Arrow(4.0, 0xFFFF00);
viz.scene.add(arrow.mesh);

box2 = new visual.Box(1.0, 2.0, 3.0, 0xFF0000, 0.25, false);
viz.scene.add(box2.mesh);
box2.mesh.position.set(3,-3,3);

vortex = new visual.Vortex(1.0, 0x00FFFF, 0.3);
viz.scene.add(vortex.mesh)

box3 = new visual.Box(10.0,10.0,0.1, 0x0000FF, 0.25, true);
viz.scene.add(box3.mesh);

tau = 2 * Math.PI;
omega = (tau / 20);
# A unit bivector rotating from k to i
 B = new blade.Euclidean3(0, 0, 0, 0, 0, 0, 1, 0);
# Just make sure that we really do have a unit bivector.
B = B / B.norm();

setUp = () -> viz.setUp()

function tick(time: number) {
    var theta = omega * time;
    var s: any = new blade.Euclidean3(Math.cos(theta/2), 0, 0, 0, 0, 0, 0, 0);
    var rotor: any = s - B * Math.sin(theta/2);

      arrow.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      box2.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      box3.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);
      vortex.mesh.quaternion.set(-rotor.yz, -rotor.zx, -rotor.xy, rotor.w);

    viz.update();
}

function terminate(time: number) { return false; }

function tearDown(e: Error) { viz.tearDown(); popUp.close(); }

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
