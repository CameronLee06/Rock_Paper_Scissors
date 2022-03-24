import random


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " / "or an integer that is more than 0"
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



# Main routine goes here...

rounds_played = 0 
choose_instruction = "Please choose rock (r) , paper" / "(p) or scissors (s)"


# Ask user for # rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game =="no":
