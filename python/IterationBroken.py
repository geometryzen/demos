# IterationBroken.py
class MyTest:
    def __init__(self,s):
        self.w = list(s)

    def __iter__(self):
        return self.w.__iter__()

x = MyTest("foo")

for i in x:
    print i