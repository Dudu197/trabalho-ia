from .hill_climbing import HillClimbing
import numpy as np


class FirstChoiceHillClimbing(HillClimbing):
    name = "First Choice"
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
                current_cost = self.calculate_attacking_queens(self.board, queens, (i, queens[i]))
                if self.calculate_attacking_queens(self.board, queens, (i, queens[i])) > 0:
                    changed = False
                    for j in range(board_size):
                        if j != queens[i]:
                            option = queens.copy()
                            option[i] = j
                            cost = self.calculate_attacking_queens(self.board, option, (i, option[i]))
                            if cost < current_cost:
                                queens[i] = option[i]
                                changed = True
                    if not changed:
                        count_resolved += 1
                else:
                    count_resolved += 1
                viewer.update(self.board, queens)
                if count_resolved == board_size:
                    resolved = True
        print("Finished")
        return count
