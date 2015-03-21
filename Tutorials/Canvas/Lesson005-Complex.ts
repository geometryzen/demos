// This little trick (not to be copied!) is a temporary undocumented feature.
var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log('Hello, World!!');

var z = blade.Complex(2, 3);

log(z);

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
  multiply(that: Complex): Complex {
    return new Complex(this.x * that.x - this.y * that.y, this.x * that.y + this.y * that.x);
  }
  toString(): String {
    return this.x + "+" + this.y + "i";
  }
}

var zero = new Complex(0,0);
var one = new Complex(1,0);
var i = new Complex(0,1);
var minusOne = new Complex(-1,0);
var minusI = new Complex(0,-1);

log("zero: " + zero);
log("one: " + one);
log("i: " + i);

log("arg(1) " + one.arg());
log("arg(i) " + i.arg());
log("arg(-1) " + minusOne.arg());
log("arg(-i) " + new Complex(0,-1).arg());
