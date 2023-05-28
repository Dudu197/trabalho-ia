
import cv2
import numpy as np

class MazeViewer():
    BLACK_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    RED_COLOR = (0, 0, 255)

    def __init__(self, labirinto, zoom=50, step_time_miliseconds=-1, should_render=True):
        self._labirinto = labirinto
        self._zoom = zoom
        self._step = step_time_miliseconds
        self._should_render = should_render

    def update(self, board, queens):
        if not self._should_render:
            return
        # To understand the image representation in opencv, refer to the following links:
        # https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/
        # https://codewords.recurse.com/issues/six/image-processing-101#:~:text=In%20OpenCV%2C%20images%20are%20represented,of%20values%20representing%20its%20color.&text=Where%20%5B72%2099%20143%5D%20%2C,values%20of%20that%20one%20pixel.
        maze_img = np.array(self._labirinto).astype(np.uint8) * 255

        # invert black and white pixels so that obstacles are black
        # and free areas are white.
        maze_img = 255 - maze_img
        maze_img = cv2.cvtColor(maze_img, cv2.COLOR_GRAY2BGR)

        self._draw_board(maze_img, board)
        self._draw_queens(maze_img, queens)

        maze_img = self._increase_image_size(maze_img, zoom=self._zoom)
        self._draw_grid(maze_img, self._zoom)

        cv2.imshow("view", maze_img)
        cv2.waitKey(self._step)

    def pause(self) -> None:
        cv2.waitKey(-1)

    def _increase_image_size(self, img, zoom=10):
        big_img = np.zeros((
            img.shape[0] * zoom,
            img.shape[1] * zoom,
            3
        ))

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                r_st = zoom * i
                r_end = zoom * (i + 1)
                c_st = zoom * j
                c_end = zoom * (j + 1)
                big_img[r_st: r_end, c_st: c_end] = img[i, j]

        return big_img

    def _draw_grid(self, maze_img, zoom):
        for i in range(0, maze_img.shape[1], zoom):
            cv2.line(
                maze_img,
                (i, 0),
                (i, maze_img.shape[0]),
                color=(0, 0, 0),
                thickness=1
            )

        for j in range(0, maze_img.shape[0], zoom):
            cv2.line(
                maze_img,
                (0, j),
                (maze_img.shape[1], j),
                color=(0, 0, 0),
                thickness=1
            )

    def _draw_board(self, maze_img, cells):
        for y in range(cells.shape[1]):
            for x in range(cells.shape[0]):
                color = self.RED_COLOR
                if cells[x, y] == 0:
                    color = self.WHITE_COLOR
                if cells[x, y] == 1:
                    color = self.BLACK_COLOR
                maze_img[y, x] = color

    def _draw_queens(self, maze_img, queens):
        x = 0
        for i in range(queens.shape[0]):
            color = self.RED_COLOR
            maze_img[queens[i], x] = color
            x += 1
