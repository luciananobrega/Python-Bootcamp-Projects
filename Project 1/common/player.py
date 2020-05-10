class Player:
    def __init__(self, marker):
        self.marker = marker
    
    def play(self):
        pos = input("Player {}, choose a position or press 'q' to quit: ".format(self.marker))
        if pos.lower() == 'q':
            print('Exiting game')
            return pos.lower()
        try:
            return int(pos)
        except:
            print("Invalid position. Try again or press 'q' to quit: ")
            return 0