import random


show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before?" ).lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    if show_instructions == "yes": 
        print("program continues")

    elif show_instructions == "y":
        print("program continues")

    elif show_instructions == "n":
        print("display instructions")

    elif show_instructions == "no":
        print("display instructions") 

    else:
        print("Please answer yes / no")


       
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

game_summary = []

rounds_played = 0 

# Rounds lost will be calculated (total - draw - win)
rounds_won = 0
rounds_drawn = 0

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
        rounds_drawn +=1

    elif user_choice == "rock" and comp_choice == "paper":
        result = "you lose"
    elif user_choice == "scissors" and comp_choice == "rock":
        result = "you lose"
    elif user_choice == "paper" and comp_choice == "scissors":
        result = "you lose"

    else:
        result = "you win"
        rounds_won +=1

    feedback = "{} vs {}, {}".format(user_choice, comp_choice, result)

    outcome = "Round {}: {}".format(rounds_played + 1, feedback)
    game_summary.append(outcome)

    print(feedback)

    rounds_played += 1

    if mode == "infinite":
        rounds += 1

    if rounds_played == rounds:
        break



# Quick Calculations (stats)
rounds_lost = rounds_played - rounds_won - rounds_drawn

if rounds_played > 0:

    # **** Calculate Game Stats ******
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    print()
    print ("***** Game History *****")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics *******")
    print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%) \nTIe: {}, ({:.0f}%)".format(rounds_won,percent_win,rounds_lost,percent_lose,rounds_drawn,percent_tie))
    print()
    print("Thanks or playing")
else:
    print("Oops - you chickened out and did not play at all :(")



                