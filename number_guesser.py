import random 

random_number = random.randint(0,10)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time >:c")
        continue

    if user_guess == random_number:
        print("Correct!")
        break
    elif user_guess > random_number:
            print("Too high")
    else:
            print("Too low")

print("You got it in", guesses, "guesses")
        
