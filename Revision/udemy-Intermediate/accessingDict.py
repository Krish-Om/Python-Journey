person = {
    "fname":"John",
    "lname":"doe",
    'age':23,
    'job':'Teacher'
}

print(f"Type of person is {type(person)}")
print(f"person is : {person}")


print(f"{"--"*4}Access to dictionary items{"--"*4}")
firstname = person['fname']
print(firstname)
