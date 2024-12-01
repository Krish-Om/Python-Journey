print("Break instruction:")

for i in range(1,6):
    if i==1:
        break
    print("inside the loop",i)
print("outside the loop")


print("Continue instruction")

for i in range(1,6):
    if i == 3:
        continue
    print("inside the loop",i)
print("Outside the loop")


