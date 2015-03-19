var x = new blade.Euclidean3(0,4,0,0,0,0,0,0);
var y = new blade.Euclidean3(0,0,6,0,0,0,0,0);
var z = x.__add__(y);
console.log(x.toString());
console.log(""+y);
console.log(""+z);
