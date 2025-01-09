def takeASafeInput(prompt, min, max):
    ok = True
    while ok:
        try:
            x = int(input(prompt))  
            if ok:
                ok = x >=min and x <=max
            if not ok:
                print("Error: the value is not within the permitted range(-10 to 10):")
                
        except TypeError:
            print("Wrong Input")
        return x

v = takeASafeInput("Enter a number from -10 to 10",-10,10)

print(v)