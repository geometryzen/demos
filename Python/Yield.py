class GeneratorClass:
    def __init__(self):
        pass
    def generator(self):
        for i in range(10):
            yield i

gen = GeneratorClass()

for g in gen.generator(3):
    print g