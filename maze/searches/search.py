from abc import ABC
from math import sqrt, inf


class Search(ABC):
    name: str = ""

    def perform_search(self, maze, start, goal, viewer):
        pass

    def get_path(self, goal):
        path = []

        current_node = goal
        while current_node is not None:
            path.append(current_node)
            current_node = current_node.prior

        # o caminho foi gerado do final para o
        # comeco, entao precisamos inverter.
        path.reverse()

        return path

    def path_cost(self, path):
        if len(path) == 0:
            return inf

        total_cost = 0
        for i in range(1, len(path)):
            total_cost += self.nodes_distance(path[i].prior, path[i])

        return total_cost

    def nodes_distance(self, node_1, node_2):
        dx = node_1.x - node_2.x
        dy = node_1.y - node_2.y
        return sqrt(dx ** 2 + dy ** 2)
