# The dictionary is another Python data structure. It's not a sequence type and it is mutable.

# Its a look-a-like of JSON
# It stores data in a key-pair value.
# It stores a key and a value corresponding to the key for easy accessing of the data

# Example:
dictionary = {"cat": "Hello", "dog": "china"}

phone_num = {"boss": 12345345345, "Suzy": 23092398743}

empty_dictionary = {}
print(phone_num)
print(dictionary)


# each key must be any immutable type of object: it can be a number or evena a string, but not a list

# dictionary is a list - a list contains a set of number values, while a dictionary holds pairs of values;
#
# we can look for value using key, but not key using value
#
#
print(dictionary["cat"])
