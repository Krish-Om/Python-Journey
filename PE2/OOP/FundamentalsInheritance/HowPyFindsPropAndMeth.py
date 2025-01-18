class Super:
    supVar = 2
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return "My name is "+self.__name + "."
    
class Sub(Super):
    subVar = 1
    def __init__(self, name):
        super().__init__(name) #super() is a python built-in method that calls the parent class constructor

obj = Sub("Andy")

print(obj)
print(obj.supVar)

class A:
    def __init__(self):
        self.supVar = 133

class B(A):
    def __init__(self):
        super().__init__() #this will let the B class to access the superClass prop and methods from class A
        self.subvar = 12
b = B()
print(b.supVar)