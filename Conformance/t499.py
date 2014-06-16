class MyTest:
    def __init__(self,s):
        self.w = s

    def plength(self):
        return len(self.w)


x = MyTest("foo")

print x.plength()
