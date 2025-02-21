def order_pizza(size,*toppings,**detail):
    print(f"Order a {size} pizza with following toppings:")
    print(f"- {toppings}") # the values in args are stored as tuple
    print(f"{detail}")
order_pizza("large","pepporoni","caramel","mushroom",detail=True,Tip=4)


#In conclusion, *args -> stores the extra values that gets pass into the 
# the function as tuple
# wherease, **kwargs stores the arguments that passed into the function
# which are in the form of key, value pair. which stored in the form of dictionary



