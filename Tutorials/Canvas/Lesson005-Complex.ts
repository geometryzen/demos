/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

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
  var sextant = ((theta / Math.PI) * 3) % 6;
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
  private _context;
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
    
    this._context = canvas.getContext("2d");
  }
  
  public draw() {
    this._context.fillStyle = this.backgroundColor.asFillStyle() 
    this._context.fillRect(0, 0, this._width, this._height);
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

class MyAnimation implements WindowAnimation {
  private _canvas = new Canvas(800, 600);
  private z: Complex = new Complex(0,1);
  setUp() {
    
  }
  tick(elapsed: number) {
    this._canvas.backgroundColor = colorFromAngle(this.z.arg());
    this._canvas.draw();
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
}

var war = windowAnimationRunner(new MyAnimation());
war.start();
