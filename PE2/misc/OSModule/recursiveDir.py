import os

os.remov("mySecondDir")
os.makedirs("myFirstDir/mySecondDir")
os.chdir("myFirstDir")
print(os.listdir())


#knowing the current working directory
print(os.getcwd())

print(os.listdir())
