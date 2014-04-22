import numpy as np
from math import exp, sin

time = np.linspace(0.0, 1.0, 9)

print time
print exp(-time/3)*sin(3*time)