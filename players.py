from random import randint

class Player:
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid = False
        while valid == False:
            game.print_numboard()
            print()
            square = input(f"{self.letter}'s turn\nEnter a square: ")
            print("")
            try:
                val = int(square)
                if val not in game.check_available():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid Input - Try again\n")
        return val


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid = False
        while valid == False:
            val = randint(0, 9)
            if val in game.check_available():
                valid = True
        return val
