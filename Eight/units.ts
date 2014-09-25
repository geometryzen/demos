console.log(blade.UNIT_KILOGRAM.toString())

var quantity = new blade.Euclidean3(0,1,0,0,0,0,0,0);

var unit = blade.UNIT_INCH;

var measure = new blade.Measure(quantity, unit);

console.log(measure.toString());