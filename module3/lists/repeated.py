my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

uniquList = []

for i in range(len(my_list)):
    if my_list[i] not in uniquList:
        uniquList.append(my_list[i])

print(uniquList)
