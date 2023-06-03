from .search import Search


class DepthFirstSearch(Search):
    name = "Depth First"

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
        while (len(frontier) > 0) and (goal_found is None):
            frontier_count += 1
            current_node = frontier.pop(0)
            if current_node == goal:
                goal_found = current_node
                break

            # busca os vizinhos do no
            neighbors = current_node.neighbors(maze, expanded)
            frontier[:0] = [n for n in neighbors if n not in frontier and n not in expanded]

            expanded.add(current_node)
            viewer.update(generated=frontier,
                          expanded=expanded)

        path = self.get_path(goal_found)
        cost = self.path_cost(path)

        return path, cost, expanded, frontier_count
