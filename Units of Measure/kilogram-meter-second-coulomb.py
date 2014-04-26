from units import *

print "kg = kilogram (" +str(kilogram) + ")"

print "length (" +str(meter.uom) + ")"

print "time (" +str(second.uom) + ")"

print "electric current (" +str(ampere.uom) + ")"

print "thermodynamic temperatue (" +str(kelvin.uom) + ")"

print "C = coulomb (" +str(coulomb) + ")"

print "N = newton (" +str(kilogram * meter / (second ** 2)) + ")"

print "J = joule (" +str(newton * meter) + ")"

print "W = watt (" +str(joule/second) + ")"

print "V = volt (" +str(joule/coulomb) + ")"

print "magnetic flux density (" +str((newton/coulomb)/(meter/second)) + ")"

print "V/m = volt/meter (" +str(volt/meter) + ")"

print "resistance (" +str(volt/ampere) + ")"

print "conductance (" +str(ampere/volt) + ")"

print "permeability (" +str(tesla * meter/ampere) + ")"

print "permittivity (" +str((coulomb ** 2)/(newton*(meter ** 2))) + ")"

print "breakdown (N/C) (" +str(newton/coulomb) + ")"

print "Js = joule * second (" +str(joule * second) + ")"

print "frequency (" +str(1 / second) + ")"

print "pressure, stress (" +str(newton /(meter ** 2)) + ")"

print "capacitance (" +str(coulomb/volt) + ")"

print "magnetic flux (" +str(volt * second) + ")"

print "inductance (" +str(tesla * (meter ** 2)/ampere) + ")"
