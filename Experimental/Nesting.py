def outer():
    x = 23
    def middle():
        def inner():
            print x
        return inner
    middle()()

outer()
