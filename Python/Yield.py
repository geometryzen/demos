import sys
class GeneratorClass:
    def __init__(self):
        print type(self)
        pass
    def generator(self):
        for i in range(10):
            yield i

gen = GeneratorClass()

sys.debug()
for g in gen.generator(23):
    print g