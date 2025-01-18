#In python entity defined later(in the inheritance sense) overrides the 
#same entity defined earlier.

class GrandParent:
    var= 100
    def fun1(self):
        return 101
    
class Parent(GrandParent):
    var = 200
    def fun1(self):
        return 201
    
class Child(Parent):
    pass

ch = Child()
print(ch.var)
print(ch.fun1())