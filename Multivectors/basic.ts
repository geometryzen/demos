var e1 = new blade.Euclidean3(0,1,0,0,0,0,0,0);
var e2 = new blade.Euclidean3(0,0,1,0,0,0,0,0);
var e3 = new blade.Euclidean3(0,0,0,1,0,0,0,0);

// First, we should be able to gracefully send text to the output window.
var w: any = window;
w.Sk.output(e1+"\n")

var M = 1 + e1 + e2 + e3 + e1 * e2 + e2 * e3 + e3 * e1 + e1 * e2 * e3
w.Sk.output(M+"\n");
w.Sk.output(~M+"\n");
