beatles = []

beatles.append("John Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


for i in range(2):
    newName = input("Enter name: ")
    beatles.append(newName)
    i += 1


del beatles[3]
del beatles[3]

beatles.insert(0, "Ringo Starr")
