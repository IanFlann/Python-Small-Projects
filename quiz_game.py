print("Welcome to my Quiz!!!")

playing = input("Are you ready? ").lower()

if playing != "yes":
    print("ok bye i guess...")
    quit()
else:
    print("Okay let's play >:>")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Who sings Midas Touch? ").lower()
if answer== "aurora":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Who is Twilight Sparkle's assistant? ").lower()
if answer == "spike":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got", score, "correct, muy bien!")
print("That's " + str((score/4) * 100) + " % mi amigo!")