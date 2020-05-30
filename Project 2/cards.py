import random

class Cards:
    def __init__(self):
        self.all_cards = ['A']
        for i in range(1,11):
            self.all_cards.append(str(i))
        self.all_cards.append('J')
        self.all_cards.append('Q')
        self.all_cards.append('K')
        self.values = { 'A': 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 
                     }

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)

    def get_card(self):
        """
        Randomly chooses a card and remove it from the deck
        """
        random_card_index = random.randint(0, len(self.all_cards) - 1)
        card = self.all_cards.pop(random_card_index)
        return card

class Hand(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.hand = []
        self.sum = 0


    def prt(self, show_first_card = True):
        if show_first_card == True:
            p     = "Cards: " + ', '.join(self.hand)
            self.result()
            p_sum = "  Sum: " + str(self.sum)
            print(p + p_sum)
        else:
            first_hand = self.hand[:]
            first_hand[0] = '_'
            print("Cards: " + ', '.join(first_hand))
            

    def result(self):
        """
        Calculates the value on hand
        """
        self.sum = 0
        for el in self.hand:
            self.sum += self.values[el]

    def add_card(self, card):
        """
        Includes card to hand
        """
        self.hand.append(card)
