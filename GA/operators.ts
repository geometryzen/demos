var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

// We should support shortcut construction in the BLADE library.
var e1 = eight.vectorE3(1,0,0);
var e2 = eight.vectorE3(0,1,0);
var e3 = eight.vectorE3(0,0,1);

var random = Math.random;
var meter = blade.units.meter;

var a = (random() * e1 + random() * e2 + random() * e3);
var b = (random() * e1 + random() * e2 + random() * e3);
var c = (random() * e1 + random() * e2 + random() * e3);

log(a * b);
log(a | b + a ^ b);
log(a << b + a ^ b);
log(a >> b + a ^ b);
log("");
log(a * b | c);
log(a * (b | c));
