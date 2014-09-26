from units import *

# units.py
print kilogram

quantity = Euclidean3(1,0,0,0,0,0,0,0);

unit = UNIT_INCH;

measure = Measure(quantity, unit);

console.log(measure.toString());

sq = measure * measure;

q = sq.quantity;
u = sq.uom;

console.log(sq.toString());

console.log(u.toString());
