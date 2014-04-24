from units import *

print "kg = kilogram (" +str(kilogram) + ")"

print "m = meter (" +str(meter) + ")"

print "s = second (" +str(second) + ")"

print "C = coulomb (" +str(coulomb) + ")"

print "N = newton (" +str(kilogram * meter / (second ** 2)) + ")"

print "J = joule (" +str(newton * meter) + ")"

print "W = watt (" +str(joule/second) + ")"

print "A = ampere (" +str(coulomb/second) + ")"

print "V = volt (" +str(joule/coulomb) + ")"

print "T = tesla (" +str((newton/coulomb)/(meter/second)) + ")"

print "V/m = volt/meter (" +str(volt/meter) + ")"

print "ohm = volt/ampere (" +str(volt/ampere) + ")"

print "permeability (" +str(tesla * meter/ampere) + ")"
