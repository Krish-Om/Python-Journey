class Stack:

    def __init__(self):  # Python Constructor
        self.__stack_list = []
        print("Hi!")

    def push(self, val):
        self.__stack_list.append(val)
        for v in self.__stack_list:
            print(v)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()  # instantiating the object
# print(len(stack_object.stack_list))

# When any class component has a name starting with two underscores (__),
# it becomes private – this means that it can be accessed only from within the class.
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)


print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
