class Complex {
  public x: number;
  public y: number;
  constructor(x: number, y:number) {
    this.x = x;
    this.y = y;
  }
  arg(): number {
    return Math.atan2(this.x, this.y);
  }
  multiply(that: Complex): Complex {
    return new Complex(this.x * that.x - this.y * that.y, this.x * that.y + this.y * that.x);
  }
  toString(): String {
    return this.x + "+" + this.y + "i";
  }
}

var zero = new Complex(0,0);

console.log("" + zero);