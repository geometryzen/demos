from units import kilogram, meter, second, joule, newton

cm = 0.01 * meter

# Construct the Plank units for Length, Mass and Time.
c = 2.998e+8 * meter / second
print "speed of light, c=" + str(c)

hbar = 1.054e-34 * joule * second
print "Planck's constant, hbar=" + str(hbar)

G = 6.67e-11 * newton * (meter ** 2) / (kilogram ** 2)
print "Universal gravitational constant, G=" + str(G)

print ""
lp = (hbar * G / c ** 3) ** 0.5
print "Planck length: " + str(lp)
print "Planck length: " + str(lp/cm) + " cm"
print repr(lp/cm)

mp = (hbar * c / G) ** 0.5
print "Planck mass:   " + str(mp)

tp = (hbar * G / c ** 5) ** 0.5
print "Planck time:   " + str(tp)
