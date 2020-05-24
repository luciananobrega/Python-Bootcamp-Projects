import random

class Cards:
    def __init__(self):
        self.all_cards = ['A']
        for i in range(1,11):
            self.all_cards.append(str(i))
        self.all_cards.append('J', 'Q', 'K')

    def values(self):
        self.values = { 'A': 10, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                        '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 
                     }

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)

    def get_card(self):
        """
        Chooses randomly a card and remove it from the deck
        """
        random_card_index = random.randint(0, len(self.all_cards))
        return self.all_cards.pop[random_card_index]

class Hand(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.hand_player = []
        self.hand_dealer = []
    
    def __str__(self):
        p     = "Player cards: " + self.hand_player
        p_sum = "    Sum:" + str(sum(self.hand_player))
        d     = "Dealer cards: " + self.hand_dealer
        d_sum = "    Sum:" + str(sum(self.dealer_player))

        return p + p_sum + d + d_sum

    def sum(self, hand):
        res = 0
        for el in hand:
            res += self.values[el]
        return res

    def add_card(self, card, pl):
        if pl == 'player':
            self.hand_player.append(card)
        elif pl == 'dealer':
            self.hand_dealer.append(card)
