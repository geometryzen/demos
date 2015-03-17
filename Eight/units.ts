// This little trick (not to be copied!) is a temporary undocumented feature.
var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

log('Hello, World!!');

log(blade.UNIT_KILOGRAM.toString())
log(blade.UNIT_METER.toString())
log(blade.UNIT_SECOND.toString())
log(blade.UNIT_COULOMB.toString())
log(blade.UNIT_KELVIN.toString())

var quantity = new blade.Euclidean3(1,0,0,0,0,0,0,0);

var unit = blade.UNIT_INCH;

var measure = new blade.Measure<blade.Euclidean3>(quantity, unit);

log(measure);

var sq = measure.mul(measure);

var q = sq.quantity;
var u = sq.uom;

log(sq);

log(u);
