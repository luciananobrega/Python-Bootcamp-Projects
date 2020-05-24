from cards import Deck, Hand


class BlackJack:

    def start(self):
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()
        self.session()

    def check21(self, endgame = False):
        if not endgame:
            if self.player.sum == 21:
                print("Player Blackjack!")
                self.session(endgame = True)
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
        if player < 21 and dealer < 21:
            self.next_action()

    def session(self, endgame = False):
        if not endgame:
            card = self.deck.get_card()
            print("Player new card: {}".format(card))
            self.player.add_card(card)
        
        card = self.deck.get_card()
        self.dealer.add_card(card)
        print("Dealer new card: {}".format(card))

        self.partial_results()
        self.check21()
    
    def partial_results(self):
        print("*** Player ***\n")
        print(self.player)
        print("\n*** Dealer ***\n")
        print(self.dealer)


    def next_action(self):
        action = input("Next action: Hit (H)/Stand (S)")

        if action.lower() == "h":
            self.session()
        elif action.lower() == "s":
            self.stand()
        else:
            print("Option not recognized. Try again.")
            self.next_action()

    def check_play_again(self):
        opt = input("You want to play it again? Y/N")
        if opt.lower == 'y':
            self.start()
        elif opt.lower == 'n':
            return 0
        else:
            print("Option not recognized. Try again.")
            self.check_play_again()

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
