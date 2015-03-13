var log = function(s: any) {
  var w: any = window;
  var output = w.Sk.output;
  output(s+'\n');
};

log('Hello, World!');

log(blade.UNIT_KILOGRAM.toString())

var quantity = new blade.Euclidean3(1,0,0,0,0,0,0,0);

var unit = blade.UNIT_INCH;

var measure = new blade.Measure<blade.Euclidean3>(quantity, unit);

log(measure);

var sq = measure.mul(measure);

var q = sq.quantity;
var u = sq.uom;

log(sq);

log(u);


