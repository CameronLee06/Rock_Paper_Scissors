import random

# checks number of rounds is infinite / more than zero
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> / or an integer that is more than 0"
        if response != "":
            try: 
                response = int(response)

                if response <1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# checks user input is valid based on a list
def choice_checker(question, valid_list, error):

    error = "Please choose from rock / paper / scissors (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()


        # Iterates through list and if response is an item
        # in the list (or the first letter of an item), the 
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here...

yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0 
choose_instruction = "Please choose rock (r) , paper / (p) or scissors (s) or 'xxx' to end"

mode = "regular"

# Ask user for # rounds, <enter> for infinite mode
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 10

end_game = "no"
while end_game =="no":

    # Rounds Heading 
    print()
    if mode == "infinite":

        heading = "Infinite Mode: Round {}".format(rounds_played +1)

    else:
        heading = ("Round {} of {}".format(rounds_played + 1, rounds)) 


    # get user choice
    print(heading)
    user_choice = choice_checker(choose_instruction, rps_list, "Please enter R / P / S")


    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # Get the computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices
    # compare options...
    if user_choice == comp_choice:
        result = "it's a tie"

    elif user_choice == "rock" and comp_choice == "paper":
        result = "you lose"
    elif user_choice == "scissors" and comp_choice == "rock":
        result = "you lose"
    elif user_choice == "paper" and comp_choice == "scissors":
        result = "you lose"

    else:
        result = "you win"

    feedback = "{} vs {}, {}".format(user_choice, comp_choice, result)

    print(feedback)

    rounds_played += 1

    if mode == "infinite":
        rounds += 1

    if rounds_played == rounds:
        break

    # RPS Component 6 - Scoring System

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played +=1

    # Generate computer choice

    result = item

    if result == "tie":
        result = "Its a tie"
        rounds_drawn +=1
    elif result == "loss":
        rounds_lost +=1

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won : {} \t|\t Lost: {} \t|\t Draw: " "{}". format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks or playing")



                