class Chips:

    def __init__(self, initial=1000):
        self.total = initial
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet