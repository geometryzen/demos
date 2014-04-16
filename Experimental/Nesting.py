def outer(x):
    def middle():
        # a = x
        def inner():
            return x
        return inner
    return middle()()

print outer(23)
