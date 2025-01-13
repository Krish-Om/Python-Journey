class Example:
    def __init__(self,val=1):
        self.__first =val

    def set_second (self,val):
        self.__second = val
    
    
obj1 = Example()
obj2 = Example(2)
obj2.set_second(2)
obj3 = Example()
obj3.__third = 3
# Note: no instance variable exists if there is no object in the class;
# a  class variable exists in one copy even if there are no objects in the class.

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
