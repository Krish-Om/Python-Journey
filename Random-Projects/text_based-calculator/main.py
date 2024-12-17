try:
    num1 = float(input("Enter a number 1:"))
    sign = input("Sign: ")
    num2 = float(input("Enter a number 2: "))

    if sign == "+":
        print(num1, sign, num2, " = ", num1 + num2)
    elif sign == "-":
        print(num1, sign, num2, " = ", num1 - num2)
    elif sign == "/":
        if num2 == 0:
            print("Division by zero")
        else:
            print(num1, sign, num2, " = ", num1 / num2)
    elif sign == "*":
        print(num1, sign, num2, " = ", num1 * num2)
except:
    print("Invalid Operands.")

