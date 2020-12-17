from copy import deepcopy

class Grid4D:

    def __init__(self, slice, default = '.'):
        self.grid = {0 : {0 : slice_to_dict(slice)}}
        self.ax_ranges = {
            'w' : (0, 1),
            'z' : (0, 1),
            'y' : (0, len(slice)),
            'x' : (0, len(slice[0])),
        }
        self.default = default

    def get_adjacent_coords(self, w, z, y, x):
        adjacents = []
        for dw in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        adj_w = w + dw
                        adj_z = z + dz
                        adj_y = y + dy
                        adj_x = x + dx
                        if dw != 0 or dz != 0 or dy != 0 or dx != 0:
                            adjacents.append((adj_w, adj_z, adj_y, adj_x))
        return adjacents

    def get(self, w, z, y, x):
        try:
            return self.grid[w][z][y][x]
        except KeyError:
            return self.default

    def set(self, w, z, y, x, char):
        if w not in self.grid:
            self.grid[w] = {}
            self.update_range(w, 'w')
        if z not in self.grid[w]:
            self.grid[w][z] = {}
            self.update_range(z, 'z')
        if y not in self.grid[w][z]:
            self.grid[w][z][y] = {}
            self.update_range(y, 'y')
        self.update_range(x, 'x')
        self.grid[w][z][y][x] = char

    def axes(self):
        return self.ax_ranges.keys()

    def update_range(self, coord, ax):
        ax_min, ax_max = self.ax_ranges[ax]
        if coord < ax_min:
            ax_min = coord
        if coord >= ax_max:
            ax_max = coord + 1
        self.ax_ranges[ax] = (ax_min, ax_max)

    def count_occurence(self, target):
        occurences = 0
        for w in range(*self.ax_ranges['w']):
            for z in range(*self.ax_ranges['z']):
                for y in range(*self.ax_ranges['y']):
                    for x in range(*self.ax_ranges['x']):
                        if self.get(w,z,y,x) == target:
                            occurences += 1
        return occurences

    def __str__(self):
        string = ''
        for w in range(*self.ax_ranges['w']):
            for z in range(*self.ax_ranges['z']):
                string += f'z={z}, w={w}\n'
                for y in range(*self.ax_ranges['y']):
                    row = ''
                    for x in range(*self.ax_ranges['x']):
                        if y==0 and x==0:
                            row += 'X'
                        else:
                            row += self.get(w,z,y,x)
                    string += row + '\n'

        return string

    def copy(self):
        new_grid = Grid4D([''])
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
