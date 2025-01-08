date = input("Enter your birhtday data: ")
while len(date ) >1:
    sum = 0
    for dig in date:
        sum += int(dig)
    date = str(sum)
print(date)

