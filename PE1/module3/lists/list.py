# list starts with an open square bracket and ends with a closed square bracket

numbers = [1, 23, 32, 5, 33]
print("Numbers:", numbers)
numbers[2] = 3  # this is called indexing in python
print("Numbers:", numbers)

print(len(numbers))

# deleting a element from list
del numbers[1]

print("Numbers:", numbers)

print(len(numbers))

# Negative indices are legal, it will traverse from reverse
print(numbers[-3])  # -> prints the 3


# some methods associated with lists
numbers.append(55)  # puts 55 in last index

numbers.insert(2, 36)  # puts 36 in the index "2" i.e 3rd location in list
