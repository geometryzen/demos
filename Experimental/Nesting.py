def outer():
    x = 23
    def middle():
        a = x
        def inner():
            print x
        return inner
    middle()()

outer()
