import numpy as np


class Ground:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._matrix = np.zeros([width, height], dtype=int)
        self._coordinates = list()

    def merge(self, tile):
        coordinates = tile.get_coordinates()
        for position in coordinates:
            if (self._matrix[position[0], position[1]] != 0) or (position[0] >= self._width) \
                    or (position[1] >= self._height):
                print("ERROR")
            self._matrix[position[0], [position[1]]] = tile.get_color()
            self._coordinates.append(position)

    def get_matrix(self):
        return self._matrix

    def get_coordinates(self):
        return self._coordinates

    def expire_rows(self):
        row_count = 0
        for h in np.arange(1, self._height - 1):
            while np.all(self._matrix[:, self._height - h] != 0):
                self._cascade(self._height - h)
                row_count = row_count + 1
        if row_count != 0:
            self._recompute_coordinates()
        return row_count

    def _cascade(self, up_to):
        rows = np.arange(0, up_to)[::-1]
        for h in rows:
            self._matrix[:, h + 1] = self._matrix[:, h]
        self._matrix[:, 0] = 0

    def _recompute_coordinates(self):
        self._coordinates.clear()
        for x in np.arange(len(self._matrix)):
            for y in np.arange(len(self._matrix[x])):
                if self._matrix[x][y] != 0:
                    self._coordinates.append(np.array([x, y]))