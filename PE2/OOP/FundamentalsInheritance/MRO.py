#MRO stands for Method Resolution Oroder

class A:
    def fun(self):
        print("A")
class B(A):
    def fun(self):
        super().fun()
        print("B")
class C(A):
    def fun(self):
        # super().fun()
        print("C")
class D(B,C):
    pass
    # def fun(self):
        # print("D")

# d = D()

# print(D.__mro__)

# d.fun()


class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle,Top):  # In Python, the order of inheritance should be from left to right
#with the child class inheriting from the parent classes in the specified order
    def m_bottom(self):
        print("bottom")

#class Bottom(Top,Middle) for this line of code, we will violate the Python's MRO, due to not inheriting the classes from left to right
#wiht the child class(Middle) inheriting from the parent classes(Top) in the specified order
    # pass

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    