from .hill_climbing import HillClimbing
import numpy as np


class StochasticHillClimbing(HillClimbing):
    name = "Stochastic"
    board = None
    random = None
    queen_value = 2

    def perform_search(self, board, random, viewer):
        self.board = board.copy()
        self.random = random
        board_size = self.board.shape[0]
        queens = self.create_queens(board_size)
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
                    current_cost = self.calculate_attacking_queens(self.board, queens, (i, queens[i]))
                    options = [x for x in options if self.calculate_attacking_queens(self.board, x, (i, x[i])) <= current_cost]
                    if options:
                        self.random.shuffle(options)
                        best_option = options[0]
                        queens[i] = best_option[i]
                    else:
                        count_resolved += 1
                else:
                    count_resolved += 1
                viewer.update(self.board, queens)
                if count_resolved == board_size:
                    resolved = True
        print("Finished")
        return count
