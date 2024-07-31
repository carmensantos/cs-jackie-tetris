import random

import numpy as np
import pygame

import shape
from tile import Tile


class Board:

    def __init__(self, screen, height=24, width=10):
        self._height = height
        self._width = width
        self._screen = screen
        self._matrix = np.zeros([width, height], dtype=int)
        self._current_tile = None
        self.score = 0
        self._colours = shape.generate_colours()
        self._shapes = shape.generate_shapes()

    def draw(self):
        block_size = 35  # Set the size of the grid block
        x_offset = 100
        y_offset = 50
        for x in range(0, self._width):
            for y in range(0, self._height):
                rect = pygame.Rect(x_offset + x * block_size, y_offset + y * block_size, block_size, block_size)
                pygame.draw.rect(self._screen, self._colours[self._matrix[x,y]], rect, 1 if self._matrix[x,y] == 0 else 0)

    def update(self, on_timer = True):
        if self._current_tile is None:
            self.create_tile()
        if on_timer:
            self._current_tile.move(0, 1)
        self._matrix[:, :] = 0
        self.draw_tile(self._current_tile)

    def create_tile(self):
        self._current_tile = Tile(self.get_shape(), self.get_colour(), random.randint(0,6))

    def get_shape(self):
        return self._shapes[random.randint(0, len(self._shapes) - 1)]

    def get_colour(self):
        return random.randint(1, len(self._colours) - 1)

    def draw_tile(self, tile):
        matrix = tile.get_coordinates()
        for pos in matrix:
            if pos[1] < self._height:
                self._matrix[pos[0], pos[1]] = tile.get_color()

    def on_key_up(self):
        self._current_tile.rotate(1)
        self.draw()

    def on_key_down(self):
        self._current_tile.move(0, 1)
        self.draw()

    def on_key_left(self):
        self._current_tile.move(-1, 0)
        self.draw()

    def on_key_right(self):
        self._current_tile.move(1, 0)
        self.draw()
