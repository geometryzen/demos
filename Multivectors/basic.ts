var e1 = new blade.Euclidean3(0,1,0,0,0,0,0,0);
var e2 = new blade.Euclidean3(0,0,1,0,0,0,0,0);
var e3 = new blade.Euclidean3(0,0,0,1,0,0,0,0);

// First, we should be able to gracefully send text to the output window.
Sk.output(e1+"")

var sum = e1 + e2;
var diff = e1 - e2;
var lco = e1 << e2;