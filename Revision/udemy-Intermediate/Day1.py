# List - =>[]
# set -> = ()
# dict -> ={}

# This is a set, not a dictionary
person = {"name", "jogn", "doe", 25}
print(f"{type(person)}")

# this is a dictionary
person = {"name": "Krishom", "Last name": "Basukala", "age": 34}
# dictionary cannont have duplicate key name
# key as number is not allowed in dict
print(type(person))

person2 = dict(firstName="John", lastName="Doe",
               age=25, job="Teacher", _10="10")
# but we can define in this way

print(f"type of {type(person2)}")
