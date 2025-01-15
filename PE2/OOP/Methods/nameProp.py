class Classy:
    pass

print(Classy.__name__)
obj = Classy()

print(type(obj).__name__)

class Snake:
    pass
class Python(Snake):
    pass

print(Python.__name__, "is a ",Snake.__name__)
print(Python.__bases__[0].__name__ ,"can be",Python.__name__)