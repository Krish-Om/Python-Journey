class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
# A class variable is a property which exists in just one copy and is stored outside any object.
#
# Note: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
