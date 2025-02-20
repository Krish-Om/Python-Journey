def debug(func): # this becomes a decorater
    def wrapper(*args,**kwargs):
        print(f"{func.__name__}")     
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}:{v}" for k,v in kwargs.items())
        print(f"Calling:{func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper


#the greet() will have to go through the debug decorater
@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")
@debug
def hello():
    print('Hello world')
greet("chai")
hello()
