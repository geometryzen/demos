from units import *

print "mass (" +str(kilogram.uom) + ")"
print "length (" +str(meter.uom) + ")"
print "time (" +str(second.uom) + ")"
print "electric current (" +str(ampere.uom) + ")"
print "thermodynamic temperature (" +str(kelvin.uom) + ")"
print "amount of substance (" +str(mole.uom) + ")"
print "luminous intensity (" +str(candela.uom) + ")"
print "electric charge (" +str(coulomb.uom) + ")"
print "force (" +str(newton.uom) + ")"
print "energy (" +str(joule.uom) + ")"
print "power (" +str(watt.uom) + ")"
print "electric potential (" +str(volt.uom) + ")"
print "magnetic flux density (" +str(tesla.uom) + ")"
print "electric field strength (" +str((volt/meter).uom) + ")"
print "resistance (" +str((volt/ampere).uom) + ")"
print "conductance (" +str((ampere/volt).uom) + ")"
print "permittivity (" +str(((coulomb ** 2)/(newton*(meter ** 2))).uom) + ")"
print "permeability (" +str((tesla * meter/ampere).uom) + ")"
print "breakdown (N/C) (" +str((newton/coulomb).uom) + ")"
print "angular momentum (" +str((joule * second).uom) + ")"
print "frequency (" +str((1 / second).uom) + ")"
print "pressure, stress (" +str((newton /(meter ** 2)).uom) + ")"
print "capacitance (" +str((coulomb/volt).uom) + ")"
print "magnetic flux (" +str((volt * second).uom) + ")"
print "inductance (" +str((tesla * (meter ** 2)/ampere).uom) + ")"
print "dynamic viscosity (" +str((newton * second/meter **2).uom) + ")"
print "moment of force (" +str((newton * meter).uom) + ")"
print "surface tension (" +str((newton/meter).uom) + ")"
print "heat flux density (" +str((watt/meter ** 2).uom) + ")"
print "heat capacity, entropy (" +str((joule/kelvin).uom) + ")"
print "thermal conductivity (" +str((watt/(meter*kelvin)).uom) + ")"
print "energy density (" +str((joule/(meter**3)).uom) + ")"
