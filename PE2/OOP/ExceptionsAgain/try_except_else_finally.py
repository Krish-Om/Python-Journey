def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError as e:
        print(e)
        # print(e.__str__())
        return None
    else:
        print("Everythin went fine")
        return n
    finally:
        print("Say goodbye")

    
print(reciprocal(23))
print(reciprocal(0))