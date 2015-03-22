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