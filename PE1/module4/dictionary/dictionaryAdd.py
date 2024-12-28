# Adding a new key-value pair to a dictionary is as simple as changing a value – you only have to assign a value to a new, previously non-existent key.

# Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}


dictionary["swan"] = "cygne"  # simply adds the key {"swan" : "cygne"} in dictionary
# the data should be non-existing, which shows that dictionary are different than list
# using update() to insert an item to dictionary
print(dictionary)

dictionary.update({"human": "homospaiens"})

# Removing a key from dictionary
# removing a key from dictionary wil remove the associated value too.
# As value cannot exist without it's key
# we remove it using the del keyword

del dictionary["cat"]
print(dictionary)


# removing the last item using popitem()

dictionary.popitem()

print(dictionary)
