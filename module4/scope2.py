def myFoo(n):
    print("I got ", n)
    n += 1
    print("I have", n)


var = 1
myFoo(var)
print(var)

# changing the parameter's value doesn't propagate outside the function(in any case, not when the variable is a scaler)
