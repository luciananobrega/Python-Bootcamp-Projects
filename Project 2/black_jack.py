from cards import Deck, Hand
from player import Player

class BlackJack:

    def __init__(self):
        """
        Start game by instanciate the important classes
        """
        self.deck = Deck()
        self.player_action = Player()
        self.player = Hand()
        self.dealer = Hand()
        self.start()

    def start(self):
        """
        Beginning of the game.
        Player starts with two cards.
        Dealer starts with two cards, but one is faced down
        """
        self.player_gets_card()
        self.dealer_gets_card(first_round=True)
        self.player_gets_card()
        self.dealer_gets_card()

        self.partial_results(show_first_card = False)
        self.check21_player()

    def player_gets_card(self):
        """
        Player gets a new card from the deck
        """
        card = self.deck.get_card()
        print("Player new card: {}".format(card))
        self.player.add_card(card)
    
    def dealer_gets_card(self, first_round = False):
        """
        Dealer gets a new card from the deck
        """
        card = self.deck.get_card()
        self.dealer.add_card(card)
        if first_round == True:
            print("Dealer new card: X")
        else:
            print("Dealer new card: {}".format(card))

    def check21_player(self):
        """
        Check value of sum
        """
        if self.player.sum < 21:
            self.play()
        if self.player.sum == 21:
            print("Player Blackjack!")
            self.dealer_play()
        elif self.player.sum > 21:
            print("Player Bust")
            print("You lose")
            self.player_action.check_play_again()

    def check21_dealer(self):
        if self.dealer.sum < self.player.sum():
            self.dealer_gets_card()
            self.check21_dealer()
        elif self.dealer.sum == 21:
            print("Dealer Blackjack!")
            if self.player.sum == 21:
                print("Push")
            else:
                print("You lose")
        elif self.dealer.sum > self.player.sum:
            print("You win!")
        else:
            print("Push")
        
        self.player_action.check_play_again()

    def play(self):
        """
        Checks new action from player: hit or stand
        """
        action = self.player_action.next_action()
        if action == 'h':
            self.player_gets_card()
            self.partial_results()
            self.check21_player()
        if action == 's':
            self.dealer_gets_card()
            self.partial_results()


    def partial_results(self, show_first_card = True):
        """
        Print partial results (cards on hands and sum)
        """
        print("*** Player ***")
        self.player.prt()
        print("*** Dealer ***")
        self.dealer.prt(show_first_card)


if __name__ == '__main__':
    bj = BlackJack()
    bj.start()


# player gets card
# dealer gets card
# check_winner

# player goal: get closer to 21 than the dealer
## possible actions:
### hit: receive another card
### stand: stop receiving cards
## if the player keeps hitting goes over 21, they bust and lose

# computer dealer: plays after the player
## if player is under 21, dealer then hits until they either beat the player or the dealer bursts

# Jack, Queen and King = 10
# Ace can be either 1 or 11 (player chooses when A appears)

# you win
# dealer wins

# CARDS:
## cards
## convert to numbers

# DECK
## send card

# HAND
## sum
## take_card

# GAME
## check_action (nothing, bust, blackjack, push)
## push: player has 21, dealer keeps hitting and also gets 21
