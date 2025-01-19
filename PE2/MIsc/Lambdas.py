# general syntax
#lambda parameters : expression

#some examples

#recommended way of styling lambdas
def init():
    def two(): return 2
    def sqr(x): return x*x
    def pwr(x,y): return x ** y

    print(two())
    print(sqr(3))
    print(pwr(3,two()))

init()

#not recommended way of styling lamdas
two = lambda: 2
sqr = lambda x: x*x
pwr = lambda x,y: x ** y

for a in range(-2,3):
    print(sqr(a),end=" ")
    print(pwr(a, two()))