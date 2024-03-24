# try:
    #     if yes_no_varibale == "N": break
    # except NameError:
    #     pass
import random
import os
turn_on = True
while turn_on:
    print("Drawing Players program----------------------------------------")
    #clearing function

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    # odd function
    def is_odd(number):
        return number % 2 == 1


    # the players list
    players_list = []
    matchs_list = []

    # ----------------- >input the players

    while True:
        # input the player and check if it's already exist or not
        while True:
            add_player_varible = input("ENTER THE PALYER'S NAME: ").capitalize()
            if add_player_varible not in players_list:
                players_list.append(add_player_varible)
                break
            else:
                print("ERROR!, The player is already exist")

        while True: # --> inquairy about yes , no
            try:
                yes_no_varibale = input("Do you want to add another player (Y/N)? ").upper()
                if yes_no_varibale in ("Y", "N"):
                    break
                else:
                    raise NameError
            except NameError:
                print("ERROR!: ENTER (Y) FOR YES OR (N) FOR NO")


        if yes_no_varibale == "Y":
            pass
        elif yes_no_varibale == "N":
            break
        else:
            print("UNEXPECKTED ERROR!")


    if is_odd(len(players_list)):
        players_list.append("UNKNOWN PLAYER!")
    else:
        pass

    # print(players_list)

    # taking players

    while len(players_list) > 0:
        the_first_player = players_list.pop(players_list.index(random.choice(players_list)))
        the_second_player = players_list.pop(players_list.index(random.choice(players_list)))
        temp_matchs_tuple = (the_first_player, the_second_player)
        matchs_list.append(temp_matchs_tuple)


     # input the matches in the dictionery


    matches_dict = {

    }

    for tu in range(len(matchs_list)):
        matches_dict[f"match {tu + 1} :"] = f"{matchs_list[tu][0]} VS {matchs_list[tu][1]}"

    # print(matches_dict)

    #clearing the screen
    clear_screen()

    #---------------> the matches screen
    print("Drawing Players program----------------------------------------")
    print("--------------------The matches--------------------")
    for key, value in matches_dict.items():
        new_string_varible = ""  # ----------> the string
        string_varible = f"|        {key}  {value}                               |" #----> the original varible
        while len(string_varible) != 51:
            if len(string_varible) < 51:
                string_varible = list(string_varible)
                string_varible.insert(-1, " ")
            elif len(string_varible) > 51:
                string_varible = list(string_varible)
                string_varible.pop(-2)
            else:
                print("UNEXPECKTED ERROR!")
        # restoring the string
        for rest in string_varible:
            new_string_varible = new_string_varible + rest
        print(new_string_varible)

    print("---------------------------------------------------")
    # ask if the user wanna end the program
    while True:
        end_program = input("Do you want to exit (Y/N)? ").upper()
        if end_program == "Y":
            turn_on = False
            break
        elif end_program == "N":
            clear_screen()
            break
        else:
            print("ERROR!: ENTER (Y) FOR YES OR (N) FOR NO")

# THANKS GOD الحمد لله تعالى
