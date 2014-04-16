def outer(x):
    def middle():
        # Why do we need this to stop x from being undefined?
        #a = x
        def inner():
            return x
        return inner
    return middle()()

print outer(23)
