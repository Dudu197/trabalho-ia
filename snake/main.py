from viewer import MazeViewer
from snake import Snake
import numpy as np

size = (10, 10)
step_time = 250
random = np.random.RandomState(42)

viewer = MazeViewer(size, step_time_miliseconds=step_time)

snake = Snake((10, 10), viewer, random)
snake.render()
snake.play()
