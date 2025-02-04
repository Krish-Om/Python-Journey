def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    
    return inner

p_tag = tag('<p>')
print(p_tag("Lorem Ipsum"))