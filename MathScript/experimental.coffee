# This little trick (not to be copied!) is a temporary undocumented feature.
print = (s) -> Sk.output(s + '\n')

x = new blade.Euclidean3(0,4,0,0,0,0,0,0)
y = new blade.Euclidean3(0,0,6,0,0,0,0,0)
z = x + y

print x.toString()
print y.toString()
print "z:" + z
