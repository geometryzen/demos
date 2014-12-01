/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;
var WIDTH = 800;
var HEIGHT = 600;

/**
 * A color value.
 */
class Color {
  private _red: number;
  private _green: number;
  private _blue: number;
  constructor(red: number, green: number, blue: number) {
    this._red = red;
    this._green = green;
    this._blue = blue;
  }
  public asFillStyle() {
    return "rgb(" + Math.floor(this._red*255) + ", " + Math.floor(this._green*255) + "," + Math.floor(this._blue*255) + ")"
  }
}

/**
 * Converts an angle to a color on a color wheel.
 */
function colorFromAngle(theta: number): Color {
  function normalizeAngle(angle: number) {
    if (angle > 2 * Math.PI) {
      return normalizeAngle(angle - 2 * Math.PI);
    }
    else if (angle < 0) {
      return normalizeAngle(angle + 2 * Math.PI);
    }
    else {
      return angle;
    }
  }
  var sextant = ((normalizeAngle(theta) / Math.PI) * 3) % 6;
  if (sextant >= 0 && sextant < 1) {
    return new Color(1.0,sextant-0,0.0);
  }
  else if (sextant >= 1 && sextant < 2) {
    return new Color(2-sextant,1.0,0.0);
  }
  else if (sextant >= 2 && sextant < 3) {
    return new Color(0.0,1.0,sextant-2);
  }
  else if (sextant >= 3 && sextant < 4) {
    return new Color(0.0,4-sextant,1.0);
  }
  else if (sextant >= 4 && sextant < 5) {
    return new Color(sextant-4,0.0,1.0);
  }
  else if (sextant >= 5 && sextant < 6) {
    return new Color(1.0,0.0,6-sextant);
  }
  else {
    return new Color(0.0,0.0,0.0);
  }
}

class Canvas {
  public backgroundColor: Color = new Color(127, 127, 127);
  public wnd: Window;
  private _width;
  private _height;
  public context: CanvasRenderingContext2D;
  constructor(width: number, height: number) {
    this._width = width;
    this._height = height;
    this.wnd = window.open("", "", "width=" + width + ", height=" + height, false);
    
    var popDoc: Document = this.wnd.document;
    
    var canvas: HTMLCanvasElement = popDoc.createElement("canvas");
    
    canvas.setAttribute("id", "graph");
    canvas.setAttribute("width",  width.toString());
    canvas.setAttribute("height", height.toString());
    
    popDoc.body.appendChild(canvas);
    // Remove the margin that pushes the canvas.
    popDoc.body.style.margin = "0";
    
    this.context = canvas.getContext("2d");
  }
  
  public draw() {
    this.context.fillStyle = this.backgroundColor.asFillStyle() 
    this.context.fillRect(0, 0, this._width, this._height);
  }

  public close() {
    this.wnd.close();
  }
}

interface WindowAnimation {
  setUp(): void;
  tick(elapsed: number): void;
  terminate(elapsed: number): boolean;
  tearDown(ex: any): void;
  window(): Window;
}

/**
 * Handles the control of an animation.
 */
var windowAnimationRunner = function(animation: WindowAnimation) {
    var win = animation.window();
    var escKeyPressed = false;
    var pauseKeyPressed = false;
    var enterKeyPressed = false;
    var startTime: number = null;
    var elapsed: number = null;
    var MILLIS_PER_SECOND = 1000;
    var requestID: number = null;
    var exception: any = null;

    var animate: FrameRequestCallback = function(timestamp) {
        if (startTime) {
            elapsed = timestamp - startTime;
        }
        else {
            startTime = timestamp;
            elapsed = 0;
        }

        if (escKeyPressed || animation.terminate(elapsed / MILLIS_PER_SECOND)) {
            escKeyPressed = false;

            win.cancelAnimationFrame(requestID);
            win.document.removeEventListener('keydown', onDocumentKeyDown, false);
            try {
                animation.tearDown(exception);
            }
            catch (e) {
                console.log(e);
            }
        }
        else {
            requestID = win.requestAnimationFrame(animate);
            try {
                animation.tick(elapsed / MILLIS_PER_SECOND);
            }
            catch (e) {
                exception = e;
                escKeyPressed = true;
            }
        }
    };

    var onDocumentKeyDown = function(event: KeyboardEvent) {
        if (event.keyCode == 27) {
            escKeyPressed = true;
            event.preventDefault();
        }
        else if (event.keyCode == 19) {
            pauseKeyPressed = true;
            event.preventDefault();
        }
        else if (event.keyCode == 13) {
            enterKeyPressed = true;
            event.preventDefault();
        }
    };

    var that =
        {
            start: function() {
                animation.setUp();
                win.document.addEventListener('keydown', onDocumentKeyDown, false);
                requestID = win.requestAnimationFrame(animate);
            },
            stop: function() {
                escKeyPressed = true;
            }
        };

    return that;
};

class Complex {
  public x: number;
  public y: number;
  constructor(x: number, y:number) {
    this.x = x;
    this.y = y;
  }
  arg(): number {
    return Math.atan2(this.y, this.x);
  }
  add(that: Complex): Complex {
    return new Complex(this.x + that.x, this.y + that.y);
  }
  subtract(that: Complex): Complex {
    return new Complex(this.x - that.x, this.y - that.y);
  }
  multiply(that: Complex): Complex {
    return new Complex(this.x * that.x - this.y * that.y, this.x * that.y + this.y * that.x);
  }
  toString(): String {
    return this.x + "+" + this.y + "i";
  }
}

var R = new Complex(Math.cos(0.01), Math.sin(0.01));

var f = function(z: Complex): Complex {
  var z3 = z.multiply(z).multiply(z);
  var sz = new Complex(6,0).multiply(z);
  var tw = new Complex(20,0);
  return z3.add(sz).subtract(tw);
};

class MinMax {
  public min: number;
  public max: number;
  constructor(min: number, max: number) {
    this.min = min;
    this.max = max;
  }
}

class MyAnimation implements WindowAnimation {
  private _canvas = new Canvas(WIDTH, HEIGHT);
  private _z: Complex = new Complex(1,0);
  private xRange: MinMax;
  private yRange: MinMax;
  constructor(xRange: MinMax, yRange: MinMax) {
    this.xRange = xRange;
    this.yRange = yRange;
  }
  setUp() {
    
  }
  tick(elapsed: number) {
    this._z = this._z.multiply(R);
    this._canvas.backgroundColor = colorFromAngle(this._z.arg());
    for (var X=0;X<WIDTH;X++) {
      for (var Y=0;Y<HEIGHT;Y++) {
        var x = (X / WIDTH) * (this.xRange.max - this.xRange.min) + this.xRange.min;
        var y = ((HEIGHT-Y)/HEIGHT) * (this.yRange.max - this.yRange.min) + this.yRange.min;
        var z = new Complex(x,y);
        this._canvas.context.fillStyle = colorFromAngle(f(z).arg()).asFillStyle();
        this._canvas.context.fillRect(X,Y,1,1);
      }
    }
  }
  terminate(elapsed: number) {
    return false;
  }
  tearDown(ex: any) {
    this._canvas.close();
  }
  window() {
    return this._canvas.wnd;
  }
}

var war = windowAnimationRunner(new MyAnimation(new MinMax(-10,+10), new MinMax(-10,+10)));
war.start();
