def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

print factorial(1)