class Class:
    def __init__(self,val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

obj = Class(1)
print("a",obj.a)

if hasattr(obj,'b') :
    print("b:", obj.b)

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()
print(hasattr(example_object,'b')) 
print(hasattr(example_object,'a'))
print(hasattr(ExampleClass,'a'))
print(hasattr(ExampleClass,'b'))
