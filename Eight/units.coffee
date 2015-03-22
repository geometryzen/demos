print = (s) -> Sk.output(s + '\n')

print blade.VERSION

kg = blade.units.kilogram
m = blade.units.meter
s = blade.units.second

print ''
print kg
print kg.dimensions

print ''
print m
print m.dimensions

print ''
print s
print s.dimensions

print m * s
print 5 * m
print m * 5
print 5 / s
print s / 5
print 5 + s
print s + 5

e1 = new blade.Euclidean3(0,1,0,0,0,0,0,0)

print 5 * e1 * m
print 5 * m * e1
print e1 * 5 * m
print e1 * m * 5
