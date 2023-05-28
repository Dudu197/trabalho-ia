from .hill_climbing import HillClimbing
import numpy as np


class RandomRestartHillClimbing(HillClimbing):
    name = "Random Restart"
    board = None
    random = None
    queen_value = 2
    num_restarts = 10
    max_iterations = 10

    def perform_search(self, board, random, viewer):
        self.board = board.copy()
        self.random = random
        board_size = self.board.shape[0]

        resolved = False
        count = 0

        for try_num in range(self.num_restarts):
            print(f"Starting {try_num} try")
            queens = self.create_queens(board_size)
            viewer.update(self.board, queens)
            count = 0
            for _ in range(self.max_iterations):
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
                        print("Finished")
                        return count
        print("Could not finish")
        print(count)
        return -count
