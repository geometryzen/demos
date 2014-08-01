from math import *

def T(D, F, R, alpha, N):
    f = F/R
    arg = D * (D - 2.0* alpha) + f * (f - 2.0 * N)
    return D - f - sqrt(arg)
    
def fee(R,T, D, alpha, N):
    return R * ((T * T / 2.0) - T * D + alpha * D) / (D - (N + T))

D = 8
R = 1700.0
alpha = 2
N = 2

print "Fee versus Time"
for F in range(0, 4500, 500):
    print F, T(D, F, R, alpha, N)

print "Time versus Fee"
for T in range(0, 60, 5):
    print T/10.0, fee(R, T/10.0, D, alpha, N)
