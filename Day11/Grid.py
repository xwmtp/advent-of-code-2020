import copy

class Grid:

    def __init__(self, rows):
        self.grid = rows

    def size(self):
        if len(self.grid) > 0:
            return (len(self.grid), len(self.grid[0]))
        else:
            return (0, 0)

    def get(self, y, x):
        return self.grid[y][x]

    def set(self, y, x, to):
        self.grid[y][x] = to

    def count_occurence(self, target):
        occurences = 0
        for row in self.grid:
            for char in row:
                if char == target:
                    occurences += 1
        return occurences

    def get_adjacent_coords(self, y, x):
        adjacents = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                adj_y = y + dy
                adj_x = x + dx
                if adj_y >= 0 and adj_y < self.size()[0] and adj_x >= 0 and adj_x < self.size()[0]:
                    adjacents.append((adj_y, adj_x))
        if (y, x) in adjacents:
            adjacents.remove((y, x))
        return adjacents

    def __str__(self):
        return ''.join([''.join(row) for row in self.grid])

    def __copy__(self):
        return Grid([row.copy() for row in self.grid])
