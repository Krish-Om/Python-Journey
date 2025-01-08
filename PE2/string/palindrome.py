text = input("Enter a string: ")
text = text.replace(' ','')
text = text.upper()

reversedText = text[::-1] #reversing the text using slices


if text == reversedText:
    print("Palindrome")
else:
    print("Not a palindrome")