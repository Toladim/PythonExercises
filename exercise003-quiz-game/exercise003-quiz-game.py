print ("Welcome to Python-Quest!")

playing = input("Do you want to start a game? (y/n): ").lower()

if playing != "y":
    quit()
else:
    print("Ok. Let's Play!")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power suply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100 ) + "%.")