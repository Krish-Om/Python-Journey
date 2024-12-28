my_list = [12, 33, 45, 1, 23]

largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
