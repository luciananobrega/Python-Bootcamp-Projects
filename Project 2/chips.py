class Chips:

    def __init__(self, initial=1000):
        self.total = initial
        self.get_bet()

    def __str__(self):
        p = "Chips balance: "
        return p + str(self.total)
    
    def get_bet(self):
        self.bet = int(input("Game Starts! What's your bet? "))
        if self.bet > self.total:
            print("Bet too high! Your balance is: {}".format(self.total))
            self.get_bet()
        return self.bet

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
