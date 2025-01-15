class Sample:
    __gamma = {}

    def __init__ (self):
        self.alpha = 1
        self.theta = True
        self.gamma = 12

    def setGamma(self,val):
        Sample.gamma = val


def getGamma():
    obj = Sample()
    print(obj.__gamma)

# getGamma()



obj = Sample()

#negating a private property

obj._Sample__theta = not obj._Sample__theta
print(obj.__theta)
# obj = Sample()
# obj2 =Sample()
# obj.beta = 23

# obj2.setGamma(22)

# print(obj.__dict__)
# print(obj.gamma)

# print("\n",obj2.__dict__)
# print(obj2.gamma)
# print()
