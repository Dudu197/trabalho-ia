class Node:
    x = 0
    y = 0
    prior = None
    distance = 0
    cost = 0

    def __init__(self, y, x, prior=None, depth=0):
        self.x = x
        self.y = y
        self.prior = prior
        self.distance = 0
        self.cost = 0
        self.depth = depth

    def neighbors(self, maze, expanded=None):
        # generate neighbors of the current state
        neighbors = [
            Node(y=self.y + 1, x=self.x + 0, prior=self, depth=self.depth + 1),
            Node(y=self.y + 1, x=self.x - 1, prior=self, depth=self.depth + 1),
            Node(y=self.y + 1, x=self.x + 1, prior=self, depth=self.depth + 1),
            Node(y=self.y + 0, x=self.x + 1, prior=self, depth=self.depth + 1),
            Node(y=self.y - 1, x=self.x + 1, prior=self, depth=self.depth + 1),
            Node(y=self.y - 1, x=self.x + 0, prior=self, depth=self.depth + 1),
            Node(y=self.y - 1, x=self.x - 1, prior=self, depth=self.depth + 1),
            Node(y=self.y + 0, x=self.x - 1, prior=self, depth=self.depth + 1),
        ]

        # seleciona as celulas livres
        available_neighbors = []
        for neighbor in neighbors:
            # verifica se a celula esta dentro dos limites do labirinto
            if (neighbor.y < 0) or (neighbor.x < 0) or \
                    (neighbor.y >= len(maze)) or (neighbor.x >= len(maze[0])) \
                    or (neighbor.x == 0 and neighbor.y == 0) \
                    and (expanded is None or neighbor in expanded):
                continue
            # verifica se a celula esta livre de obstaculos.
            if maze[neighbor.y][neighbor.x] == 0:
                available_neighbors.append(neighbor)

        return available_neighbors

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.__str__().__hash__()