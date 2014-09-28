// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

var popUp = window.open("", "", "width=800, height=600", false);

var document = popUp.document;

var canvas = document.createElement("canvas");

canvas.setAttribute("id", "graph");
canvas.setAttribute("width", "400");
canvas.setAttribute("height", "400");

document.body.appendChild(canvas);

var context: CanvasRenderingContext2D = canvas.getContext("2d");

/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  context.clearRect(0,0,200,200);
  var c = Math.cos(time);
  var s = Math.sin(time);
  var center = {x:100,y:100}
  context.beginPath();
  context.moveTo(center.x, center.y);
  context.lineTo(c * 100 + center.x, s * 100 + center.y);
  context.closePath();
  context.stroke();
}

/**
 * Called to determine whether to end the animation.
 */
function terminate(time: number): boolean {
  return false;
}

/**
 * Called once at the start of the animation.
 */
function setUp() {
  
}

/**
 * Called once at the end of the animation.
 */
function tearDown(e: Error) {
  popUp.close();
}

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();