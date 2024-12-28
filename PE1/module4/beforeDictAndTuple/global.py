def myFoo():
    global var
    var = 2
    print("Do I know that variable?", var)


myFoo()
print(var)
