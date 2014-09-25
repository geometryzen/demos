console.log(blade.UNIT_KILOGRAM.toString())

var quantity = new blade.Euclidean3(1,0,0,0,0,0,0,0);

var unit = blade.UNIT_INCH;

var measure = new blade.Measure<blade.Euclidean3>(quantity, unit);

console.log(measure.toString());

var sq = measure.mul(measure);

var q = sq.quantity;
var u = sq.uom;

console.log(sq.toString());

console.log(u.toString());