class TicTacToe:
    def __init__(self):
        self.matrix = {1:'-',2:'-',3:'-',
                        4:'-',5:'-',6:'-',
                        7:'-',8:'-',9:'-'}
        self.turn = 0
        self.win = 0
        self.tie = 0
        self.winning_conditions = [[1,2,3],[4,5,6],[7,8,9],
                                   [1,4,7],[2,5,8],[3,6,9],
                                    [1,5,9],[3,5,7]]
        self.players = ['X','O']


    def matrix_print(self):
        print(self.matrix[1], " ", self.matrix[2], " ", self.matrix[3])
        print(self.matrix[4], " ", self.matrix[5], " ", self.matrix[6])
        print(self.matrix[7], " ", self.matrix[8], " ", self.matrix[9])

    def check_winner(self):
        for win_set in self.winning_conditions:

            if (self.matrix[win_set[0]] != '-') or (self.matrix[win_set[2]] != '-'):
                if (self.matrix[win_set[0]] == self.matrix[win_set[1]]) and (self.matrix[win_set[1]] == self.matrix[win_set[2]]):
                    print("Player " + self.matrix[win_set[0]] + " is winner !!!")
                    self.win = 1
        return self.win

    def check_tie(self):
        if all(cell == "X" or cell == "O" for cell in self.matrix):
            self.tie = 1
            print("Game is a Tie")
        return self.tie

    def process_input(self,input_x):
        if (0 < input_x <= 9) and self.matrix[input_x] == '-':
            self.matrix[input_x] = self.players[self.turn]
        else:
            print("Enter Valid input & game finished")

        self.turn = (self.turn + 1) % 2
        return self.matrix



game = TicTacToe()
game.matrix_print()
while True:
    input_x = int(input("player " + game.players[game.turn] + " :"))
    game.process_input(input_x)
    game.matrix_print()
    game.check_winner()
    game.check_tie()
    if game.win or game.tie:
        break


