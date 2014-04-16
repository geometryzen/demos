def outer(x):
    def middle(y):
        a = x
        def inner(z):
            print "z", str(z)
            print "y", str(y)
            return x
        return inner
    return middle

print outer(10)(20)(30)
