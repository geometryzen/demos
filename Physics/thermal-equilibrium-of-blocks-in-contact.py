from math import log, exp

Q = 10  # Total number of quanta shared between the blocks
N1 = 30 # number of oscillators in first block
N2 = 20 # number of oscillators in second block

'''
Note. To make this work for large numbers requires Strirling's approximation. We can use the approximation obtained from considering the Trapezoid rule.
'''
def factorial(n):
    return exp(n * log(n) - n + 1)

for q1 in range(Q+1):
    q2 = Q - q1
    w1 = factorial(q1 + N1 - 1) / factorial(q1) * factorial(N1-1)
    w2 = factorial(q2 + N2 - 1) / factorial(q2) * factorial(N2-1)
    print q1, q2, w1, w2, w1 * w2
