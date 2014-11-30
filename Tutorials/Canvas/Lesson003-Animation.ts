/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

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
    return "rgb(" + this._red + ", " + this._green + "," + this._blue + ")"
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


function animate() {
  canvas.backgroundColor = new Color(255, 255, 0);
  canvas.draw();
}

animate();
