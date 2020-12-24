# https://adventofcode.com/2020/day/24
from HexGrid import HexGrid

with open('Input24.txt', 'r') as file:
    tiles = file.read().splitlines()

# --- Part 1 --- #

hex = HexGrid()
for tile in tiles:
    hex.flip_tile(tile)
print(hex.count_occurence('.'))

# --- Part 2 --- #

def expanded_range(grid, ax):
    ax_min, ax_max = grid.ax_ranges[ax]
    return range(ax_min - 1, ax_max + 1)

def update_tile(grid, coord):
    black_adjacents = count_black_adjacents(grid, coord)
    if grid.get(*coord) == '.' and black_adjacents not in [1, 2]:
        return 'W'
    if grid.get(*coord) == 'W' and black_adjacents == 2:
        return '.'

def count_black_adjacents(grid, coord):
    black = 0
    adjacent_coords = grid.get_adjacent_coords(*coord)
    for coord in adjacent_coords:
        if grid.get(*coord) == '.':
            black += 1
    return black

def day(grid):
    new_grid = grid.copy()
    for y in expanded_range(grid, 'y'):
        for x in expanded_range(grid, 'x'):
            update = update_tile(grid, (y, x))
            if update:
                new_grid.set(y, x, update)
    return new_grid

for i in range(100):
    hex = day(hex)
print(hex.count_occurence('.'))
