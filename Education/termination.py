from math import *

def time(D,F,R, alpha):
    return D - (F/R) - sqrt(D * (D- 2* alpha))

print time(8, 1700, 1700, 2)