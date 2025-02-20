import time

def cache(fn):
    cache_value={}
    print(cache_value)
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result = fn(*args,**kwargs)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_run(a,b):
    time.sleep(b)
    return b+a
    
print(long_run(2,3))
print(long_run(3,5))
