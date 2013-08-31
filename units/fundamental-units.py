from units import *

# Construct the Plank units for Length, Mass and Time.
c = 3e+8 * meter / second ** 2

print c
print "c: " + repr(c)

h = 6.6e-34 * joule * second

print h
print "h: " + repr(h)

G = 6.7e-11 * newton * (meter ** 2) / (kilogram ** 2)

print G
print "G: " + repr(G)

print repr((h * G / c ** 3))
planckL = (h * G / c ** 3) ** 0.5

print planckL

mass = (h * c / G) ** 0.5

print mass

# TODO: Got a bit of a bug here.
# Check the newton.
print newton
# That looks OK.

# Maybe it's the power stuff...
# To be continued.

