import os

os.makedirs("myFirstDir/mySecondDir")
os.chdir("myFirstDir")
print(os.listdir())
