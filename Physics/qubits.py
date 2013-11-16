from e3ga import *
from math import exp

theta = 0
phi = 0

R = exp(-I * e3 * phi / 2) * exp(-I * e2 * theta / 2)

print R