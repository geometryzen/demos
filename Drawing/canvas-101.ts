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
  public position: eight.Euclidean3;
  public attitude: eight.Euclidean3;
  private corners: eight.Euclidean3[];
  constructor(position: eight.Euclidean3, attitude: eight.Euclidean3) {
    this.position = position;
    this.attitude = attitude;
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
    var R = this.attitude;
    var T = new eight.Euclidean3(this.attitude.w,0,0,0,-this.attitude.xy,-this.attitude.yz,-this.attitude.zx,0);
    console.log(R.toStringIJK());
    console.log(T.toStringIJK());
    var corners = this.corners.map(function(value) {return R.mul(value).mul(T);});
    // front face
    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.moveTo(this.position.x + corners[0].x, this.position.y + corners[0].y, this.position.z + corners[0].z);
    printer.lineTo(this.position.x + corners[1].x, this.position.y + corners[1].y, this.position.z + corners[1].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(this.position.x + corners[1].x, this.position.y + corners[1].y, this.position.z + corners[1].z);
    printer.lineTo(this.position.x + corners[2].x, this.position.y + corners[2].y, this.position.z + corners[2].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.lineTo(this.position.x + corners[2].x, this.position.y + corners[2].y, this.position.z + corners[2].z);
    printer.lineTo(this.position.x + corners[3].x, this.position.y + corners[3].y, this.position.z + corners[3].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(this.position.x + corners[3].x, this.position.y + corners[3].y, this.position.z + corners[3].z);
    printer.lineTo(this.position.x + corners[0].x, this.position.y + corners[0].y, this.position.z + corners[0].z);
    printer.stroke();

    // back face
    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.moveTo(this.position.x + corners[4].x, this.position.y + corners[4].y, this.position.z + corners[4].z);
    printer.lineTo(this.position.x + corners[5].x, this.position.y + corners[5].y, this.position.z + corners[5].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(this.position.x + corners[5].x, this.position.y + corners[5].y, this.position.z + corners[5].z);
    printer.lineTo(this.position.x + corners[6].x, this.position.y + corners[6].y, this.position.z + corners[6].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.lineTo(this.position.x + corners[6].x, this.position.y + corners[6].y, this.position.z + corners[6].z);
    printer.lineTo(this.position.x + corners[7].x, this.position.y + corners[7].y, this.position.z + corners[7].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(this.position.x + corners[7].x, this.position.y + corners[7].y, this.position.z + corners[7].z);
    printer.lineTo(this.position.x + corners[4].x, this.position.y + corners[4].y, this.position.z + corners[4].z);
    printer.stroke();

    // LHS face
    printer.beginPath();
    printer.moveTo(this.position.x + corners[0].x, this.position.y + corners[0].y, this.position.z + corners[0].z);
    printer.lineTo(this.position.x + corners[4].x, this.position.y + corners[4].y, this.position.z + corners[4].z);
    printer.moveTo(this.position.x + corners[1].x, this.position.y + corners[1].y, this.position.z + corners[1].z);
    printer.lineTo(this.position.x + corners[5].x, this.position.y + corners[5].y, this.position.z + corners[5].z);
    printer.stroke();

    // RHS face
    printer.beginPath();
    printer.moveTo(this.position.x + corners[2].x, this.position.y + corners[2].y, this.position.z + corners[2].z);
    printer.lineTo(this.position.x + corners[6].x, this.position.y + corners[6].y, this.position.z + corners[6].z);
    printer.moveTo(this.position.x + corners[3].x, this.position.y + corners[3].y, this.position.z + corners[3].z);
    printer.lineTo(this.position.x + corners[7].x, this.position.y + corners[7].y, this.position.z + corners[7].z);
    printer.stroke();

    // top face
    // bottom face
  }
}

var TAO = Math.PI * 2;
var theta = TAO / 9;
var c = eight.scalarE3(Math.cos(theta/2));
var s = eight.scalarE3(Math.sin(theta/2));
var one = eight.scalarE3(1);
var sqrt2 = eight.scalarE3(Math.sqrt(2));
var a = eight.vectorE3(1,0,0);
var b = eight.vectorE3(0,0,1);
var R = c.sub(s.mul(a.wedge(b)));
console.log(R.toStringIJK());

var cube = new Cube(eight.vectorE3(0, 0, 200), R);

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
