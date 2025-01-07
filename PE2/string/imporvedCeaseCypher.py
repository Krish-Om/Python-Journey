

def encrypt(text,shiftValue):
    cipher = ""

    for char in text:
        if not char.isalpha():
            cipher+=char
        else:
            if char.islower():
                code = ord(char) + shiftValue
                if code > ord('z'):
                    code = ord('a')
                cipher += chr(code)
            elif char.isupper():
                code = ord(char) + shiftValue
                if code > ord('Z'):
                    code = ord('A')
                cipher += chr(code)

    return cipher


def start():
    text = input("Enter the message you want to encrypt: ")
    shiftValue = int(input("Enter a shift value in range of [1-25]: "))
    while (True):
        if (shiftValue >0) and (shiftValue <= 25):
            print("Shift value: ", shiftValue)
            break
        shiftValue = int(input("Enter a shift value in range of [1-25]: "))

    encrypted = encrypt(text,shiftValue)

    print("Text: ",text, "Shift Value: ", shiftValue, sep=" ")

    print("Ceaser cipher: " , encrypted)


start()