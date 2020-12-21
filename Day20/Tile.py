from Grid import Grid

class Tile:
    def __init__(self, id_str, tile_rows):
        self.id = int(id_str.replace('Tile ', '').replace(':',''))
        self.grid = Grid(tile_rows)
        self.transformed_grid = self.grid.copy()

    def bottom(self, flip=False):
        max_x, max_y = self.transformed_grid.size()
        return transform([self.transformed_grid.get(max_y-1, x) for x in range(max_x)], flip)

    def top(self, flip=False):
        max_x, max_y = self.transformed_grid.size()
        return transform([self.transformed_grid.get(0, x) for x in range(max_x)], flip)

    def left(self, flip=False):
        max_x, max_y = self.transformed_grid.size()
        return transform([self.transformed_grid.get(y, 0) for y in range(max_y)], flip)

    def right(self, flip=False):
        max_x, max_y = self.transformed_grid.size()
        return transform([self.transformed_grid.get(y, max_x-1) for y in range(max_y)], flip)

    def borders(self):
        return {
            'top' : self.top(),
            'bottom' : self.bottom(),
            'left' : self.left(),
            'right': self.right(),
            'top-flip': self.top(flip=True),
            'bottom-flip': self.bottom(flip=True),
            'left-flip': self.left(flip=True),
            'right-flip': self.right(flip=True),
        }

    def rotate_clockwise(self, flip=False):
        if flip:
            to_rotate = [row[::-1] for row in self.transformed_grid.grid]
        else:
            to_rotate = self.transformed_grid.grid
        self.transformed_grid.grid = list(zip(*to_rotate[::-1]))

    def __str__(self):
        return f"{self.id}\n{str(self.transformed_grid)}"

def transform(lst, rotate):
    if rotate:
        return lst[::-1]
    else:
        return lst