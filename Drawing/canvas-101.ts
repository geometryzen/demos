// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

// Global Variables.
var popUp: Window = window.open("", "", "width=800, height=600", false);
var context: CanvasRenderingContext2D;
var printer: Printer3D;

class Printer3D {
  private context2D: CanvasRenderingContext2D;
  constructor(context2D: CanvasRenderingContext2D) {
    this.context2D = context2D;
  }
  beginPath(): void {
    this.context2D.beginPath();
  }
  stroke(): void {
    this.context2D.stroke();
  }
  moveTo(x: number, y: number, z: number): void {
    this.context2D.moveTo(x, y);    
  }
  lineTo(x: number, y: number, z: number): void {
    this.context2D.lineTo(x, y);    
  }
}

class Cube {
  draw()
  {
    // RHS face
    printer.beginPath();
    printer.moveTo(+100,-100,-100);
    printer.lineTo(+100,-100,+100);
    printer.lineTo(+100,+100,+100);
    printer.lineTo(+100,+100,-100);
    printer.lineTo(+100,-100,-100);
    printer.stroke();

    // LHS face
    printer.beginPath();
    printer.moveTo(-100,-100,-100);
    printer.lineTo(-100,-100,+100);
    printer.lineTo(-100,+100,+100);
    printer.lineTo(-100,+100,-100);
    printer.lineTo(-100,-100,-100);
    printer.stroke();

    // bottom face
    printer.beginPath();
    printer.moveTo(-100,+100,-100);
    printer.lineTo(-100,+100,+100);
    printer.lineTo(+100,+100,+100);
    printer.lineTo(+100,+100,-100);
    printer.lineTo(-100,+100,-100);
    printer.stroke();
  }
}

var cube = new Cube();

function perspective(X: number, Y: number, Z: number, d: number): {x:number; y:number} {
  /**
   * The distance factor determines how much the X and Y components are reduced by the distance (Z + d) from the viewer.
   */
  var distanceFactor = d / (Z + d);
  
  return {'x': distanceFactor * X, 'y': distanceFactor * Y};
}

/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  context.clearRect(0,0,200,200);
  cube.draw();
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
  var document = popUp.document;
  
  var canvas = document.createElement("canvas");
  
  canvas.setAttribute("id", "graph");
  canvas.setAttribute("width", "400");
  canvas.setAttribute("height", "400");
  
  document.body.appendChild(canvas);
  
  context = canvas.getContext("2d");
  
  printer = new Printer3D(context);
}

/**
 * Called once at the end of the animation.
 */
function tearDown(e: Error) {
  popUp.close();
  if (e) {
    alert(e.message);
  }
}

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
