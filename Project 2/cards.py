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


class Hand():
    def __init__(self):
        self.hand = []
        self.sum = 0

    def __str__(self, show_first_card = True):
        if show_first_card == True:
            p     = "Cards: " + ', '.join(i.__str__() for i in self.hand)
            p_sum = "  Sum: " + str(self.result())
            return p + p_sum
        else:
            first_hand = self.hand[1:]
            return "Cards: _, " + ', '.join(i.__str__() for i in self.hand[1:])
            
    def result(self):
        """
        Calculates the value on hand
        """
        self.sum = 0
        for card in self.hand:
            self.sum += values[card.ranks]
        return self.sum

    def add_card(self, card):
        """
        Includes card to hand
        """
        self.hand.append(card)


if __name__ == '__main__':
    deck = Deck()
    player = Hand()
    c = Cards('7', 'Hearts')
    player.add_card(c)
    player.result()
    print(player.sum)