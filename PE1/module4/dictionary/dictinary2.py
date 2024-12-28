dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ["cat", "lion", "horse"]


for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


# keys() --> returns an iterable object consisiting of all keys gatthered in dictionary
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# items() returns a tuples where each tuple is a key-value pair
print(dictionary.items())
for english, french in dictionary.items():
    print(english, "->", french)


dictionary["cat"] = "minou"

print(dictionary)


for french in sorted(dictionary.keys()):
    print(french)


for french in dictionary.values():  # returns values just like keys() returns keys
    print(french)
