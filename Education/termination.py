from math import *

def time(D,F,R, alpha, N):
    f = F/R
    return D - f - sqrt(D * (D - 2* alpha) + f * (f - 2 * N))

D = 8
R = 1700
alpha = 2
N = 2

print time(D, 1700, R, alpha, N)
print time(D, 2500, R, alpha, N)