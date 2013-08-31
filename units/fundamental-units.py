from units import *

# Construct the Plank units for Length, Mass and Time.
c = 3e+8 * meter / second
print "speed of light, c=" + str(c)

h = 6.6e-34 * joule * second
print "Planck's constant, h=" + str(h)

G = 6.7e-11 * newton * (meter ** 2) / (kilogram ** 2)
print "G=" + str(G)

print ""
lp = (h * G / c ** 3) ** 0.5
print "Planck length: " + str(lp)

mp = (h * c / G) ** 0.5
print "Planck mass:   " + str(mp)

tp = (h * G / c ** 5) ** 0.5
print "Planck time:   " + str(tp)
