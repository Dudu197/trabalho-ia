import numpy as np
from a_star_search import AStarSearch
from node import Node


class Snake:
    search = AStarSearch()
    arena = []
    random = None
    BLANK = 0
    HEAD = 1
    BODY = 2
    FOOD = 3
    head_position = None
    body_position = []
    food_position = None
    points = -1

    # 0 = White space
    # 1 = Head
    # 2 = Body
    # 3 = Food
    def __init__(self, size, viewer, random):
        self._size = size
        self.viewer = viewer
        self.random = random
        self.arena = self.create_arena()
        head_start_x = self.random.randint(0, size[0] - 1)
        head_start_y = self.random.randint(0, size[1] - 1)
        self.set_head((head_start_x, head_start_y))
        self.create_food()

    def create_arena(self):
        return np.zeros(self._size)

    def set_head(self, position):
        x, y = position
        if self.head_position:
            self.arena[self.head_position.x, self.head_position.y] = self.BLANK
        self.head_position = Node(x, y)
        self.arena[x, y] = self.HEAD

    def move(self, node):
        if node == self.food_position:
            self.create_food()
        else:
            if node in self.body_position and node != self.body_position[0]:
                print("Game over")
                self.game_over()
            if self.body_position:
                self.body_position.pop(0)
        self.body_position.append(self.head_position.copy())
        self.head_position = node.copy()
        self.reset_prior()
        self.render()

    def reset_prior(self):
        self.head_position.prior = None
        self.food_position.prior = None
        for n in self.body_position:
            n.prior = None

    def render(self):
        self.viewer.update(self.head_position, self.body_position, self.food_position)

    def create_food(self):
        while True:
            new_food_position_x = self.random.randint(0, self._size[0] - 1)
            new_food_position_y = self.random.randint(0, self._size[1] - 1)
            food_node = Node(new_food_position_x, new_food_position_y)
            if food_node not in self.body_position and food_node != self.head_position and food_node != self.food_position:
                self.food_position = food_node
                self.points += 1
                print(f"Points: {self.points}")
                return food_node

    def game_over(self):
        print("Game over!")
        raise Exception("Game over!")

    def simulate_arena(self):
        arena = self.create_arena()
        for node in self.body_position:
            arena[node.x, node.y] = 1
        return arena

    def play(self):
        print("Let the game begin!")
        count = 0
        while True:
            count += 1
            if count == 22:#20:
                print("Vai dar ruim")
            caminho, custo, expanded = self.search.perform_search(self.simulate_arena(), self.head_position, self.food_position, self.body_position, self.viewer)
            if not caminho:
                self.viewer.pause()
            caminho.pop(0)
            for i in caminho:
                self.move(i)

