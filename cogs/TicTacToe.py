class Game:
    def __init__(self):
        self.turn = 1
        self.piece = "X"
        self.spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display(self):
        print(self.spaces[0] + "|" + self.spaces[1] + "|" + self.spaces[2])
        print("-+-+-")
        print(self.spaces[3] + "|" + self.spaces[4] + "|" + self.spaces[5])
        print("-+-+-")
        print(self.spaces[6] + "|" + self.spaces[7] + "|" + self.spaces[8])

    def update(self, placement, piece):
        if(not (0 <= placement and placement <= 8)):
            print("Invalid placement! Please enter in a valid placement: ")
            return False
        if(self.spaces[placement] == "X" or self.spaces[placement] == "O"):
            print("Space is already filled! Please select another space:")
            return False
        else:
            self.spaces[placement] = piece
            return True

    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        
        for _ in range(9):
            print("It is X's turn! Please enter an empty space: ")
            self.display()
            placement = int(input())
            if(self.update(placement, self.piece)):
                self.turn = self.turn + 1
                self.piece = "O"
            else:
                placement = int(input())
                self.update(placement, self.piece)
            
            if(self.checkWinner()):
                return

            print("It is O's turn! Please enter an empty space: ")
            self.display()
            placement = int(input())
            if(self.update(placement, self.piece)):
                self.turn = self.turn + 1
                self.piece = "X"
            else:
                placement = int(input())
                self.update(placement, self.piece)
            
            if(self.checkWinner()):
                return

    def checkWinner(self):
        if (self.spaces[0] == self.spaces[1] == self.spaces[2] != " "):
            print(self.spaces[0] + " wins!")
            return 1
        elif (self.spaces[3] == self.spaces[4] == self.spaces[5] != " "):
            print(self.spaces[3] + " wins!")
            return 1
        elif (self.spaces[6] == self.spaces[7] == self.spaces[8] != " "):
            print(self.spaces[6] + " wins!")
            return 1
        elif (self.spaces[0] == self.spaces[3] == self.spaces[6] != " "):
            print(self.spaces[0] + " wins!")
            return 1
        elif (self.spaces[1] == self.spaces[4] == self.spaces[7] != " "):
            print(self.spaces[1] + " wins!")
            return 1
        elif (self.spaces[2] == self.spaces[5] == self.spaces[8] != " "):
            print(self.spaces[2] + " wins!")
            return 1
        elif (self.spaces[0] == self.spaces[4] == self.spaces[8] != " "):
            print(self.spaces[0] + " wins!")
            return 1
        elif (self.spaces[2] == self.spaces[4] == self.spaces[6] != " "):
            print(self.spaces[2] + " wins!")
            return 1

def main():
    game = Game()
    game.run()

main()