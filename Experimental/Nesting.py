def outer():
    x = 23
    def middle():
        # Why do we need this to stop x from being undefined?
        # a = x
        def inner():
            print x
        return inner
    middle()()

outer()
