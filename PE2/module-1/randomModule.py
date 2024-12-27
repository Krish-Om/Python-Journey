from random import random, seed

for i in range(5):
    print(random())


seed(0)
print("\n")
for i in range(5):
    print(random())
