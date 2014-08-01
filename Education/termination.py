from math import *

def T(D, F, R, alpha, N):
    f = F/R
    print f
    return D - f - sqrt(D * (D - 2* alpha) + f * (f - 2 * N))

D = 8
R = 1700
alpha = 2
N = 2

print T(D, 1700, R, alpha, N)
print T(D, 2000, R, alpha, N)
print T(D, 2500, R, alpha, N)
