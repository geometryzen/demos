var eight = window.EIGHT;

var glwin = window.open("","","width=800,height=600");

glwin.document.body.style.backgroundColor = "202020";
glwin.document.body.style.overflow = "hidden";
glwin.document.title = "Visualizing Geometric Algebra with WebGL";

var canvas2D = glwin.document.createElement("canvas");
canvas2D.style.position = "absolute";
canvas2D.style.top = "0px";
canvas2D.style.left = "0px";
/*
workbench2D = Workbench2D(canvas2D, glwin)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text(glwin.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)
*/
var scene = eight.scene();

var camera = eight.perspectiveCamera(45, 1.0, 0.1, 100);

var renderer = eight.webGLRenderer();
// renderer.setClearColor(THREE.Color(0x080808), 1.0)

var box = eight.mesh(eight.boxGeometry());
scene.add(box);
box.position = eight.vectorE3(-1.0,-0.5,-5.0);
var prism = eight.mesh(eight.prismGeometry());
scene.add(prism);
prism.position = eight.vectorE3(0.0,0.0,-5.0);

/*
#CartesianSpace(scene, renderer, camera)
#camera.position = eight.vectorE3(10.0, 9.0, 8.0)
#camera.up.set(0,0,1)
#camera.lookAt(scene.position)
*/
var workbench3D = eight.workbench3D(renderer.canvas, renderer, camera, glwin)
/*
tau = 2 * pi
omega = (tau / 20) / second
# A unit bivector rotating from k to i
B = BivectorE3(0.0, 0.0, 1.0)
# Just make sure that we really do have a unit bivector.
B = B / magnitude(B)
*/
function setUp()
{
//  workbench2D.setUp()
    workbench3D.setUp()
    monitor.start()
}

var B = eight.bivectorE3(0,0,1);
var angle = 0;

function tick(t)
{
  var c = eight.scalarE3(Math.cos(angle/2));
  var s = eight.scalarE3(Math.sin(angle/2));
  var R = c.sub(B.mul(s));
  box.attitude = R;
  prism.attitude = R;

  renderer.render(scene, camera)
//  space2D.render()
  angle += 0.01;
}

function terminate(t)
{
    return false;
}

function tearDown(e)
{
    monitor.stop();
    glwin.close();
    if (e)
    {
        console.log("Error during animation: " + e)
    }
    else
    {
        console.log("Goodbye!")
        workbench3D.tearDown()
//      workbench2D.tearDown()
        scene.tearDown();
    }
}

var runner = eight.windowAnimationRunner(tick, terminate, setUp, tearDown, glwin);

function onContextLoss()
{
    runner.stop();
    renderer.onContextLoss();
    scene.onContextLoss();
}

function onContextGain(gl)
{
    scene.onContextGain(gl);
    renderer.onContextGain(gl);
    runner.start();
}

var monitor = eight.webGLContextMonitor(renderer.canvas, onContextLoss, onContextGain);

onContextGain(renderer.context);
