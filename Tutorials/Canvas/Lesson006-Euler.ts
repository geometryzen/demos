/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;
var WIDTH = 400;
var HEIGHT = 400;

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
  public luminance(): number {
    return Color.luminance(this._red, this._green, this._blue);
  }
  public toString(): string {
    return "rgb(" + this._red + ", " + this._green + "," + this._blue + ")"
  }
  public asFillStyle() {
    return "rgb(" + Math.floor(this._red*255) + ", " + Math.floor(this._green*255) + "," + Math.floor(this._blue*255) + ")"
  }
  public static luminance(red: number, green: number, blue: number): number {
    var gamma = 2.2;
    return 0.2126 * Math.pow(red, gamma) + 0.7152 * Math.pow(green, gamma) + 0.0722 * Math.pow(blue, gamma);
  }
  /**
   * Converts an angle, radius, height to a color on a color wheel.
   */
  public static fromHSL(H: number, S: number, L: number): Color {
    var C = (1 - Math.abs(2*L-1)) * S;
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
    function matchLightness(R: number, G: number, B: number): Color {
      var x = Color.luminance(R, G, B);
      var m = L - (0.5 * C);
      return new Color(R + m, G + m, B + m);
    }
    var sextant = ((normalizeAngle(H) / Math.PI) * 3) % 6;
    var X = C * (1 - Math.abs(sextant % 2 - 1));
    if (sextant >= 0 && sextant < 1) {
      return matchLightness(C,X/*C*(sextant-0)*/,0.0);
    }
    else if (sextant >= 1 && sextant < 2) {
      return matchLightness(X/*C*(2-sextant)*/,C,0.0);
    }
    else if (sextant >= 2 && sextant < 3) {
      return matchLightness(0.0,C,C*(sextant-2));
    }
    else if (sextant >= 3 && sextant < 4) {
      return matchLightness(0.0,C*(4-sextant),C);
    }
    else if (sextant >= 4 && sextant < 5) {
      return matchLightness(X,0.0,C);
    }
    else if (sextant >= 5 && sextant < 6) {
      return matchLightness(C,0.0,X);
    }
    else {
      return matchLightness(0.0,0.0,0.0);
    }
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

class Complex {
  public x: number;
  public y: number;
  constructor(x: number, y:number) {
    this.x = x;
    this.y = y;
  }
  mod(): number {
    return Math.sqrt(this.x * this.x + this.y * this.y);
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
  divide(that: Complex): Complex {
    var denom = that.x * that.x + that.y * that.y;
    return new Complex((this.x * that.x + this.y * that.y)/denom, (this.y * that.x - this.x * that.y)/denom);
  }
  toString(): String {
    return this.x + "+" + this.y + "i";
  }
}

var f = function(z: Complex): Complex {
  //return z;
  // return new Complex(1,0).divide(z);
  
  var z3 = z.multiply(z).multiply(z);
  var z2 = z.multiply(z);
  var sz = new Complex(6,0).multiply(z);
  var tw = new Complex(20,0);
  return z3.add(z2).add(sz).subtract(tw);
  
};

class MinMax {
  public min: number;
  public max: number;
  constructor(min: number, max: number) {
    this.min = min;
    this.max = max;
  }
}

function sigmoid(t: number) {
  return 1 / (1 + Math.exp(-t));
}

function lightnessFromMagnitude(r: number) {
  return 2 * sigmoid(r) - 1.0
}

class ComplexPlane {
  private _canvas = new Canvas(WIDTH, HEIGHT);
  private xRange: MinMax;
  private yRange: MinMax;
  private f: (z: Complex) => Complex;
  constructor(xRange: MinMax, yRange: MinMax, f: (z: Complex)=>Complex) {
    this.xRange = xRange;
    this.yRange = yRange;
    this.f = f;
  }
  draw() {
    for (var X=0;X<WIDTH;X++) {
      for (var Y=0;Y<HEIGHT;Y++) {
        var x = (X / WIDTH) * (this.xRange.max - this.xRange.min) + this.xRange.min;
        var y = ((HEIGHT-Y)/HEIGHT) * (this.yRange.max - this.yRange.min) + this.yRange.min;
        var z = new Complex(x,y);
        var H = this.f(z).arg();
        var S = 1;
        var L = lightnessFromMagnitude(this.f(z).mod());
        //L = 0.5;
        this._canvas.context.fillStyle = Color.fromHSL(H, S, L).asFillStyle();
        this._canvas.context.fillRect(X,Y,1,1);
      }
    }
  }
}

var R = 10;
var cp = new ComplexPlane(new MinMax(-R,+R), new MinMax(-R,+R),f);
cp.draw();

