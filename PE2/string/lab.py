
def splitCustom(str):
    list=[]
    word=''
    if str == " " or str.isspace():
        return [ ]
    
    inword = not str[0].isspace()
    
    for ch in str:
        if inword:
            if not ch.isspace():
                word = word + ch
            else:
                list.append(word)
                
                inword = False
        else:
            if not ch.isspace():
                inword = True
                word = ch
            else:
                pass
    if inword:
        list.append(word)
    return list

print(splitCustom("Hello world"))