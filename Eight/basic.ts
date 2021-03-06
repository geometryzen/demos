var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log("Hello!");

var popUp: Window = open("", "", "width=800, height=600");

popUp.document.body.style.backgroundColor = "202020";
popUp.document.body.style.overflow = "hidden";
popUp.document.title = "Visualizing Geometric Algebra with WebGL";

var scene = eight.scene();

var camera = eight.perspective(45, 1.0, 0.1, 100);

var renderer: eight.WebGLRenderer = eight.renderer();

var box = eight.mesh(eight.box());
scene.add(box);
box.position = eight.vectorE3(-1.0,-0.5,-5.0);
var prism = eight.mesh(eight.prism());
scene.add(prism);
prism.position = eight.vectorE3(0.0,0.0,-5.0);

var workbench = eight.workbench(renderer.canvas, renderer, camera, popUp);

function setUp() {
  workbench.setUp();
  monitor.start();
}

var B = eight.bivectorE3(0,1,1);
B = B / B.norm()
var angle: number = 0;

var w: any = window
var stats = new w.Stats();
stats.setMode(0);
stats.domElement.style.position = 'absolute';
stats.domElement.style.left = '0px';
stats.domElement.style.top = '0px';

popUp.document.body.appendChild(stats.domElement);

/**
 * Performs the animation.
 */
function tick(time: number) {
  stats.begin();
  var halfAngle = angle/2;
  var c = Math.cos(halfAngle);
  var s = Math.sin(halfAngle);
  var R = c - B * s;
  box.attitude = R;
  prism.attitude = R;

  renderer.render(scene, camera);
  angle += 0.01;
  stats.end();
}

/**
 * Determines whether to terminate the animation.
 */
function terminate(time: number) {return false;}

function tearDown(e) {
  monitor.stop();
  popUp.close();
  if (e) {
    log("Error during animation: " + e);
  }
  else {
    log("Goodbye!");
    workbench.tearDown();
    scene.tearDown();
  }
}

var runner = eight.animationRunner(tick, terminate, setUp, tearDown, popUp);

function onContextLoss() {
    runner.stop();
    renderer.onContextLoss();
    scene.onContextLoss();
}

function onContextGain(context: WebGLRenderingContext) {
    scene.onContextGain(context);
    renderer.onContextGain(context);
    runner.start();
}

var monitor = eight.contextMonitor(renderer.canvas, onContextLoss, onContextGain);

onContextGain(renderer.context);
