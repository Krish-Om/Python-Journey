# try:
# code that may throw an error
# except Exception as e:
# code which will be executed once an error or exception is occured

# ex:

try:
    value = int(input("A value"))
    print("The ratio of ", value, "is", 1 / value)
except ValueError:
    print("Dunno what to do")
except ZeroDivisionError:
    print("Division by zero is Infinite")
except ValueError:
    print("Something strange occured")
except TypeError:
    print(
        "caused when you try to apply a data whose type cannot be accepted in the current context"
    )
except AttributeError:
    print(
        "Caused by trying to activate a method which doesn't exist in an item you're dealing with."
    )
