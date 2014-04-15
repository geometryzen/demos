def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

for i in range(10):
    print i,factorial(i)
    
print map(lambda x: x*x*x, range(1, 11))

integers = range(8)
squares  = map(lambda x: x*x, integers)
print map(None, sequence, squares)
