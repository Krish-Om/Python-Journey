print("Welcome to the Quiz Game")
score = 0


playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for ? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


print("You got " + str(score) + " questions correct !")
score = (score / 3) * 100
print("You got " + str(score) + " % ")
