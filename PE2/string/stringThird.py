# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print("[" + min(t) + "]")

t = [0, 1, 2]
print(min(t))


# min() checks the minimum ASCII value of the characters present in the string.
#
print(max("aAbByYzZ"))
# same for max(), the greatest ASCII value of the characters
#
#
# index()
# returns the index of the first occurence of the argument
#
#
## Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


# list()
# returns the list of each of characters
print(list("abcdef"))

# count()
# returns the count of occurenece of argument in the string
print("abbbbcdef".count("b"))
