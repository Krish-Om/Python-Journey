# Tuples are the unchangeable and ordered collections of data. They can be thought of as immutable lists.
# They are written in round brackets
#
#
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9

duplicates = tup.count(2)

print(duplicates)


d1 = {"Adam Smith": "A", "Judy Paxton": "B+"}
d2 = {"Mary Louis": "A", "Patrick White": "C"}
d3 = {}

for item in (d1, d2):
    d3.update(item)  # Write your code here.

print(d3)

# converting dictionary into Tuples
t = tuple(d1)
print(t)


# converting tuples into dictionary
tempT = (("green", "#008000"), ("blue", "#0000FF"))

d4 = dict(tempT)


print(d4)
