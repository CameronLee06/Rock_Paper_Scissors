rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1


        # compare options...
        if user_choice == comp_choice:
            result = "tie"
        
        elif user_choice == "rock" and comp_choice == "paper":
            result = "lose"
        elif user_choice == "scissors" and comp_choice == "rock":
            result = "lose"
        elif user_choice == "paper" and comp_choice == "scissors":
            result = "lose"

        else:
            result = "win"
        




        print("You chose {}, the computer chose {}. "
                " \nResult:  {}".format(user_choice, comp_choice, result))

                