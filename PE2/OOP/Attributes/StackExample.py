class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]

        return val


StackB = Stack()
smallStack = Stack()
BigStack = Stack()

print(StackB.push(4))
print(smallStack.push(StackB.pop() + 4))
print(BigStack.push(56))
print(BigStack.push(smallStack.pop() * 3))
