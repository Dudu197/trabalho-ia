from searches import *
from viewer import MazeViewer
import numpy as np
import pandas as pd
import time

# search_methods = [BreadthFirstSearch(), DepthFirstSearch(), UniformCostSearch(), AStarSearch(), InteractiveDeepningDepthFirstSearch(), UniformCostNonCumulativeSearch(), AStarNonCumulativeSearch()]
# search_methods = [UniformCostSearch()]
# df_results = pd.DataFrame(columns=["method", "experiment", "steps", "expanded", "cost", "time_duration"])


SIZE = 8
WALL_RATE = 0.5
STEP_TIME = 50
ZOOM = 80
test_number = 1
should_render = True
seed = 42

method = RandomRestartHillClimbing()
board = np.tile([[0, 1], [1, 0]], (int(SIZE / 2), int(SIZE / 2)))

random = np.random.RandomState(seed)
viewer = MazeViewer(board, step_time_miliseconds=STEP_TIME, zoom=ZOOM, should_render=should_render)
start_time = time.time()
method.perform_search(board, random, viewer)
end_time = time.time()
print("Total time (s):")
print(end_time - start_time)

if should_render:
    # viewer.update(path=caminho)
    viewer.pause()

# for method in search_methods:
#     random = np.random.RandomState(seed)
#     print(f"Testing {method.name}")
#     for i in range(test_number):
#         START = Node(x=0, y=0)
#         GOAL = Node(x=Y_SIZE - 1, y=X_SIZE - 1)
#
#         """
#         O labirinto sera representado por uma matriz (lista de listas)
#         em que uma posicao tem 0 se ela eh livre e 1 se ela esta ocupada.
#         """
#         maze = create_maze(Y_SIZE, X_SIZE, START, GOAL, WALL_RATE, random)
#
#         viewer = MazeViewer(maze, START, GOAL, step_time_miliseconds=STEP_TIME, zoom=ZOOM, should_render=should_render)
#
#         # ----------------------------------------
#         # BFS Search
#         # ----------------------------------------
#         viewer._figname = method.name
#         start_time = time.time()
#         caminho, custo_total, expandidos, gerados = method.perform_search(maze, START, GOAL, viewer)
#         end_time = time.time()
#         total_time = end_time - start_time
#             # uniform_path_search(maze, START, GOAL, viewer)
#         # a_star_search(labirinto, INICIO, GOAL, viewer)
#         # depth_first_search(labirinto, INICIO, GOAL, viewer)
#         # breadth_first_search(labirinto, INICIO, GOAL, viewer)
#
#         if len(caminho) == 0:
#             print("Goal é inalcançavel neste labirinto.")
#
#         print(
#             f"\tCusto total do caminho: {custo_total}.\n"
#             f"\tNumero de passos: {len(caminho) - 1}.\n"
#             f"\tNumero total de nos expandidos: {len(expandidos)}.\n"
#             f"\tDuração (s): {total_time}.\n\n"
#         )
#
#         df_results = df_results.append([{
#             "method": method.name,
#             "experiment": i + 1,
#             "steps": len(caminho),
#             "expanded": len(expandidos),
#             "generated": gerados,
#             "cost": custo_total,
#             "time_duration": total_time
#             }], ignore_index=True)
#
#         if should_render:
#             viewer.update(path=caminho)
#             viewer.pause()
#
#     # ----------------------------------------
#     # DFS Search
#     # ----------------------------------------
#
#     # ----------------------------------------
#     # A-Star Search
#     # ----------------------------------------
#
#     # ----------------------------------------
#     # Uniform Cost Search (Obs: opcional)
#     # ----------------------------------------
# df_results.to_json("result.json", orient="records")
print("Finalizado!")