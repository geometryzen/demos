from units import *

def show(name, measure):
    print "The symbol for the SI unit of %s is %s" % (name, measure.uom)
    
show("mass", kilogram)
show("length", meter)
show("time", second)
show("electric current", ampere)

print "thermodynamic temperature " +str(kelvin)
print "amount of substance " +str(mole)
print "luminous intensity " +str(candela)
print "electric charge " +str(coulomb)
print "force " +str(newton)
print "energy " +str(joule)
print "power " +str(watt)
print "electric potential " +str(volt)
print "magnetic flux density " +str(tesla)
print "electric field strength " +str(volt/meter)
print "resistance " +str(volt/ampere)
print "conductance " +str(ampere/volt)
print "permittivity " +str((coulomb ** 2)/(newton*(meter ** 2)))
print "permeability " +str(tesla * meter/ampere)
print "angular momentum " +str(joule * second)
print "frequency " +str(1 / second)
print "pressure, stress " +str(newton /(meter ** 2))
print "capacitance " +str(coulomb/volt)
print "magnetic flux " +str(volt * second)
print "inductance " +str(tesla * (meter ** 2)/ampere)
print "dynamic viscosity " +str(newton * second/meter **2)
print "moment of force " +str(newton * meter)
print "surface tension " +str(newton/meter)
print "heat flux density " +str(watt/meter ** 2)
print "heat capacity, entropy " +str(joule/kelvin)
print "thermal conductivity " +str(watt/(meter*kelvin))
print "energy density " +str(joule/(meter**3))
print "molar energy " +str(joule/mole)
print "molar entropy " +str(joule/(mole*kelvin))
