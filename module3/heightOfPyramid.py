blocks = int(input("Enter the number of blocks:"))
height =0
for i in range(blocks):
    for j in range(blocks-i-1):
        height = j
print(height)        