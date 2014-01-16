a = 1.0
b = 0.5

c = a + b

while c != a:
    b = b / 2.0
    c = a + b
    print c

print a,b,c