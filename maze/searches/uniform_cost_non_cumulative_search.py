from .search import Search


class UniformCostNonCumulativeSearch(Search):
    name = "Uniform Cost Non Cumulative"

    def nodes_abs_distance(self, current_node, previous_node):
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
        frontier_count = 0

        # Repete enquanto nos nao encontramos o goal e ainda
        # existem para serem expandidos na fronteira. Se
        # acabarem os nos da fronteira antes do goal ser encontrado,
        # entao ele nao eh alcancavel.
        while (len(frontier) > 0) and (goal_found is None):
            frontier_count += 1
            frontier = sorted(frontier, key=lambda x: x.distance)
            current_node = frontier.pop(0)
            if current_node == goal:
                goal_found = current_node
                break

            # busca os vizinhos do no
            vizinhos = current_node.neighbors(maze, expanded)

            for v in vizinhos:

                if v not in frontier and v not in expanded:
                    distance = self.nodes_abs_distance(v, goal)
                    v.distance = distance
                    frontier.append(v)

            if current_node.x != 0 or current_node.y != 0:
                expanded.add(current_node)
            viewer.update(generated=frontier,
                          expanded=expanded)

        caminho = self.get_path(goal_found)
        custo = self.path_cost(caminho)

        return caminho, custo, expanded, frontier_count