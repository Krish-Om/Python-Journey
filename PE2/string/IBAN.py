iban = "DE89 3704 0044 0532 0130 00"

# print(iban[4:]+iban[0:4])
iban= iban.replace(" ",'')

if not iban.isalnum():
    print("You have entered invalid charactes")
elif len(iban)<15:
    print("IBAN entered is too short")
elif len(iban) >31:
    print("IBAN entered is too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2+= str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 ==1:
        print("Iban is valid")
    else:
        print("IBAN is not valid")