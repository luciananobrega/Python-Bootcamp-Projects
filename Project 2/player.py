class Player:
    def next_action(self):
        """
        Player can choose the next action: hit or stand
        """
        action = input("Next action: Hit (H)/Stand (S) ")

        if action.lower() == "h" or action.lower() == "s":
            return action.lower()
        else:
            print("Option not recognized. Try again.")
            self.next_action()

    def check_play_again(self):
        """
        Asks player if wants to play again
        """
        opt = input("You want to play it again? Y/N ")
        if opt.lower() == 'y':
            return True
        elif opt.lower() == 'n':
            return False
        else:
            print("Option not recognized. Try again.")
            self.check_play_again()