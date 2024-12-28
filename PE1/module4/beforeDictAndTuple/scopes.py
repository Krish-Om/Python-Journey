def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


def my_function2():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function2()
print(var)
# A variable existing outside
# a function has scope inside the function's body, excluding those which define a variable of the same name
# It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). Assigning a value forces the creation of the function's own variable.
