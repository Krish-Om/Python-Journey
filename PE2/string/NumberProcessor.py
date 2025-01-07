line = input("Enter a line of numbers - seperate them with spaces:")
strings = line.split()
total = 0

print(strings)
try:
    for substr in strings:
        print(substr)
        total += float(substr)
    print("The total is: ", total)
except:
    print(substr, "is not number")
