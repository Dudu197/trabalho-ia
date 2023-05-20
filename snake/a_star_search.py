from math import sqrt, inf


class AStarSearch:
    name = "Uniform Cost"

    def perform_search(self, maze, start, goal, body, viewer):
        # remova o comando abaixo e coloque o codigo A-star aqui
        frontier = []
        # nos ja expandidos (amarelos)
        expanded = set(body)
        # adiciona o no inicial na fronteira
        frontier.append(start)

        # variavel para armazenar o goal quando ele for encontrado.
        goal_encontrado = None

        # Repete enquanto nos nao encontramos o goal e ainda
        # existem para serem expandidos na fronteira. Se
        # acabarem os nos da fronteira antes do goal ser encontrado,
        # entao ele nao eh alcancavel.
        while (len(frontier) > 0) and (goal_encontrado is None):
            frontier = sorted(frontier, key=lambda x: x.distance)
            no_atual = frontier.pop(0)

            # busca os vizinhos do no
            vizinhos = no_atual.neighbors(maze, expanded)

            for v in vizinhos:

                if v.y == goal.y and v.x == goal.x:
                    goal_encontrado = v
                    break

                if v not in frontier and v not in expanded:
                    distance = self.nodes_distance(v, goal)
                    v.distance = distance
                    frontier.append(v)

            if no_atual.x != 0 or no_atual.y != 0:
                expanded.add(no_atual)
            viewer.update_search(frontier, expanded, start, goal, no_atual)

        caminho = self.get_path(goal_encontrado)
        custo = self.path_cost(caminho)
        if len(caminho) == 0:
            print("zero")

        return caminho, custo, expanded

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