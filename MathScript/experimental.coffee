print = (s) -> Sk.output(s + '\n')

x = new blade.Euclidean3(0,4.7,0,0,0,0,0,0)
y = new blade.Euclidean3(0,0,6.3,0,0,0,0,0)

z = x << y
m = blade.UNIT_METER
s = blade.UNIT_SECOND

v = z * m

print Ms.VERSION 
print "x: " + x
print "y: " + y
print "z: #{z}"
print "velocity: " + v
