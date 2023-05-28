from .search import Search
import numpy as np


class DepthFirstSearch(Search):
    name = "Depth First"
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
        # diag_2 = np.diag(current_board, k=-1)
        count += len(row[row == self.queen_value]) - 1
        count += len(column[column == self.queen_value]) - 1
        count += len(diag_1[diag_1 == self.queen_value])
        # count += len(diag_2[diag_2 == self.queen_value])

        return count

    def perform_search(self, board, random, viewer):
        self.board = board.copy()
        self.random = random
        board_size = self.board.shape[0]
        queens = self.random.randint(low=0, high=board_size-1, size=board_size)
        viewer.update(self.board, queens)

        resolved = False
        count = 0

        while not resolved:
            count += 1
            arr = np.arange(board_size)
            self.random.shuffle(arr)
            count_resolved = 0
            for i in arr:
                options = []
                if self.calculate_attacking_queens(self.board, queens, (i, queens[i])) > 0:
                    for j in range(board_size):
                        if j != queens[i]:
                            option = queens.copy()
                            option[i] = j
                            options.append(option)
                    options = sorted(options, key=lambda x: self.calculate_attacking_queens(self.board, x, (i, x[i])))
                    options_cost = list(map(lambda x: self.calculate_attacking_queens(self.board, x, (i, x[i])), options))
                    best_option = options[0]
                    queens[i] = best_option[i]
                    # print("updating", i)
                else:
                    count_resolved += 1
                viewer.update(self.board, queens)
                if count_resolved == board_size:
                    resolved = True
        print("Finished")
        print(count)
        viewer.pause()
