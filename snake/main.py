from viewer import MazeViewer
from snake import Snake
import numpy as np

size = (10, 10)
zoom = 50
step_time = 50
random = np.random#.RandomState(42)
render_snake = True
render_path = False

viewer = MazeViewer(size, zoom=zoom, step_time_miliseconds=step_time, render_snake=render_snake, render_path=render_path)

snake = Snake(size, viewer, random)
snake.render()
snake.play()
