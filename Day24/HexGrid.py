from copy import deepcopy

DIRECTIONS = {
    'se' : ( 1,  1),
    'sw' : ( 1,  0),
    'nw' : (-1, -1),
    'ne' : (-1,  0),
    'e': (0, 1),
    'w': (0, -1),
}

class HexGrid:

    def __init__(self, default = 'W'):
        self.grid = {0 : {0 : default}}
        self.ax_ranges = {
            'y' : (0, 1),
            'x' : (0, 1)
        }
        self.default = default

    def get_adjacent_coords(self, y, x):
        return [(y + dy, x + dx) for dy, dx in DIRECTIONS.values()]

    def get_tile_coords(self, tile):
        y, x = 0, 0
        while tile != '':
            for dir in DIRECTIONS:
                if tile.startswith(dir):
                    dx, dy = DIRECTIONS[dir]
                    y += dy
                    x += dx
                    tile = tile.replace(dir, '', 1)
                    break
        return y, x

    def flip_tile(self, tile):
        y, x = self.get_tile_coords(tile)
        if self.get(y, x) == '.':
            self.set(y, x, 'W')
        elif self.get(y, x) == 'W':
            self.set(y, x, '.')

    def get(self, y, x):
        try:
            return self.grid[y][x]
        except KeyError:
            return self.default

    def set(self, y, x, char):
        if y not in self.grid:
            self.grid[y] = {}
            self.update_range(y, 'y')
        self.update_range(x, 'x')
        self.grid[y][x] = char

    def update_range(self, coord, ax):
        ax_min, ax_max = self.ax_ranges[ax]
        if coord < ax_min:
            ax_min = coord
        if coord >= ax_max:
            ax_max = coord + 1
        self.ax_ranges[ax] = (ax_min, ax_max)

    def count_occurence(self, target):
        occurences = 0
        for y in range(*self.ax_ranges['y']):
            for x in range(*self.ax_ranges['x']):
                if self.get(y,x) == target:
                    occurences += 1
        return occurences

    def __str__(self):
        string = ''
        for y in range(*self.ax_ranges['y']):
            row = ''
            for x in range(*self.ax_ranges['x']):
                if y==0 and x==0:
                    row += 'X'
                else:
                    row += self.get(y, x)
            string += row + '\n'
        return string

    def copy(self):
        new_grid = HexGrid()
        new_grid.grid = deepcopy(self.grid)
        new_grid.ax_ranges = deepcopy(self.ax_ranges)
        new_grid.default = self.default
        return new_grid
