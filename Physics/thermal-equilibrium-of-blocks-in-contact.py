from math import factorial

Q = 10  # Total number of quanta shared between the blocks
N1 = 5 # number of oscillators in first block
N2 = 7 # number of oscillators in second block

for q1 in range(Q):
    q2 = Q - q1
    w1 = factorial(q1 + N1 - 1) / factorial(q1) * factorial(N1-1)
    w2 = factorial(q2 + N2 - 1) / factorial(q2) * factorial(N2-1)
    print q1, q2, w1, w2, w1 * w2
