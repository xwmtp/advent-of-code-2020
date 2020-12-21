

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

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def copy(self):
        return Grid([row.copy() for row in self.grid])
