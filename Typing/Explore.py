# Typing/Explore.py
@typechecked
def greet(name, age):
#def greet(name: str, age: int) -> str:
    print('Hello {0}, you are {1} years old'.format(name, age))
    
greet(1,28)
