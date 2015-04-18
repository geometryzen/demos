var e1 = new blade.Euclidean2(0,1,0,0);
var e2 = new blade.Euclidean2(0,0,1,0);

var log = function(s: any) {
  var w: any = window;
  w.Sk.output(s+'\n');
};

function show(label: string, x) {
  log(label + ": " + x);
}

show('e1', e1);