// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

// Global Variables.
var popUp: Window = window.open("", "", "width=800, height=800", false);
var context: CanvasRenderingContext2D;
var printer: Printer3D;

class Printer3D {
  private context2D: CanvasRenderingContext2D;
  private d: number;
  constructor(context2D: CanvasRenderingContext2D, d: number) {
    this.context2D = context2D;
    this.d = d;
  }
  beginPath(): void {
    this.context2D.beginPath();
  }
  stroke(): void {
    this.context2D.stroke();
  }
  moveTo(x: number, y: number, z: number): void {
    var point = perspective(x, y, z, this.d);
    this.context2D.moveTo(point.x+200, point.y+200);
  }
  lineTo(x: number, y: number, z: number): void {
    var point = perspective(x, y, z, this.d);
    this.context2D.lineTo(point.x+200, point.y+200);
  }
}

class Cube {
  public position: eight.Euclidean3
  private corners: eight.Euclidean3[];
  constructor(position: eight.Euclidean3) {
    this.position = position;
    this.corners = [];
    this.corners.push(eight.vectorE3(-100, +100, -100));
    this.corners.push(eight.vectorE3(-100, -100, -100));
    this.corners.push(eight.vectorE3(+100, -100, -100));
    this.corners.push(eight.vectorE3(+100, +100, -100));
    this.corners.push(eight.vectorE3(-100, +100, +100));
    this.corners.push(eight.vectorE3(-100, -100, +100));
    this.corners.push(eight.vectorE3(+100, -100, +100));
    this.corners.push(eight.vectorE3(+100, +100, +100));
  }
  draw()
  {
    // front face
    printer.beginPath();
    printer.moveTo(this.position.x + this.corners[0].x, this.position.y + this.corners[0].y, this.position.z + this.corners[0].z);
    printer.lineTo(this.position.x + this.corners[1].x, this.position.y + this.corners[1].y, this.position.z + this.corners[1].z);
    printer.lineTo(this.position.x + this.corners[2].x, this.position.y + this.corners[2].y, this.position.z + this.corners[2].z);
    printer.lineTo(this.position.x + this.corners[3].x, this.position.y + this.corners[3].y, this.position.z + this.corners[3].z);
    printer.lineTo(this.position.x + this.corners[0].x, this.position.y + this.corners[0].y, this.position.z + this.corners[0].z);
    printer.stroke();

    // back face
    printer.beginPath();
    printer.moveTo(this.position.x + this.corners[4].x, this.position.y + this.corners[4].y, this.position.z + this.corners[4].z);
    printer.lineTo(this.position.x + this.corners[5].x, this.position.y + this.corners[5].y, this.position.z + this.corners[5].z);
    printer.lineTo(this.position.x + this.corners[6].x, this.position.y + this.corners[6].y, this.position.z + this.corners[6].z);
    printer.lineTo(this.position.x + this.corners[7].x, this.position.y + this.corners[7].y, this.position.z + this.corners[7].z);
    printer.lineTo(this.position.x + this.corners[4].x, this.position.y + this.corners[4].y, this.position.z + this.corners[4].z);
    printer.stroke();

    // LHS face
    printer.beginPath();
    printer.moveTo(this.position.x + this.corners[0].x, this.position.y + this.corners[0].y, this.position.z + this.corners[0].z);
    printer.lineTo(this.position.x + this.corners[4].x, this.position.y + this.corners[4].y, this.position.z + this.corners[4].z);
    printer.moveTo(this.position.x + this.corners[1].x, this.position.y + this.corners[1].y, this.position.z + this.corners[1].z);
    printer.lineTo(this.position.x + this.corners[5].x, this.position.y + this.corners[5].y, this.position.z + this.corners[5].z);
    printer.stroke();

    // RHS face
    printer.beginPath();
    printer.moveTo(this.position.x + this.corners[2].x, this.position.y + this.corners[2].y, this.position.z + this.corners[2].z);
    printer.lineTo(this.position.x + this.corners[6].x, this.position.y + this.corners[6].y, this.position.z + this.corners[6].z);
    printer.moveTo(this.position.x + this.corners[3].x, this.position.y + this.corners[3].y, this.position.z + this.corners[3].z);
    printer.lineTo(this.position.x + this.corners[7].x, this.position.y + this.corners[7].y, this.position.z + this.corners[7].z);
    printer.stroke();

    // top face
    // bottom face
  }
}

var cube = new Cube(eight.vectorE3(0, 0, 200));

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
  canvas.setAttribute("width", "800");
  canvas.setAttribute("height", "800");
  
  document.body.appendChild(canvas);
  
  context = canvas.getContext("2d");
  
  printer = new Printer3D(context, 100);
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
