from Const import O, X
from Helpers import all_equal
from Result import Result


class TicTacToe:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.turn = X

    def board_reset(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.turn = X

    def print(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
        print()

    def move(self, position):
        if self.board[position - 1] == X or self.board[position - 1] == O:
            print("The position number is occupied")
            print()
            return False

        else:
            self.board[position - 1] = self.turn
            if self.turn == X:
                self.turn = O
            else:
                self.turn = X
            return True

    def is_draw(self):
        rows = [
            self.board[0:3],
            self.board[3:6],
            self.board[6:9],
            list(self.board[i] for i in (0, 4, 8)),
            list(self.board[i] for i in (2, 4, 6)),
            list(self.board[i] for i in (0, 3, 6)),
            list(self.board[i] for i in (1, 4, 7)),
            list(self.board[i] for i in (2, 5, 8))
        ]

        for row in rows:
            if not any(value in self.board for value in ("1", "2", "3", "4", "5", "6", "7", "8", "9")):
                if not all_equal(row):
                    return True
            else:
                return False

    def is_finished(self):
        if self.is_draw():
            return True
        elif (all_equal(self.board[0:3])
              or all_equal(self.board[3:6])
              or all_equal(self.board[6:9])
              or all_equal(list(self.board[i] for i in (0, 4, 8)))
              or all_equal(list(self.board[i] for i in (2, 4, 6)))
              or all_equal(list(self.board[i] for i in (0, 3, 6)))
              or all_equal(list(self.board[i] for i in (1, 4, 7)))
              or all_equal(list(self.board[i] for i in (2, 5, 8)))):
            return True
        else:
            return False

    def get_result(self):
        if not self.is_finished():
            return Result.NotFinished
        if self.is_draw():
            return Result.Draw
        if ((all_equal(self.board[0:3]) and self.board[0] == X)
                or (all_equal(self.board[3:6]) and self.board[3] == X)
                or (all_equal(self.board[6:9]) and self.board[6] == X)
                or (all_equal(list(self.board[i] for i in (0, 4, 8))) and self.board[0] == X)
                or (all_equal(list(self.board[i] for i in (2, 4, 6))) and self.board[2] == X)
                or (all_equal(list(self.board[i] for i in (0, 3, 6))) and self.board[0] == X)
                or (all_equal(list(self.board[i] for i in (1, 4, 7))) and self.board[1] == X)
                or (all_equal(list(self.board[i] for i in (2, 5, 8))) and self.board[2] == X)):
            return Result.X_Won
        else:
            return Result.O_Won
