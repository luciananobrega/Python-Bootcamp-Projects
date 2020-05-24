from cards import Deck, Hand

if __name__ == '__main__':
    deck = Deck()
    player = Hand()
    


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
