// We should support shortcut construction in the BLADE library.
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);

var random = Math.random;
var meter = blade.units.meter;

var a = (random() * e1 + random() * e2 + random() * e3) * meter
var b = (random() * e1 + random() * e2 + random() * e3) * meter
var c = (random() * e1 + random() * e2 + random() * e3) * meter

print a * b
print a | b + a ^ b
print a << b + a ^ b
print a >> b + a ^ b
print
print a * b | c
print a * (b | c)
