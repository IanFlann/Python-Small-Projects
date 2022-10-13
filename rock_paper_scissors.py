import random

user_wins = 0
computer_wins = 0
draws = 0
options = ["R", "P", "S"]

print("Rock Paper Scissors Game !!")

while True:
    user_input = input("Type R for Rock, P for Paper or S for Scissors (or Q to quit): ").Upper()

    if user_input == "Q":
        break   
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer Picked:", computer_pick)

    if user_input == "R" and computer_pick == "S":
        print("You win!")
        user_wins+= 1

    elif user_input == "S" and computer_pick == "P":
        print("You win!")
        user_wins+= 1
        
    elif user_input == "P" and computer_pick == "R":
        print("You win!")
        user_wins+= 1
    
    elif user_input == computer_pick:
        print("Draw!")
        draws+= 1
        
    else:
        print("You Lose!")
        computer_wins+= 1

print("------------------------>")
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("You drew", draws, "times.")
print("Bye Bye!")
print("------------------------>")