from .search import Search


class InteractiveDeepningDepthFirstSearch(Search):
    name = "Interactive Deepening Depth First"

    def perform_search(self, maze, start, goal, viewer):
        # nos gerados e que podem ser expandidos (vermelhos)
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
            current_node = frontier.pop(0)

            # busca os vizinhos do no
            neighbors = current_node.neighbors(maze, expanded)
            frontier[:0] = [n for n in neighbors if n not in frontier and n not in expanded]
            frontier = sorted(frontier, key=lambda x: x.depth)

            for neighbor in neighbors:
                if neighbor.y == goal.y and neighbor.x == goal.x:
                    goal_found = neighbor
                    # encerra o loop interno
                    break

            if current_node.x != 0 or current_node.y != 0:
                expanded.add(current_node)
            viewer.update(generated=frontier,
                          expanded=expanded)

        path = self.get_path(goal_found)
        cost = self.path_cost(path)

        return path, cost, expanded
