# This little trick (not to be copied!) is a temporary undocumented feature.
log = (s) =>
  Sk.output(s+'\n');

x = new blade.Euclidean3(0,4,0,0,0,0,0,0)
y = new blade.Euclidean3(0,0,6,0,0,0,0,0)
z = x + y

log x.toString()
log y.toString()
log z.toString()
