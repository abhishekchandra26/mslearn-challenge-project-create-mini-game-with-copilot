# import the random module
import random   

# create a list of options that has rock, paper and scissors
options = ["rock", "paper", "scissors"]

# create a score variable and set it to 0
score = 0

# create a variable to count the number of rounds
rounds = 0

while True:
    # create a variable to store the user's choice
    user_choice = input("Choose rock, paper, or scissors: ")

    # create a variable to store the computer's choice
    computer_choice = random.choice(options)

# if the user's choice is rock
    if user_choice == "rock":
        # add the rounds variable by 1
        rounds += 1
        # if the computer's choice is rock
        if computer_choice == "rock":
            # print "Tie"
            print("Tie")
        # if the computer's choice is paper
        elif computer_choice == "paper":
            # print "You lose"
            print("You lose")
        # if the computer's choice is scissors
        else:
            # print "You win"
            print("You win")
            # add 1 to the score variable
            score += 1

# if the user's choice is paper
    elif user_choice == "paper":
        # add the rounds variable by 1
        rounds += 1
        # if the computer's choice is paper
        if computer_choice == "paper":
            # print "Tie"
            print("Tie")
        # if the computer's choice is scissors
        elif computer_choice == "scissors":
            # print "You lose"
            print("You lose")
        # if the computer's choice is rock
        else:
            # print "You win"
            print("You win")
            # add 1 to the score variable
            score += 1

# if the user's choice is scissors
    elif user_choice == "scissors":
        # add the rounds variable by 1
        rounds += 1
        # if the computer's choice is scissors
        if computer_choice == "scissors":
            # print "Tie"
            print("Tie")
        # if the computer's choice is rock
        elif computer_choice == "rock":
            # print "You lose"
            print("You lose")
        # if the computer's choice is paper
        else:
            # print "You win"
            print("You win")
            # add 1 to the score variable
            score += 1

# if the user's choice is quit
    elif user_choice == "quit":
        # print the score variable
        print("Your score is: " + str(score))
        # print the rounds variable
        print("You played " + str(rounds) + " rounds")
        # break out of the loop
        break

    # if the user's choice is not rock, paper, scissors, or quit
    else:
        # print "Invalid choice"
        print("Invalid choice")

# ask the user if they want to play again
    play_again = input("Play again? (y/n): ")

    # if the user's choice is n
    # break out of the while loop
    # print out the score and the number of rounds
    #
    # if the user's choice is y
    # continue the while loop
    # reset the score and the number of rounds to 0
    if play_again == "n":
        break
    elif play_again == "y":
        score = 0
        rounds = 0
    else:
        print("Invalid choice")