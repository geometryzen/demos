from units import *
from e3ga import *

print kilogram

quantity = Euclidean3(1,0,0,0,0,0,0,0);

unit = meter;

measure = quantity * unit

print measure

sq = measure * measure;

q = sq.quantity;
u = sq.uom;

print sq

print u
