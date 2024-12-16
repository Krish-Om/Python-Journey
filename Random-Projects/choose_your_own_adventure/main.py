name = input("Type your name: ")
print("Welcome,", name, "to this adventure")


answer = input(
    "You are on a dirt road. It has come to and end and you can go left or right. "
)

if answer == "left":
    answer = input(
        "You come to a river. you can walk around it or swim across. Type to walk and swim to swim across"
    )
    if answer == "swin":
        print("You swam across the river and were swept away by the river.")
    elif answer == "walk":
        print("You walked for many miles,")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross? (cross/back)"
    )

    if answer == "back":
        print("You go back")
    elif answer == "cross":
        print(
            "You tried to cross the bridge. As you walked into the bridge, the bridge "
        )
else:
    print("Not a valid option. You lose.")
