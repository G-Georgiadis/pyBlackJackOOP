from Game21 import Game21
from Player import Player


def prompt_number_of_players():
    """
    Gets the number of players selection after validating it
    :return: A valid number of players (1-4)
    """
    while True:
        try:
            user_input = int(input("How many players (1-4)? "))
            if 1 <= user_input <= 4:
                return user_input
        except ValueError:
            print("Please enter a number between 1 and 4.")


def prompt_play_again():
    while True:
        user_input = input("Would you like to play another round?")
        if user_input == 'n' or user_input == 'N':
            return False
        elif user_input == 'y' or user_input == 'Y':
            return True
        else:
            print("[Y]es or [N]")


def prompt_keep_players():
    user_input = input("Keep the same players?")
    if user_input == 'n' or user_input == 'N':
        return False
    elif user_input == 'y' or user_input == 'Y':
        return True
    else:
        print("[Y]es or [N]")


if __name__ == '__main__':
    player_list = []  # Create a list of players
    keep_players = False

    while True:

        if not keep_players:
            player_list.clear()
            dealer = Player(is_dealer=True)     # Create the dealer
            player_list.append(dealer)          # Add dealer to player list

            number_of_players = prompt_number_of_players()  # Ask number of players
            for i in range(number_of_players):
                player = Player(is_dealer=False)    # Create players
                player_list.append(player)          # Add players to list

        game = Game21(player_list)

        if not prompt_play_again():  # Exit the program
            break
        else:  # Play again
            keep_players = prompt_keep_players()
