from .search import Search


class UniformCostSearch(Search):
    name = "Uniform Cost"

    def perform_search(self, maze, start, goal, viewer):
        # remova o comando abaixo e coloque o codigo A-star aqui
        frontier = []
        # nos ja expandidos (amarelos)
        expanded = set()
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
            viewer.update(generated=frontier,
                          expanded=expanded)

        caminho = self.get_path(goal_encontrado)
        custo = self.path_cost(caminho)

        return caminho, custo, expanded