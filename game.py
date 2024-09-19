class TicTakToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]  # single list to represent 3x3 board
        self.current_winner = None  # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

# Create an instance of the TicTakToe class and print the empty board
# if __name__ == '__main__':
#     run = TicTakToe()
#     TicTakToe.Print_board_nums()
