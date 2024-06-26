from .search import Search


class BreadthFirstSearch(Search):
    name = "Breadth First"

    def perform_search(self, maze, start, goal, viewer):
        # nos gerados e que podem ser expandidos (vermelhos)
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
        while frontier:
            frontier_count += 1

            # seleciona o no mais antigo para ser expandido
            no_atual = frontier.pop(0)
            if no_atual == goal:
                goal_found = no_atual
                break

            # busca os vizinhos do no
            neighbors = no_atual.neighbors(maze)

            # para cada vizinho verifica se eh o goal e adiciona na
            # fronteira se ainda nao foi expandido e nao esta na fronteira
            for neighbor in neighbors:
                if neighbor not in expanded and neighbor not in frontier:
                    frontier.append(neighbor)

            expanded.add(no_atual)

            viewer.update(generated=frontier,
                          expanded=expanded)

        caminho = self.get_path(goal_found)
        custo = self.path_cost(caminho)

        return caminho, custo, expanded, frontier_count
