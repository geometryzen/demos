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
var CANVAS_DISTANCE = 100;

// Global Variables.
var popUp: Window = window.open("", "", "width=" + WINDOW_WIDTH + ", height=" + WINDOW_HEIGHT, false);
var context: CanvasRenderingContext2D;

var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);
var arcBall: ArcBall;

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

/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  // Set the background color to gray.
  context.fillStyle = "#555555";
  context.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  
  var R = arcBall.rotor;
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
