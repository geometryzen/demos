/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

/**
 * 
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

function colorFromAngle(theta: number): Color {
  var sextant = ((theta / Math.PI) * 3) % 6;
  if (sextant >= 0 && sextant < 1) {
    return new Color(1.0,0.5,0.0);
  }
  else if (sextant >= 1 && sextant < 2) {
    return new Color(1.0,0.5,0.0);
  }
  else if (sextant >= 2 && sextant < 3) {
    return new Color(0.0,1.0,0.5);
  }
  else if (sextant >= 3 && sextant < 4) {
    return new Color(0.0,0.5,1.0);
  }
  else if (sextant >= 4 && sextant < 5) {
    return new Color(0.5,0.0,1.0);
  }
  else if (sextant >= 5 && sextant < 6) {
    return new Color(1.0,0.0,0.5);
  }
  else {
    return new Color(0.0,0.0,0.0);
  }
}

class Canvas {
  public backgroundColor: Color = new Color(127, 127, 127);
  private _window: Window;
  private _width;
  private _height;
  private _context;
  constructor(width: number, height: number) {
    this._width = width;
    this._height = height;
    this._window = window.open("", "", "width=" + width + ", height=" + height, false);
    
    var popDoc: Document = this._window.document;
    
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
    this._window.close();
  }
}

var canvas = new Canvas(800, 600);

var angle = 0;

canvas.backgroundColor = colorFromAngle(2 * Math.PI * Math.random());

function animate() {
  angle += 0.1;
  canvas.backgroundColor = colorFromAngle(angle);
  canvas.draw();
  
  window.requestAnimationFrame(animate);
}

var frame: number = window.requestAnimationFrame(animate);

animate();
