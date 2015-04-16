var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

/**
 * Demonstrates creating a 2D canvas and context.
 * Illustrates the fundamental theorem of algebra.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
//var unused: Window = window;
var WIDTH = 400;
var HEIGHT = 400;

class Canvas {
  public backgroundColor: blade.Color = new blade.Color(127, 127, 127);
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

/**
 * The complex function that we wish to visualize.
 */
function foo(z: blade.Complex) {
    return z * (z * (z + 1) + 6) - 20;
}

class MinMax {
  public min: number;
  public max: number;
  constructor(min: number, max: number) {
    this.min = min;
    this.max = max;
  }
  transform(s: number): number {
    return s * (this.max - this.min) + this.min;
  }
}

function sigmoid(t: number) {
  return 1 / (1 + Math.exp(-t*t/2000));
}

function lightnessFromMagnitude(r: number) {
  return 2 * sigmoid(r) - 1.0
}

class ComplexPlane {
  private _canvas = new Canvas(WIDTH, HEIGHT);
  private xRange: MinMax;
  private yRange: MinMax;
  private f: (z: blade.Complex) => blade.Complex;
  constructor(xRange: MinMax, yRange: MinMax, f: (z: blade.Complex)=>blade.Complex) {
    this.xRange = xRange;
    this.yRange = yRange;
    this.f = f;
  }
  draw() {
    for (var X=0;X<WIDTH;X++) {
      for (var Y=0;Y<HEIGHT;Y++) {
        var x = this.xRange.transform(X / WIDTH);
        var y = this.yRange.transform((HEIGHT-Y)/HEIGHT);
        var z = new blade.Complex(x,y);
        var H = this.f(z).arg();
        var S = 1;
        // var L = lightnessFromMagnitude(this.f(z).norm());
        var L = 0.5;
        this._canvas.context.fillStyle = blade.Color.fromHSL(H, S, L).asFillStyle();
        this._canvas.context.fillRect(X, Y, 1, 1);
      }
    }
  }
}

var R = 10;
var cp = new ComplexPlane(new MinMax(-R,+R), new MinMax(-R,+R), foo);
cp.draw();
