'''
In natural units, c = 1, hbar = 1
'''
from units import kilogram, meter, second, joule, newton, gram, cm

c = 2.998e+8 * meter / second
print "speed of light, c=" + str(c)

hbar = 1.054e-34 * joule * second
print "Planck's constant, hbar=" + str(hbar)

eV = 1.6e-19 * joule
print "1 eV = electron volt = " + str(eV / joule) + " J"
GeV = 1e9 * eV

protonMassEnergy = 0.9383 * GeV
print "Proton mass " + str(protonMassEnergy / GeV) + " GeV"

energyUnit = hbar / second
lengthUnit = c / second

print "Proton mass rest energy " + str(protonMassEnergy) + " J"
