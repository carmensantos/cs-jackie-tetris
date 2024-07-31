import numpy as np


class Tile:

    def __init__(self, shape, color, pos_x=5, pos_y=0, rotation=0):
        self._shape = shape
        self._rotation = rotation
        self._color = color
        self._position = np.array([pos_x, pos_y])

    def render(self, board):
        matrix = self.get_coordinates()
        board.draw_tile(matrix, self._color)

    def get_coordinates(self):
        return self._shape.get_matrix_with_offset(self._rotation, self._position)

    def get_color(self):
        return self._color

    def rotate(self, direction):
        new_rotation = np.abs(np.mod(self._rotation + direction, self._shape.rotations_count))
        new_matrix = self._shape.get_matrix_with_offset(new_rotation, self._position)
        self._rotation = new_rotation
        return new_matrix

    def move(self, dx, dy):
        next_pos = self._position + np.array([dx, dy])
        tile_matrix = self._shape.get_matrix_with_offset(self._rotation, next_pos)
        self._position = next_pos
        return tile_matrix
