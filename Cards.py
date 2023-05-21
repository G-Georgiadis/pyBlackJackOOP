class CardElements:
    """
    The elements used in a standard playing card deck.
    numbers:    The numbers including faces.
    suite:      The suits ( Spades, Heart, Clubs, Diamonds).
    """
    numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = (u'\u2660', u'\u2665', u'\u2663', u'\u2666')


class Card:
    """
    A playing card.
    It has a number (or face) and a suit.
    """
    def __init__(self, number, suit):
        self.__number = number
        self.__suit = suit

    def get_number(self):
        return self.__number

    def get_suit(self):
        return self.__suit

    def get_name(self):
        return "{}{}".format(self.__number, self.__suit)
