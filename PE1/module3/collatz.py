c0 = int(input("Enter a non-negative and non-zero number:"))
i = 0
while True:
    
    if c0 % 2 == 0:
        c0 = c0//2
    else:
        c0 = c0*3 + 1

    print(c0) 
    i+= 1 
    if c0 ==1:
        break
    else:
        continue

print("Steps: ",i)
print("Proved: hypothesis!")