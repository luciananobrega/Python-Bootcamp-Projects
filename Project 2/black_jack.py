from cards import Deck, Hand
from player import Player
from chips import Chips

chips = Chips()

class BlackJack:

    def __init__(self):
        """
        Start game by instanciating the important classes
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

        self.partial_results(show_first_card=False)
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
            self.partial_results()
            self.check21_dealer()
        elif self.player.sum > 21:
            print("Player busts")
            print("You lose")
            chips.lose_bet()
            print(chips)
            self.player_action.check_play_again()

    def check21_dealer(self):
        if self.dealer.sum == 21:
            print("Dealer Blackjack!")
            if self.player.sum == 21:
                print("Push")
            else:
                print("You lose")
                chips.lose_bet()
        elif self.dealer.sum < 21:
            if self.dealer.sum <= self.player.sum:
                self.dealer_gets_card()
                self.partial_results()
                self.check21_dealer()
            else:
                print("You lose")
                chips.lose_bet()
        elif self.dealer.sum > 21:
                print("Dealer busts! You win!")
                chips.win_bet()
                
        print(chips)

        play_again = self.player_action.check_play_again()
        if play_again:
            self.main()

    def play(self):
        """
        Checks new action from player: hit or stand
        """
        action = self.player_action.next_action()
        if action == 'h':
            self.player_gets_card()
            self.partial_results(show_first_card=False)
            self.check21_player()
        if action == 's':
            self.partial_results()
            self.check21_dealer()
            self.dealer_gets_card()
            self.partial_results()
            self.check21_dealer()

    def partial_results(self, show_first_card = True):
        """
        Print partial results (cards on hands and sum)
        """
        print("*** Player ***")
        print(self.player)
        print("*** Dealer ***")
        p_dealer = self.dealer.__str__()
        if show_first_card is True:
            print(p_dealer)
        else: 
            p_dealer = p_dealer.split(':')[1].split(',')[1]
            print('Cards: X, ' + p_dealer + ': X')

    def main(self):
        chips.get_bet()
        bj = BlackJack()

if __name__ == '__main__':
    bj = BlackJack()
    bj.main()