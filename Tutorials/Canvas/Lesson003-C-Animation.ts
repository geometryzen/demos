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

interface Animation {
  tick(): void;
  window();
}

/**
 * Handles the control of an animation.
 */
class WindowAnimationRunner {
  private _animation: Animation;
  private _animate;
  constructor(animation: Animation) {
    this._animation = animation;
    var self = this;
    var animate = function() {
      animation.tick();
      animation.window().requestAnimationFrame(animate);
    }
    this._animate = animate;
  }
  /**
   * Starts the animation.
   */
  public start() {
    this._animation.window().requestAnimationFrame(this._animate);
  }
}

class MyAnimation implements Animation {
  private _canvas = new Canvas(800, 600);
  private _angle: number = 0;
  tick() {
    this._angle += 0.01;
    this._canvas.backgroundColor = colorFromAngle(this._angle);
    this._canvas.draw();
  }
  window() {
    return this._canvas.wnd;
  }
}

var anime = new MyAnimation();

var war = new WindowAnimationRunner(anime);
war.start();
