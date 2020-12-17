# https://adventofcode.com/2020/day/17
from Grid3D import Grid3D
from Grid4D import Grid4D

with open('Input17.txt', 'r') as file:
    input = file.read().splitlines()

def expanded_range(grid, ax):
    ax_min, ax_max = grid.ax_ranges[ax]
    return range(ax_min - 1, ax_max + 1)

def update_cube(grid, coord):
    active_adjacents = count_active_adjacents(grid, coord)
    if grid.get(*coord) == '#' and active_adjacents not in [2, 3]:
        return '.'
    if grid.get(*coord) and active_adjacents == 3:
        return '#'

def count_active_adjacents(grid, coord):
    active = 0
    adjacent_coords = grid.get_adjacent_coords(*coord)
    for coord in adjacent_coords:
        if grid.get(*coord) == '#':
            active += 1
    return active

# --- Part 1 --- #

def cycle3D(grid):
    new_grid = grid.copy()
    for z in expanded_range(grid, 'z'):
        for y in expanded_range(grid, 'y'):
            for x in expanded_range(grid, 'x'):
                update = update_cube(grid, (z, y, x))
                if update:
                    new_grid.set(z, y, x, update)
    return new_grid

grid = Grid3D(input)
for i in range(6):
    grid = cycle3D(grid)
    print(f'After {i+1} cycle(s):')
    print(grid)
print(grid.count_occurence('#'))

# --- Part 2 --- #

def cycle4D(grid):
    new_grid = grid.copy()
    for w in expanded_range(grid, 'w'):
        for z in expanded_range(grid, 'z'):
            for y in expanded_range(grid, 'y'):
                for x in expanded_range(grid, 'x'):
                    update = update_cube(grid, (w, z, y, x))
                    if update:
                        new_grid.set(w, z, y, x, update)
    return new_grid

grid = Grid4D(input)
for i in range(6):
    grid = cycle4D(grid)
    print(f'After {i+1} cycle(s):')
    print(grid)
print(grid.count_occurence('#'))