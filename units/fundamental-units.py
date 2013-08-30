from units import *

c = 3e+8 * meter / second ** 2

print c

h = 6.6e-34 * joule * second

print h

G = 6.7e-11 * newton * (meter ** 2) / (kilogram ** 2)

print G

length = (h * G / c ** 3) ** 0.5

print length

mass = (h * c / G) ** 0.5

print mass

# TODO: Got a bit of a bug here.
# Check the newton.
print newton
# That looks OK.

# Maybe it's the power stuff...
# To be continued.

