def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

#when the make_closure(2) is invoked, it returns the power(p), and loc to the fsqr variable
# and we can invoke the fsqr as a function.
# this shows that, eventhough the make_closure(par) is dead or finished executing, the environment inside it is still retained


fsqr = make_closure(2)# now this will become a function that squres
fcub = make_closure(3)# now this will become a function that cubes

for i in range(5):
    print(i, fsqr(i), fcub(i))
    
