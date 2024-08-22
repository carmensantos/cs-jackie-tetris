from enum import Enum
import numpy as np


class Collision(Enum):
    NONE = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3
    ROTATION = 4


class CollisionDetector:

    def __init__(self, board, ground):
        self._board = board
        self._ground = ground

    def check(self, tile_coordinates, dx, dy):
        board_collision = self.check_board(tile_coordinates)
        if board_collision != Collision.NONE:
            return board_collision
        return self.check_ground(tile_coordinates, dx, dy)

    def check_board(self, shape_coordinates):
        if np.max(shape_coordinates[:, 1]) >= self._board.height:
            return Collision.BOTTOM
        if np.max(shape_coordinates[:, 0]) >= self._board.width:
            return Collision.LEFT
        if np.min(shape_coordinates[:, 0]) < 0:
            return Collision.RIGHT
        return Collision.NONE

    def check_ground(self, tile_coordinates, dx, dy):
        ground_coordinates = self._ground.get_coordinates()
        for ground_coord_1 in ground_coordinates:
            for tile_coord_1 in tile_coordinates:
                if np.all(ground_coord_1 == tile_coord_1):
                    if dy > 0:
                        return Collision.BOTTOM
                    if dx > 0:
                        return Collision.RIGHT
                    if dx < 0:
                        return Collision.LEFT
                    if dx == 0 and dy == 0:
                        return Collision.ROTATION
                    return Collision.NONE
        return Collision.NONE


