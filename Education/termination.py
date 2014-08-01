from math import *

def time(D,F,R, alpha):
    f = F/R
    return D - f - sqrt(D * (D - 2* alpha) + f * (f - 2 * N))

print time(8, 1700, 1700, 2)