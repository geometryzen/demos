print = (s) -> Sk.output(s + '\n')

x = new blade.Euclidean3(0,4.7,0,0,0,0,0,0)
y = new blade.Euclidean3(0,0,6.3,0,0,0,0,0)
z = x + y

print "x: " + x
print "y: " + y
print "z: " + z
