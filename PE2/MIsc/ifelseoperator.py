list1 = []

for x in range(10):
    list1.append(1 if x%2==0 else 0)

print(list1)

#above task also can be done through this way 
#where compactness and elegance matter


list2 = [1 if x%2 ==0 else 0 for x in range(10)]

print(list2)