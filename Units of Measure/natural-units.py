'''
In natural units, c = 1, hbar = 1
'''
from units import kilogram, meter, second, joule, newton, gram, cm

milligram = 0.001 * gram
mosquitoMassSI = 10 * milligram

# Construct the Plank units for Length, Mass and Time.
c = 2.998e+8 * meter / second
print "speed of light, c=" + str(c)

hbar = 1.054e-34 * joule * second
print "Planck's constant, hbar=" + str(hbar)

energyUnit = hbar / second
lengthUnit = 1 / c

print "mosquito rest energy (SI)  " + str(mosquitoMassSI * c * c)
print "mosquito rest energy (GeV) " + str(mosquitoMassSI * c * c / energyUnit)
