var one = new blade.Euclidean2(1,0,0,0);
var e1 = new blade.Euclidean2(0,1,0,0);
var e2 = new blade.Euclidean2(0,0,1,0);
var I = e1 * e2

var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

function show(label: string, x) {
  log(label + ": " + x);
}

show('one | 1',   one | 1);
show('e1 | e1',   e1 | e1);
show('e2 | e2',   e2 | e2);
show('I | I',   I | I);
