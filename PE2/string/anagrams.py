
# This is what we're going to do with both strings:
# - remove spaces
# - change all letters to upper case
# - convert into list
# - sort the list
# - join list's elements into string
# and finally, compare both strings.
# Let's do it!
str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")




str_1 = str_1.replace(' ','')
str_2 = str_2.replace(' ','')

str_1 = str_1.upper()
str_2 = str_2.upper()

str_1 = list(str_1)
str_2 = list(str_2)

str_1= sorted(str_1)
str_2 = sorted(str_2)

str_1 = "".join(str_1)
str_2 = "".join(str_2)

if str_1 == str_2:
    print("They are anagrams")
else:
    print("They are not")