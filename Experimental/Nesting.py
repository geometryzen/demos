def outer(x):
    def middle(y):
        a = x
        def inner(z):
            return x
        return inner
    return middle

print outer(10)(20)(30)
