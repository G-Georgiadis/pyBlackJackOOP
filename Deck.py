import random
import Cards


class Deck:
    """
    A deck of (initially) 52 playing cards.
    initialize() initializes the deck, returning it to its original (new deck) state
    draw() passes a card and removes it from the deck
    """
    __cards: [Cards]

    def __init__(self):
        """
        The default constructor.
        Initializes the cards list with all combinations of numbers and suits
        """
        self.__cards = []
        self.initialize()

    def initialize(self):
        """
        Initializes the deck with all the combinations of numbers and suits
        :return:
        """
        if len(self.__cards) > 0:       # If there are cards in the deck, empty it
            self.__cards.clear()

        for number in Cards.CardElements.numbers:
            for suit in Cards.CardElements.suits:
                self.__cards.append(Cards.Card(number, suit))
        random.shuffle(self.__cards)
        random.shuffle(self.__cards)

    def draw(self):
        """
        Pops (removes the last) card from the deck and returns it
        :return: Card: The last card from the deck
        """
        card = self.__cards.pop()
        return card

    def show_cards(self):
        card_names = []
        for card in self.__cards:
            card_names.append(card.get_name())
        return card_names
