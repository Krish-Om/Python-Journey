def bad_func(n):
    raise ZeroDivisionError

try:
    bad_func(2)
except ArithmeticError:
    print("Opps something went wrong")

    