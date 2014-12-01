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

/**
 * Handles the control of an animation.
 */
class WindowAnimationRunner {
  private _wnd: Window;
  private _animate;
  constructor(tick: () => void, w: Window) {
    this._wnd = w;
    var self = this;
    var animate = function() {
      tick();
      w.requestAnimationFrame(animate);
    }
    this._animate = animate;
  }
  /**
   * Starts the animation.
   */
  public start() {
    this._wnd.requestAnimationFrame(this._animate);
  }
}

var canvas = new Canvas(800, 600);

var angle = 0;

function draw(): void {
  angle += 0.01;
  canvas.backgroundColor = colorFromAngle(angle);
  console.log("angle: " + angle);
  canvas.draw();
}

var war = new WindowAnimationRunner(draw, canvas.wnd);
war.start();
