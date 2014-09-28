// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

// Global Variables.
var popUp: Window = window.open("", "", "width=800, height=800", false);
var context: CanvasRenderingContext2D;
var printer: Printer3D;
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);
var canvasDistance = 100;

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
    this.context2D.moveTo(point.x+400, point.y+400);
  }
  lineTo(x: number, y: number, z: number): void {
    var point = perspective(x, y, z, this.d);
    this.context2D.lineTo(point.x+400, point.y+400);
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
    var T = reverse(R);
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
    context.strokeStyle = "#0000FF";
    printer.moveTo(this.position.x + corners[0].x, this.position.y + corners[0].y, this.position.z + corners[0].z);
    printer.lineTo(this.position.x + corners[4].x, this.position.y + corners[4].y, this.position.z + corners[4].z);
    printer.moveTo(this.position.x + corners[1].x, this.position.y + corners[1].y, this.position.z + corners[1].z);
    printer.lineTo(this.position.x + corners[5].x, this.position.y + corners[5].y, this.position.z + corners[5].z);
    printer.stroke();

    // RHS face
    printer.beginPath();
    context.strokeStyle = "#0000FF";
    printer.moveTo(this.position.x + corners[2].x, this.position.y + corners[2].y, this.position.z + corners[2].z);
    printer.lineTo(this.position.x + corners[6].x, this.position.y + corners[6].y, this.position.z + corners[6].z);
    printer.moveTo(this.position.x + corners[3].x, this.position.y + corners[3].y, this.position.z + corners[3].z);
    printer.lineTo(this.position.x + corners[7].x, this.position.y + corners[7].y, this.position.z + corners[7].z);
    printer.stroke();

    // top face
    // bottom face
  }
}

var cube = new Cube(eight.vectorE3(0, 0, 200), eight.scalarE3(1));

function perspective(X: number, Y: number, Z: number, d: number): {x:number; y:number} {
  /**
   * The distance factor determines how much the X and Y components are reduced by the distance (Z + d) from the viewer.
   */
  var distanceFactor = d / (Z + d);
  
  return {'x': distanceFactor * X, 'y': distanceFactor * Y};
}

function reverse(m: eight.Euclidean3) {
  return new eight.Euclidean3(m.w, m.x, m.y, m.z,-m.xy,-m.yz,-m.zx, m.xyz);
}

function vanishingPoint(v: eight.Euclidean3) : {x: number; y: number} {
  var norm = v.norm();
  var normalized = v.div(norm);
  var x = canvasDistance * v.x / v.z;
  var y = canvasDistance * v.y / v.z;
  return {'x':x,'y':y};
}

/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  // Set the background color to gray.
  context.fillStyle = "#666666"
  context.fillRect(0,0,800,800);
  
  // Draw the cube at the appropriate attitude.
  var TAO = Math.PI * 2;
  var omega = TAO / 60.0;
  var theta = omega * time;
  var c = eight.scalarE3(Math.cos(theta/2));
  var s = eight.scalarE3(Math.sin(theta/2));
  var one = eight.scalarE3(1);
  var sqrt2 = eight.scalarE3(Math.sqrt(2));
  var a = eight.vectorE3(1,0,0);
  var b = eight.vectorE3(0,0,1);
  var R = c.sub(s.mul(a.wedge(b)));
  cube.attitude = R;
  cube.draw();
  
  // Draw the vanishing points.
  var T = reverse(R);
  var p1 = vanishingPoint(R.mul(e1).mul(T));
  context.beginPath();
  context.strokeStyle = "#FF0000";
  context.moveTo(p1.x-10+400, p1.y+400);
  context.lineTo(p1.x+10+400, p1.y+400);
  context.moveTo(p1.x+400, p1.y-10+400);
  context.lineTo(p1.x+400, p1.y+10+400);
  context.stroke();

  var p2 = vanishingPoint(R.mul(e2).mul(T));
  context.beginPath();
  context.strokeStyle = "#00FF00";
  context.moveTo(p2.x-10+400, p2.y+400);
  context.lineTo(p2.x+10+400, p2.y+400);
  context.moveTo(p2.x+400, p2.y-10+400);
  context.lineTo(p2.x+400, p2.y+10+400);
  context.stroke();

  var p3 = vanishingPoint(R.mul(e3).mul(T));
  context.beginPath();
  context.strokeStyle = "#0000FF";
  context.moveTo(p3.x-10+400, p3.y+400);
  context.lineTo(p3.x+10+400, p3.y+400);
  context.moveTo(p3.x+400, p3.y-10+400);
  context.lineTo(p3.x+400, p3.y+10+400);
  context.stroke();
  
  
  context.strokeRect(0,0,canvasDistance,canvasDistance);
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
  
  printer = new Printer3D(context, canvasDistance);
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
