// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

var CANVAS_HEIGHT = 800;
var CANVAS_WIDTH  = 800;

// Global Variables.
var popUp: Window = window.open("", "", "width=800, height=800", false);
var context: CanvasRenderingContext2D;
var printer: Printer3D;
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);
var canvasDistance = 100;
var arcBall: ArcBall;

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
    var x = -(clientX - 400) / 400;
    var y = -(clientY - 400) / 400;
    var z = Math.sqrt(1 - x * x - y * y);
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
  context.fillStyle = "#555555"
  context.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  
  var R = arcBall.rotor;
  
  // Draw the cube at the appropriate attitude.
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
  
  context.strokeStyle = "#FFFFFF";
  context.strokeRect(0+400-canvasDistance,0+400-canvasDistance,canvasDistance*2,canvasDistance*2);
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
  var document = popUp.document;
  
  var canvas = document.createElement("canvas");
  
  canvas.setAttribute("id", "graph");
  canvas.setAttribute("width",  CANVAS_WIDTH.toString());
  canvas.setAttribute("height", CANVAS_HEIGHT.toString());
  
  document.body.appendChild(canvas);
  
  context = canvas.getContext("2d");
  
  printer = new Printer3D(context, canvasDistance);
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
