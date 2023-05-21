import Cards


class Player:
    def __init__(self, is_dealer: bool, score=0):
        self.__hand = []
        self.is_dealer = is_dealer
        self.__score = score
        if is_dealer:
            self.__name = 'Dealer'
        else:
            self.__name = input("Enter your name: ")

    def take_card(self, card: Cards.Card):
        self.__hand.append(card)

    def play(self, deck):
        if self.is_dealer:              # Dealer logic
            while self.count_hand() < 16:
                self.__hand.append(deck.draw())
        else:                           # Normal player logic
            for draw_num in range(2):   # Draw the 2 initial cards
                self.__hand.append((deck.draw()))

            while self.count_hand() < 21:   # While not busted
                self.show_hand()
                try:
                    user_input = input("{}: Draw another card? [y/n]".format(self.__name))
                    if user_input == 'y' or user_input == 'Y':
                        self.__hand.append((deck.draw()))
                    elif user_input == 'n' or user_input == 'N':
                        break
                except ValueError:
                    print("[Y]es or [N]o please")
            if self.count_hand() > 21:
                self.show_hand()
                print("{}: Busted!".format(self.__name))
                return self.count_hand()
            elif self.count_hand() == 21:
                self.show_hand()
                print("{}: 21!!!".format(self.__name))
                return self.count_hand()
            else:
                print("{}: Your final hand:".format(self.get_name()))
                self.show_hand()
                print("{}: sum of the cards in your hand is: {}".format(self.get_name(), self.count_hand()))
                return self.count_hand()

    def show_hand(self):
        for card in self.__hand:
            print(card.get_name())

    def count_hand(self):
        """
        Counts the value of the cards in the player's hand.
        Two aces count as 11, one ace counts as 10 if it doesn't make the player bust and 1 otherwise
        :return: The total value of the player's hand
        """
        sum_in_hand = 0
        number_of_aces = 0
        for card in self.__hand:
            if card.get_number() == 'A':
                number_of_aces += 1
            elif card.get_number() == '2':
                sum_in_hand += 2
            elif card.get_number() == '3':
                sum_in_hand += 3
            elif card.get_number() == '4':
                sum_in_hand += 4
            elif card.get_number() == '5':
                sum_in_hand += 5
            elif card.get_number() == '6':
                sum_in_hand += 6
            elif card.get_number() == '7':
                sum_in_hand += 7
            elif card.get_number() == '8':
                sum_in_hand += 8
            elif card.get_number() == '9':
                sum_in_hand += 9
            elif card.get_number() == '10':
                sum_in_hand += 10
            elif card.get_number() == 'J':
                sum_in_hand += 10
            elif card.get_number() == 'Q':
                sum_in_hand += 10
            elif card.get_number() == 'K':
                sum_in_hand += 10
        if number_of_aces == 2:
            sum_in_hand += 12
        elif number_of_aces == 1:
            if sum_in_hand + 11 <= 21:
                sum_in_hand += 11
            else:
                sum_in_hand += 1
        return sum_in_hand

    def win(self):
        self.__score += 1
        print("{}: You have gained a point!".format(self.__name))
        print("{}: Score is {}".format(self.__name, self.__score))

    def lose(self):
        self.__score -= 1
        print("{}: You have lost a point!".format(self.__name))
        print("{}: Score is {}".format(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def clear_hand(self):
        self.__hand.clear()
