import random


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


# Ask user for # rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game =="no":

    # Rounds Heading 
    print()
    if rounds == "":
        heading = "Infinite Mode: Round {}".format(rounds_played + 1)
        print(heading)
        if rounds == rounds_played == rounds + 1:
            break
    else: 
        heading = "Round {} of {}".format(rounds_played + 1, rounds)


    print(heading)
    choose = choice_checker(choose_instruction, rps_list, "Please enter R / P / S")


    # End game if exit code is typed
    if choose == rounds_played == rounds - 1:
        break

    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played +=1

print("Thank you for playing")
