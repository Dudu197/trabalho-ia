from copy import copy as copyy


class Node:
    x = 0
    y = 0
    prior = None
    distance = 0
    cost = 0

    def __init__(self, x, y, prior=None, depth=0):
        self.x = x
        self.y = y
        self.prior = prior
        self.distance = 0
        self.cost = 0
        self.depth = depth

    def neighbors(self, maze, expanded=None):
        # generate neighbors of the current state
        neighbors = [
            Node(x=self.x + 0, y=self.y + 1, prior=self, depth=self.depth + 1),
            Node(x=self.x + 0, y=self.y - 1, prior=self, depth=self.depth + 1),
            Node(x=self.x + 1, y=self.y + 0, prior=self, depth=self.depth + 1),
            Node(x=self.x - 1, y=self.y + 0, prior=self, depth=self.depth + 1),
        ]

        # seleciona as celulas livres
        available_neighbors = []
        for neighbor in neighbors:
            # verifica se a celula esta dentro dos limites do labirinto
            if (neighbor.y < 0) or (neighbor.x < 0) or \
                    (neighbor.y >= len(maze)) or (neighbor.x >= len(maze[0])):
                    # or (expanded is not None and neighbor in expanded):
                continue
            # verifica se a celula esta livre de obstaculos.
            if neighbor not in expanded: #maze[neighbor.x][neighbor.y] == 0:
                available_neighbors.append(neighbor)

        return available_neighbors

    def copy(self):
        return copyy(self)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return other is not None and self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.__str__().__hash__()