import json


def del_perons(people):
    for i, person in enumerate(people):
        print(i + 1, " - ", person["name"], "|", person["age"], "|", person["email"])

    while True:

        num = input("Enter a number to delete:")
        try:
            num = int(num)
            if num <= 0 or num > len(people):
                print("Invalid number, out of range")
            else:
                break
        except:
            print("Invalid number")

    people.pop(num - 1)
    print("Successfully deleted!!")


def show_conmtacts(people):
    for i, person in enumerate(people):
        print(i + 1, " - ", person["name"], "|", person["age"], "|", person["email"])


def add_person():
    name = input("Name:")
    age = input("age")
    email = input("Email")
    person = {"name": name, "age": age, "email": email}
    return person


def search(people):
    search_name = input("Search for a name:").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    show_conmtacts(results)


people = []
print("Hi,welcome to the contact manangment system.")

with open("contact.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    command = input("You can 'Add','Show', 'Delete' or 'Search' and 'q' ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person add")

    elif command == "delete":
        del_perons(people)
    elif command == "show":
        show_conmtacts(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid Command")

with open("contact.json", "w") as f:
    json.dump({"contacts": people}, f)
