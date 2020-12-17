from copy import deepcopy

class Grid3D:

    def __init__(self, slice, default = '.'):
        self.grid = {0 : slice_to_dict(slice)}
        self.ax_ranges = {
            'z' : (0,  1),
            'y' : (0, len(slice)),
            'x' : (0, len(slice[0]))
        }
        self.default = default

    def get_adjacent_coords(self, z, y, x):
        adjacents = []
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    adj_z = z + dz
                    adj_y = y + dy
                    adj_x = x + dx
                    if dz != 0 or dy != 0 or dx != 0:
                        adjacents.append((adj_z, adj_y, adj_x))
        return adjacents

    def get(self, z, y, x):
        try:
            return self.grid[z][y][x]
        except KeyError:
            return self.default

    def set(self, z, y, x, char):
        if z not in self.grid:
            self.grid[z] = {}
            self.update_range(z, 'z')
        if y not in self.grid[z]:
            self.grid[z][y] = {}
            self.update_range(y, 'y')
        self.update_range(x, 'x')
        self.grid[z][y][x] = char

    def update_range(self, coord, ax):
        ax_min, ax_max = self.ax_ranges[ax]
        if coord < ax_min:
            ax_min = coord
        if coord >= ax_max:
            ax_max = coord + 1
        self.ax_ranges[ax] = (ax_min, ax_max)

    def count_occurence(self, target):
        occurences = 0
        for z in range(*self.ax_ranges['z']):
            for y in range(*self.ax_ranges['y']):
                for x in range(*self.ax_ranges['x']):
                    if self.get(z,y,x) == target:
                        occurences += 1
        return occurences

    def __str__(self):
        string = ''
        for z in range(*self.ax_ranges['z']):
            string += f'z={z}\n'
            for y in range(*self.ax_ranges['y']):
                row = ''
                for x in range(*self.ax_ranges['x']):
                    if y==0 and x==0:
                        row += 'X'
                    else:
                        row += self.get(z,y,x)
                string += row + '\n'
        return string

    def copy(self):
        new_grid = Grid3D([''])
        new_grid.grid = deepcopy(self.grid)
        new_grid.ax_ranges = self.ax_ranges
        new_grid.default = self.default
        return new_grid

def slice_to_dict(slice):
    dct = {}
    for y, row in enumerate(slice):
        for x, char in enumerate(row):
            if not y in dct:
                dct[y] = {}
            dct[y][x] = char
    return dct
