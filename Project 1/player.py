class Player:
    def __init__(self, marker):
        self.marker = marker
    
    def play(self):
        try:
            return int(input("Player {}, choose a position: ".format(self.marker)))
        except:
            print("Invalid position. Try again.")
            return 0