def foo():
    x = 5
    def bar(): 
        print(x)
        print(*(cell.cell_contents for cell in bar.__closure__))
    bar()
foo()
