list1= []

for ex in range(6):
    list1.append(10 ** ex)

list2 = [10 ** ex for ex in range(5)]
print(list1)
print(list2)

#a easy ways to create a generator
x = (i for i in range(3)) # this becomes a generator comprehension
for n in x:
    print(n)