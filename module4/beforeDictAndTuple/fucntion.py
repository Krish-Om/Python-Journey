def factorial(num):
    if num > 1:
        return factorial(num - 1) * num
    else:
        return 1


print(factorial(2))
