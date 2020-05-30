import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ['A']
for i in range(1,11):
    ranks.append(str(i))
ranks.append('J')
ranks.append('Q')
ranks.append('K')

values = { 'A': 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 
         }

class Cards:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
    
    def __str__(self):
        return self.ranks + ' of ' + self.suits

class Deck():
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Cards(rank, suit))
    def get_card(self):
        """
        Randomly chooses a card and remove it from the deck
        """
        random_card_index = random.randint(0, len(self.deck) - 1)
        card = self.deck.pop(random_card_index)
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
