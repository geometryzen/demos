var canvas = document.getElementById("my-canvas");
if (typeof WebGLDebugUtils !== 'undefined')
{
  canvas = WebGLDebugUtils.makeLostContextSimulatingCanvas(canvas);
  //canvas.loseContextInNCalls(1000);
  //canvas.setRestoreTimeout(3000);
}
var scene = EIGHT.scene();
var renderer = EIGHT.webGLRenderer({'canvas':canvas});

var box = EIGHT.mesh(EIGHT.boxGeometry());
box.position = EIGHT.vectorE3(-1.0,-0.5,-5);
scene.add(box);
var prism = EIGHT.mesh(EIGHT.prismGeometry());
prism.position = EIGHT.vectorE3(0.0,0.0,-5);
scene.add(prism);

var B = EIGHT.bivectorE3(0,0,1);
var angle = 0;

var stats = new Stats();
stats.setMode(0);
stats.domElement.style.position = 'absolute';
stats.domElement.style.left = '0px';
stats.domElement.style.top = '0px';
document.body.appendChild(stats.domElement);

var tick = function(time)
{
  var c = EIGHT.scalarE3(Math.cos(angle/2));
  var s = EIGHT.scalarE3(Math.sin(angle/2));
  var R = c.sub(B.mul(s));
  box.attitude = R;
  prism.attitude = R;
  stats.begin();
  renderer.render(scene, camera);
  stats.end();
  angle += 0.01;
};
var terminate = function(time)
{
  return false;
};
var setUp = function()
{
  monitor.start();
};

var tearDown = function()
{
  monitor.stop();
  scene.tearDown();
};

var runner = EIGHT.windowAnimationRunner(tick, terminate, setUp, tearDown);
var camera = EIGHT.perspectiveCamera(45, canvas.width / canvas.height, 0.1, 100.0);

var onContextLoss = function()
{
  runner.stop();
  renderer.onContextLoss();
  scene.onContextLoss();
};

var onContextGain = function(gl)
{
  scene.onContextGain(gl);
  renderer.onContextGain(gl);
  runner.start();
};

var monitor = EIGHT.webGLContextMonitor(canvas, onContextLoss, onContextGain);

var gl = canvas.getContext('webgl');
if (typeof WebGLDebugUtils !== 'undefined')
{
  var logGLCall = function(functionName, args)
  {
     console.log(functionName + "(" + WebGLDebugUtils.glFunctionArgsToString(functionName, args) + ")");
  }
  function validateNoneOfTheArgsAreUndefined(functionName, args)
  {
    for (var ii = 0; ii < args.length; ++ii)
    {
      if (args[ii] === undefined)
      {
        var argString = WebGLDebugUtils.glFunctionArgsToString(functionName, args);
        console.error("undefined passed to " + functionName + "(" + argString + ")");
      }
    }
  }
  function onGLCall(functionName, args)
  {
     logGLCall(functionName, args);
     validateNoneOfTheArgsAreUndefined(functionName, args);
  }
  gl = WebGLDebugUtils.makeDebugContext(gl, undefined, onGLCall);
}
onContextGain(gl);
