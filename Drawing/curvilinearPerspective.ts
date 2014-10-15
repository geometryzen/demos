/**
 * Demonstrates the vanishing points from 3D space projected onto a 2D canvas.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

var WINDOW_HEIGHT = 800;
var WINDOW_WIDTH  = 800;
var WINDOW_HALF_HEIGHT = WINDOW_HEIGHT / 2;
var WINDOW_HALF_WIDTH  = WINDOW_WIDTH / 2;
var CANVAS_HEIGHT = 800;
var CANVAS_WIDTH  = 800;
var CANVAS_HALF_HEIGHT = CANVAS_HEIGHT / 2;
var CANVAS_HALF_WIDTH  = CANVAS_WIDTH / 2;
var CANVAS_DISTANCE = 1;
var IMAGE_DISTANCE = 100;
var ZOOM = 30

// Global Variables.
var popUp: Window = window.open("", "", "width=" + WINDOW_WIDTH + ", height=" + WINDOW_HEIGHT, false);
var context: CanvasRenderingContext2D;
var printer: Printer3D;
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);
var arcBall: ArcBall;

class Printer3D {
  private context2D: CanvasRenderingContext2D;
  /**
   * Viewing distance to screen.
   */
  private d: number;
  /**
   * Distance screen to origin.
   */
  private s: number;
  private zoom: number;
  constructor(context2D: CanvasRenderingContext2D, d: number, s: number, zoom: number) {
    this.context2D = context2D;
    this.d = d;
    this.s = s;
    this.zoom = zoom;
  }
  beginPath(): void {
    this.context2D.beginPath();
  }
  stroke(): void {
    this.context2D.stroke();
  }
  moveTo(x: number, y: number, z: number): void {
    var point = perspective(x, y, z, this.d, this.s);
    this.context2D.moveTo(point.x * this.zoom + CANVAS_HALF_WIDTH, point.y * this.zoom + CANVAS_HALF_HEIGHT);
  }
  lineTo(x: number, y: number, z: number): void {
    var point = perspective(x, y, z, this.d, this.s);
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
  constructor(win: Window) {
    this.win = win;
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
  setUp(): void {
    var self = this;
    this.win.addEventListener('mousedown', function(ev: MouseEvent) {
      self.down = true;
      self.a = ArcBall.vectorFromMouse(ev.clientX, ev.clientY);
      self.start = self.rotor;
    });
    this.win.addEventListener('mouseup', function(ev: MouseEvent) {
      self.down = false;
      self.b = ArcBall.vectorFromMouse(ev.clientX, ev.clientY);
      self.rotor = ArcBall.computeRotor(self.a, self.b).mul(self.start);
    });
    this.win.addEventListener('mousemove', function(ev: MouseEvent) {
      if (self.down) {
        self.b = ArcBall.vectorFromMouse(ev.clientX, ev.clientY)
        self.rotor = ArcBall.computeRotor(self.a, self.b).mul(self.start);
      }
    });
  }
  tearDown(): void {
    
  }
}

class Cube {
  public position: eight.Euclidean3;
  public attitude: eight.Euclidean3;
  public size: number = 1;
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
  draw()
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

var n = 20;
var separation = 5;
var cubes: Cube[] = [];
for (var i=-n;i<=n;i++) {
  var j = 0;
//  for (var j=-n;j<=n;j++) {
    for (var k=-n;k<=n;k++) {
      cubes.push(new Cube(eight.vectorE3(i*separation, j*separation, k*separation), eight.scalarE3(1)));
    }
//  }
}

function perspective(X: number, Y: number, Z: number, d: number, s:number): {x:number; y:number} {

  var vx = X;
  var vy = Y;
  var vz = s + Z;

  var m = Math.sqrt(vx * vx + vy * vy + vz * vz)
  
  var nx = d * vx / m;
  var ny = d * vy / m;
  var nz = d * vz / m;
  
  var distanceFactor = d / (d + nz);

  var x = distanceFactor * nx;
  var y = distanceFactor * ny;

  return {'x': x, 'y': y};
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
    cubes[i].draw();
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
  
  printer = new Printer3D(context, CANVAS_DISTANCE, IMAGE_DISTANCE, ZOOM);
}

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
