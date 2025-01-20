#In newer version of python, we can create iterators
# without implementing the __iter__ and __next__ methods
# Python will implicitly implement them for us, when we build generators


def gen(n):
    for i in range(n):
        yield i

for i in gen(3):
    print(i)