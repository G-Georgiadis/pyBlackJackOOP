from Deck import Deck
from Player import Player


class Game21:
    __player_list = []
    __deck = []

    def __init__(self):
        # Create Dealer and add to player list
        dealer = Player(is_dealer=True)
        self.__player_list.append(dealer)

        # Ask user for the number of players
        self.__number_of_players = self.__prompt_number_of_players()
        # Add players to the player list
        for i in range(self.__number_of_players):
            player = Player(is_dealer=False)
            self.__player_list.append(player)

        # Make the playing deck
        self.__deck = Deck()
        # print(self.__deck.show_cards())

        # Dealer draws first
        dealer.play(self.__deck)
        dealer.show_hand()
        print("Dealer sum is " + str(dealer.count_hand()))

        if dealer.count_hand() > 21:  # Dealer busted, players win
            print("Dealer busted! All players win")
            for player in self.__player_list:
                if not player.is_dealer:
                    player.win()
        elif dealer.count_hand() == 21:  # Dealer got 21, players lose
            print("Dealer drew 21. All players lose!")
            for player in self.__player_list:
                if not player.is_dealer:
                    player.lose()
        else:  # Dealer has valid hand, players take turns
            for player in self.__player_list:
                if not player.is_dealer:    # So that we skip iterating the dealer
                    player.play(self.__deck)
                    if player.count_hand() == 21:
                        player.win()
                    elif player.count_hand() > 21:
                        player.lose()
                    elif player.count_hand() > dealer.count_hand():
                        player.win()

    @staticmethod
    def __prompt_number_of_players():
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
