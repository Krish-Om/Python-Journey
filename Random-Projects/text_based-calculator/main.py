def get_number(number):
    while True:
        
        num = input("num "+ str(number)+ ":")
        try:
            return float(num)
            break
        except:
            print("Invalid number,try again")
    
num1 = get_number(1)
num2 = get_number(2)

sign = input("Sign: ")
valid = False
try:
    num1 = float(num1)
    num2 = float(num2)
    valid = True
except:
    print("Invalid Operands.")

if valid:    
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