/**
 * Demonstrates the vanishing points from 3D space projected onto a 2D canvas.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

interface Perspective {
  transform(X: number, Y:number, Z: number): {x: number; y: number};
}

class ConformalPerspective implements Perspective {
  public s: number;
  public d: number;
  constructor(d: number, s: number) {
    this.d = d;
    this.s = s;
  }
  transform(X: number, Y:number, Z:number): {x: number; y: number} {
    var vx = X;
    var vy = Y;
    var vz = this.s + Z;
  
    var m = Math.sqrt(vx * vx + vy * vy + vz * vz)
    
    var nx = this.d * vx / m;
    var ny = this.d * vy / m;
    var nz = this.d * vz / m;
    
    var distanceFactor = this.d / (this.d + nz);
  
    var x = distanceFactor * nx;
    var y = distanceFactor * ny;
  
    return {'x': x, 'y': y};
  }
}

class LinearPerspective implements Perspective {
  public s: number;
  public d: number;
  constructor(d: number, s: number) {
    this.d = d;
    this.s = s;
  }
  transform(X: number, Y:number, Z:number): {x: number; y: number} {
    var distanceFactor = this.d / (this.d + this.s + Z);
    
    var x = distanceFactor * X;
    var y = distanceFactor * Y;
  
    return {'x': x, 'y': y};
  }
}

var WINDOW_HEIGHT = 800;
var WINDOW_WIDTH  = 1800;
var WINDOW_HALF_HEIGHT = WINDOW_HEIGHT / 2;
var WINDOW_HALF_WIDTH  = WINDOW_WIDTH / 2;
var CANVAS_HEIGHT = 800;
var CANVAS_WIDTH  = 1800;
var CANVAS_HALF_HEIGHT = CANVAS_HEIGHT / 2;
var CANVAS_HALF_WIDTH  = CANVAS_WIDTH / 2;
var CANVAS_DISTANCE =40;
var IMAGE_DISTANCE = 400;
var ZOOM = 20

// Global Variables.
var popUp: Window = window.open("", "", "width=" + WINDOW_WIDTH + ", height=" + WINDOW_HEIGHT, false);
var context: CanvasRenderingContext2D;
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);
var arcBall: ArcBall;
var printer;
  
class Printer3D {
  private context2D: CanvasRenderingContext2D;
  private zoom: number;
  private perspective: Perspective;
  constructor(context2D: CanvasRenderingContext2D, zoom: number, perspective: Perspective ) {
    this.context2D = context2D;
    this.zoom = zoom;
    this.perspective = perspective;
  }
  beginPath(): void {
    this.context2D.beginPath();
  }
  stroke(): void {
    this.context2D.stroke();
  }
  moveTo(x: number, y: number, z: number): void {
    var point = this.perspective.transform(x, y, z);
    this.context2D.moveTo(point.x * this.zoom + CANVAS_HALF_WIDTH, point.y * this.zoom + CANVAS_HALF_HEIGHT);
  }
  lineTo(x: number, y: number, z: number): void {
    var point = this.perspective.transform(x, y, z);
    this.context2D.lineTo(point.x * this.zoom + CANVAS_HALF_WIDTH, point.y * this.zoom + CANVAS_HALF_HEIGHT);
  }
}

class ArcBall {
  private start: eight.Euclidean3;
  public rotor: eight.Euclidean3 = eight.scalarE3(1);
  private win: Window;
  private down: boolean = false;
  private a: eight.Euclidean3;
  private b: eight.Euclidean3;
  private mousedown: (ev: MouseEvent) => void;
  private mouseup: (ev: MouseEvent) => void;
  private mousemove: (ev: MouseEvent) => void;
  constructor(win: Window) {
    this.win = win;
    this.mousedown = ArcBall.makeMouseDown(this);
    this.mouseup = ArcBall.makeMouseUp(this);
    this.mousemove = ArcBall.makeMouseMove(this);
  }
  private static vectorFromMouse(clientX: number, clientY: number): eight.Euclidean3 {
    var x = (clientX - CANVAS_HALF_WIDTH) / CANVAS_HALF_WIDTH;
    var y = (clientY - CANVAS_HALF_HEIGHT) / CANVAS_HALF_HEIGHT;
    // The negative sign for z arises because the arc ball is a hemisphere in the
    // directin of the user, which is negative z.
    var z = -Math.sqrt(1 - x * x - y * y);
    return eight.vectorE3(x, y, z);
  }
  private static computeRotor(a: eight.Euclidean3, b: eight.Euclidean3) {
    var one = eight.scalarE3(1);
    var rotor = one.add(b.mul(a)).div(a.add(b).norm());
    return rotor;
  }
  private static makeMouseDown(arcBall: ArcBall) {
    return function(ev: MouseEvent) {
      arcBall.down = true;
      arcBall.a = ArcBall.vectorFromMouse(ev.clientX, ev.clientY);
      arcBall.start = arcBall.rotor;
    }
  }
  private static makeMouseUp(arcBall: ArcBall) {
    return function(ev: MouseEvent) {
      arcBall.down = false;
      arcBall.b = ArcBall.vectorFromMouse(ev.clientX, ev.clientY);
      arcBall.rotor = ArcBall.computeRotor(arcBall.a, arcBall.b).mul(arcBall.start);
    }
  }
  private static makeMouseMove(arcBall: ArcBall) {
    return function(ev: MouseEvent) {
      if (arcBall.down) {
        arcBall.b = ArcBall.vectorFromMouse(ev.clientX, ev.clientY)
        arcBall.rotor = ArcBall.computeRotor(arcBall.a, arcBall.b).mul(arcBall.start);
      }
    }
  }
  setUp(): void {
    this.win.addEventListener('mousedown', this.mousedown);
    this.win.addEventListener('mouseup', this.mouseup);
    this.win.addEventListener('mousemove', this.mousemove);
  }
  tearDown(): void {
    this.win.removeEventListener('mousedown', this.mousedown);
    this.win.removeEventListener('mouseup', this.mouseup);
    this.win.removeEventListener('mousemove', this.mousemove);
  }
}

interface Drawable {
  attitude: eight.Euclidean3;
  draw(printer: Printer3D)
}

class Circle implements Drawable {
  public position: eight.Euclidean3;
  public attitude: eight.Euclidean3;
  public radius = 25;
  private points: eight.Euclidean3[];
  constructor(position: eight.Euclidean3, attitude: eight.Euclidean3) {
    this.position = position;
    this.attitude = attitude;
    this.points = [];
    for (var i=0;i<360;i++) {
      var theta = (Math.PI / 180) * i;
      var c = Math.cos(theta);
      var s = Math.sin(theta);
      var v = eight.vectorE3(position.x + this.radius * c, position.y, position.z + this.radius * s);
      this.points.push(v);
    }
  }
  draw(printer: Printer3D) {
    var R = this.attitude;
    var T = reverse(R);
    var points = this.points.map(function(value) {return R.mul(value).mul(T);});
    // front face
    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.moveTo(points[0].x, points[0].y, points[0].z);
    for (var i=1;i<360;i++) {
      printer.lineTo(points[i].x, points[i].y, points[i].z);
    }
    printer.stroke();
    
  }
}

class Cube implements Drawable {
  public position: eight.Euclidean3;
  public attitude: eight.Euclidean3;
  public size: number = 10;
  private corners: eight.Euclidean3[];
  constructor(position: eight.Euclidean3, attitude: eight.Euclidean3) {
    this.position = position;
    this.attitude = attitude;
    this.corners = [];
    
    var sz = this.size;
    this.corners.push(eight.vectorE3(position.x - sz, position.y + sz, position.z - sz));
    this.corners.push(eight.vectorE3(position.x - sz, position.y - sz, position.z - sz));
    this.corners.push(eight.vectorE3(position.x + sz, position.y - sz, position.z - sz));
    this.corners.push(eight.vectorE3(position.x + sz, position.y + sz, position.z - sz));
    this.corners.push(eight.vectorE3(position.x - sz, position.y + sz, position.z + sz));
    this.corners.push(eight.vectorE3(position.x - sz, position.y - sz, position.z + sz));
    this.corners.push(eight.vectorE3(position.x + sz, position.y - sz, position.z + sz));
    this.corners.push(eight.vectorE3(position.x + sz, position.y + sz, position.z + sz));
  }
  draw(printer: Printer3D)
  {
    var R = this.attitude;
    var T = reverse(R);
    var corners = this.corners.map(function(value) {return R.mul(value).mul(T);});
    // front face
    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.moveTo(corners[0].x, corners[0].y, corners[0].z);
    printer.lineTo(corners[1].x, corners[1].y, corners[1].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(corners[1].x, corners[1].y, corners[1].z);
    printer.lineTo(corners[2].x, corners[2].y, corners[2].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.lineTo(corners[2].x, corners[2].y, corners[2].z);
    printer.lineTo(corners[3].x, corners[3].y, corners[3].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(corners[3].x, corners[3].y, corners[3].z);
    printer.lineTo(corners[0].x, corners[0].y, corners[0].z);
    printer.stroke();

    // back face
    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.moveTo(corners[4].x, corners[4].y, corners[4].z);
    printer.lineTo(corners[5].x, corners[5].y, corners[5].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(corners[5].x, corners[5].y, corners[5].z);
    printer.lineTo(corners[6].x, corners[6].y, corners[6].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#00FF00";
    printer.lineTo(corners[6].x, corners[6].y, corners[6].z);
    printer.lineTo(corners[7].x, corners[7].y, corners[7].z);
    printer.stroke();

    printer.beginPath();
    context.strokeStyle = "#FF0000";
    printer.lineTo(corners[7].x, corners[7].y, corners[7].z);
    printer.lineTo(corners[4].x, corners[4].y, corners[4].z);
    printer.stroke();

    // LHS face
    printer.beginPath();
    context.strokeStyle = "#0000FF";
    printer.moveTo(corners[0].x, corners[0].y, corners[0].z);
    printer.lineTo(corners[4].x, corners[4].y, corners[4].z);
    printer.moveTo(corners[1].x, corners[1].y, corners[1].z);
    printer.lineTo(corners[5].x, corners[5].y, corners[5].z);
    printer.stroke();

    // RHS face
    printer.beginPath();
    context.strokeStyle = "#0000FF";
    printer.moveTo(corners[2].x, corners[2].y, corners[2].z);
    printer.lineTo(corners[6].x, corners[6].y, corners[6].z);
    printer.moveTo(corners[3].x, corners[3].y, corners[3].z);
    printer.lineTo(corners[7].x, corners[7].y, corners[7].z);
    printer.stroke();

    // top face
    // bottom face
  }
}

var n = 5;
var separation = 60;
var cubes: Drawable[] = [];
for (var i=-n;i<=n;i++) {
  var j = 0.5;
//  for (var j=-n;j<=n;j++) {
    for (var k=-n;k<=n;k++) {
      cubes.push(new Circle(eight.vectorE3(i*separation, j*separation, k*separation), eight.scalarE3(1)));
    }
//  }
}

function reverse(m: eight.Euclidean3) {
  return new eight.Euclidean3(m.w, m.x, m.y, m.z,-m.xy,-m.yz,-m.zx, -m.xyz);
}
/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  // Set the background color to gray.
  context.fillStyle = "#555555";
  context.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  
  var R = arcBall.rotor;
  
  // Draw the cube at the appropriate attitude.
  for (var i=0;i<cubes.length;i++) {
    cubes[i].attitude = R
    cubes[i].draw(printer);
  }
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
  arcBall = new ArcBall(popUp);
  arcBall.setUp();

  var popDoc = popUp.document;
  
  var canvas = popDoc.createElement("canvas");
  
  canvas.setAttribute("id", "graph");
  canvas.setAttribute("width",  CANVAS_WIDTH.toString());
  canvas.setAttribute("height", CANVAS_HEIGHT.toString());
  
  popDoc.body.appendChild(canvas);
  // Remove the margin that pushes the canvas.
  popDoc.body.style.margin = "0";
  
  context = canvas.getContext("2d");
  //printer = new Printer3D(context, ZOOM, new LinearPerspective(CANVAS_DISTANCE, IMAGE_DISTANCE));}
  printer = new Printer3D(context, ZOOM, new ConformalPerspective(CANVAS_DISTANCE, IMAGE_DISTANCE));}

/**
 * Called once at the end of the animation.
 */
function tearDown(e: Error) {
  arcBall.tearDown();
  popUp.close();
  if (e) {
    alert(e.message);
  }
}

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();
