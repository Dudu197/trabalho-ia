from abc import ABC, abstractmethod
import numpy as np


class HillClimbing(ABC):
    name = None
    board = None
    random = None
    queen_value = 2

    def calculate_board(self, board, queens):
        current_board = board.copy()
        x = 0
        for y in queens:
            current_board[x, y] = self.queen_value
            x += 1
        return current_board

    def get_diagonal(self, array, x, y):
        diags = []
        size = self.board.shape[0]
        for i in range(1, size):
            diags.append([x + i, y + i])
            diags.append([x - i, y - i])
            diags.append([x + i, y - i])
            diags.append([x - i, y + i])
        diags = list(filter(lambda i: (0 <= i[0] < size and 0 <= i[1] < size), diags))
        return np.array(list(map(lambda i: array[i[0], i[1]], diags)))

    def calculate_attacking_queens(self, board, queens, queen):
        current_board = self.calculate_board(board, queens)
        count = 0
        x = queen[0]
        y = queen[1]
        row = current_board[x, :]
        column = current_board[:, y]
        diag_1 = self.get_diagonal(current_board, x, y)
        count += len(row[row == self.queen_value]) - 1
        count += len(column[column == self.queen_value]) - 1
        count += len(diag_1[diag_1 == self.queen_value])
        return count

    def create_queens(self, board_size):
        return self.random.randint(low=0, high=board_size - 1, size=board_size)

    @abstractmethod
    def perform_search(self, board, random, viewer):
        pass
