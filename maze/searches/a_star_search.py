from .search import Search


class AStarSearch(Search):
    name = "A Star"

    def calculate_h(self, current_node, previous_node):
        return abs(current_node.x - previous_node.x) + abs(current_node.y - previous_node.y)

    def perform_search(self, maze, start, goal, viewer):
        # remova o comando abaixo e coloque o codigo A-star aqui
        frontier = []
        # nos ja expandidos (amarelos)
        expanded = set()
        # adiciona o no inicial na fronteira
        frontier.append(start)

        # variavel para armazenar o goal quando ele for encontrado.
        goal_found = None

        # Repete enquanto nos nao encontramos o goal e ainda
        # existem para serem expandidos na fronteira. Se
        # acabarem os nos da fronteira antes do goal ser encontrado,
        # entao ele nao eh alcancavel.
        while (len(frontier) > 0) and (goal_found is None):
            frontier = sorted(frontier, key=lambda x: x.cost)
            current_node = frontier.pop(0)

            # busca os vizinhos do no
            neighbor = current_node.neighbors(maze, expanded)

            for v in neighbor:

                if v.y == goal.y and v.x == goal.x:
                    goal_found = v
                    break

                if v not in frontier and v not in expanded:
                    distance = self.nodes_distance(v, goal)
                    cost = self.calculate_h(v, current_node)
                    v.distance = current_node.distance + distance
                    v.cost = v.distance + cost
                    frontier.append(v)

            if current_node.x != 0 or current_node.y != 0:
                expanded.add(current_node)
            viewer.update(generated=frontier,
                          expanded=expanded)

        caminho = self.get_path(goal_found)
        custo = self.path_cost(caminho)

        return caminho, custo, expanded