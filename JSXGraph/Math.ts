var Math = JXG.Math;

function print(x) {
  var w: any = window;
  w.Sk.output(x + "\n");
}

print("JXG.Math.eps = " + JXG.Math.eps);
print("JXG.Math.binomial(4,2) = " + JXG.Math.binomial(4,2));