from searches import *
from viewer import MazeViewer
from node import Node
import numpy as np
import pandas as pd
import time

search_methods = [BreadthFirstSearch(), DepthFirstSearch(), UniformCostSearch(), AStarSearch(), InteractiveDeepningDepthFirstSearch(), UniformCostNonCumulativeSearch(), AStarNonCumulativeSearch()]
# search_methods = [UniformCostSearch()]
df_results = pd.DataFrame(columns=["method", "experiment", "steps", "expanded", "cost", "time_duration"])


def create_maze(y_size, x_size, start, goal, wall_rate, random):
    """
    Only creates square mazes
    :param y_size: Height of the maze
    :param x_size: Width of the maze
    :param start: Beginning node
    :param goal: Ending node
    :param wall_rate: Rate of how many walls should appear
    :param random: np random state
    :return: The created maze
    """
    # cria labirinto vazio
    maze = [[0] * x_size for _ in range(y_size)]

    # adiciona celulas ocupadas em locais aleatorios de
    # forma que 25% do labirinto esteja ocupado
    numero_de_obstaculos = int(wall_rate * (y_size * x_size))
    for _ in range(numero_de_obstaculos):
        line = random.randint(0, y_size - 1)
        row = random.randint(0, x_size - 1)
        maze[line][row] = 1

    # remove eventuais obstaculos adicionados na posicao
    # inicial e no goal
    maze[start.y][start.x] = 0
    maze[goal.y][goal.x] = 0

    return maze


Y_SIZE = 300
X_SIZE = 300
WALL_RATE = 0.5
STEP_TIME = 40
ZOOM = 40
test_number = 1
should_render = False
seed = 42

for method in search_methods:
    random = np.random.RandomState(seed)
    print(f"Testing {method.name}")
    for i in range(test_number):
        START = Node(x=0, y=0)
        GOAL = Node(x=Y_SIZE - 1, y=X_SIZE - 1)

        """
        O labirinto sera representado por uma matriz (lista de listas)
        em que uma posicao tem 0 se ela eh livre e 1 se ela esta ocupada.
        """
        maze = create_maze(Y_SIZE, X_SIZE, START, GOAL, WALL_RATE, random)

        viewer = MazeViewer(maze, START, GOAL, step_time_miliseconds=STEP_TIME, zoom=ZOOM, should_render=should_render)

        # ----------------------------------------
        # BFS Search
        # ----------------------------------------
        viewer._figname = method.name
        start_time = time.time()
        caminho, custo_total, expandidos, gerados = method.perform_search(maze, START, GOAL, viewer)
        end_time = time.time()
        total_time = end_time - start_time
            # uniform_path_search(maze, START, GOAL, viewer)
        # a_star_search(labirinto, INICIO, GOAL, viewer)
        # depth_first_search(labirinto, INICIO, GOAL, viewer)
        # breadth_first_search(labirinto, INICIO, GOAL, viewer)

        if len(caminho) == 0:
            print("Goal é inalcançavel neste labirinto.")

        print(
            f"\tCusto total do caminho: {custo_total}.\n"
            f"\tNumero de passos: {len(caminho) - 1}.\n"
            f"\tNumero total de nos expandidos: {len(expandidos)}.\n"
            f"\tDuração (s): {total_time}.\n\n"
        )

        df_results = df_results.append([{
            "method": method.name,
            "experiment": i + 1,
            "steps": len(caminho),
            "expanded": len(expandidos),
            "generated": gerados,
            "cost": custo_total,
            "time_duration": total_time
            }], ignore_index=True)

        if should_render:
            viewer.update(path=caminho)
            viewer.pause()

    # ----------------------------------------
    # DFS Search
    # ----------------------------------------

    # ----------------------------------------
    # A-Star Search
    # ----------------------------------------

    # ----------------------------------------
    # Uniform Cost Search (Obs: opcional)
    # ----------------------------------------
df_results.to_json("result.json", orient="records")
print("Finalizado!")