import math
x = float(input("Enter a number: "))

assert x >= 0.0 #raises an AssertionError if the value of x is less than 0.0.k
x = math.sqrt(x)
print(x)