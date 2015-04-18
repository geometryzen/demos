debugger;

var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

// We should support shortcut construction in the blade library.
var e1 = blade.vectorE3(1,0,0);
var e2 = blade.vectorE3(0,1,0);
var e3 = blade.vectorE3(0,0,1);

var a = (2 * e1 + 3 * e2 + 5 * e3);
var b = (7 * e1 + 11 * e2 + 13 * e3);
var c = (17 * e1 + 19 * e2 + 23 * e3);

log(a);
log(b);
log(a * b);
log(a | b);
log(a ^ b);
log(a | b + a ^ b);
log(a << b + a ^ b);
log(a >> b + a ^ b);
log("");
log(a * b | c);
log(a * (b | c));
log((a * b) | c);
