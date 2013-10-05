'''
In natural units, c = 1, hbar = 1
'''
from units import kilogram, meter, second, joule, newton, gram, cm

c = 2.998e+8 * meter / second
print "speed of light, c=" + str(c)

hbar = 1.054e-34 * joule * second
print "Planck's constant, hbar=" + str(hbar)

eV = 1.6e-19 * joule
milligram = 0.001 * gram
protonMass = 938.3 * 1e6 * eV
print "Proton mass " + str(protonMass)

energyUnit = hbar / second
lengthUnit = c / second

print "proton rest energy " + str(protonMass * c * c / joule) + " J"
