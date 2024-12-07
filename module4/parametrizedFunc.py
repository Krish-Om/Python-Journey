def intro(first_name, lastName="Basukala"):
    print(first_name, lastName)


intro("Alita", "wasspu")
intro("Krishom")


# def add(a,b=2,c):
#     print(a+b+c)
# add(a=2,c=3) #will give SyntaxError as teh default parameter wit values must come after the parameters withou the default values


def add(a, c, b=2):
    print(a + b + c)


add(a=2, c=3)
