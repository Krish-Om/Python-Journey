def add_person():
    name = input("Name:")
    age = input("age")
    email = input("Email")
    person = {"name": name, "age": age, "email": email}
    return person


people = []
print("Hi,welcome to the contact manangment system.")
print()
while True:
    command = input("You can 'Add', 'Delete' or 'Search' and 'q' ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person add")

    elif command == "delete":
        pass
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid Command")


print(people)
