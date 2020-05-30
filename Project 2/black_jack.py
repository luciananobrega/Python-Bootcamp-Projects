from cards import Deck, Hand

class BlackJack:

    def start(self):
        """
        Start game by instanciate the important classes
        """
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()
        self.session()
        self.session()

        self.partial_results()
        self.check21()

    def check21(self, stand = False):
        """
        Check if we have a winner
        """
        if not stand:
            if self.player.sum < 21 and self.dealer.sum < 21:
                self.next_action()
            if self.player.sum == 21:
                print("Player Blackjack!")
                self.session(stand = True)
            elif self.player.sum > 21:
                print("Player Bust")
                print("You lose")
                self.check_play_again()
        if self.dealer.sum == 21:
            print("Dealer Blackjack")
            print("You lose")
            self.check_play_again()
        elif self.dealer.sum > 21:
            print("Dealer Bust!")
            print("You win!")
            self.check_play_again()


    def session(self, stand = False):
        """
        Player and dealer take a card twice
        """
        card = self.deck.get_card()
        print("Player new card: {}".format(card))
        self.player.add_card(card)

        card = self.deck.get_card()
        self.dealer.add_card(card)
        print("Dealer new card: {}".format(card))

    def partial_results(self):
        """
        Print partial results (cards on hands and sum)
        """
        print("*** Player ***")
        print(self.player)
        print("*** Dealer ***")
        print(self.dealer)


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
