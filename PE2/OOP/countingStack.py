class Stack:
    def __init__(self):
        self.__stklist = []

    def push(self, val):
        self.__stklist.append(val)

    def pop(self):
        val = self.__stklist[-1]
        del self.__stklist[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()

for i in range(10):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
