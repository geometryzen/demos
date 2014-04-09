# Limits.py : determines approximate machine precision
N = 3
eps = 1.0
for i in range(N) :
    eps = eps / 2
    onePluseps = 1.0 + eps
    print "one + eps = ", onePluseps
    print "eps = ", eps