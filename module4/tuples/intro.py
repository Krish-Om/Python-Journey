# Tuples are the immutable sequence, where data cannot be updated in the position
# we can't modify the tuples as list, as it is a immutable. If we python will throw error.
# syntax: using paranthesis and comma seperated values
# we can only read from the tuple not write into it.
tuple_1 = (11, 2, 4, 5)
tuple_2 = 1, 2, 4, 5, 65

print(tuple_1, tuple_2)
# Note:
# you must end the value with comma for a tuple with only single element
tupele_3 = (1,)
tuple_4 = (1,)

# Empty tuple
tuple_0 = ()


# If you want to get the elements of a tuple in order to read them over,
# you can use the same conventions to which you're accustomed while using lists.
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
