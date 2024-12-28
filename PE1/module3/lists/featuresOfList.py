# The assignment: list_2 = list_1 copies the name of the array, not its contents.
# In effect, the two names (list_1 and list_2) identify the same location in the computer memory.
# Modifying one of them affects the other, and vice versa.


# the name of an ordinary variable is the name of its contents
# the name of a list is the name of a memory location where the list is stored


# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Slicing syntax
# newList = my_list[start:end]
# Copying some part of the list. i.e copies element from start to end-1
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

newList = my_list[1:-1]
print(newList)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

del new_list[:]  # deletes the data stored inside it only.
print(new_list)
del new_list  # deletes the variable and data
# print(new_list) will give an error of new_list no longer being defined
