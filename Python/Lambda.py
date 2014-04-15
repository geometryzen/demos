def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

for i in range(10):
    print factorial(i)