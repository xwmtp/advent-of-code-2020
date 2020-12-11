# https://adventofcode.com/2020/day/11
from Grid import Grid
from copy import copy

with open('Input11.txt', 'r') as file:
    rows = [[c for c in line] for line in file.read().splitlines()]

def run_simulation(grid, consider ='adjacents'):
    while(True):
        grid, updates = step(grid, consider)
        print(f"Grid changes: {updates}")
        #print_grid(grid)
        if updates == 0:
            break
    return grid

def step(grid, consider='adjacents'):
    updates = 0
    new_grid = copy(grid)
    for x in range(grid.size()[1]):
        for y in range(grid.size()[0]):
            if consider == 'adjacents':
                update = update_position_adjacents(grid, y, x)
            else:
                update = update_position_visibles(grid, y, x)
            if update:
                new_grid.set(y, x, update)
                updates += 1
    return new_grid, updates

def update_position_adjacents(grid, y, x):
    occupied_adjacents = count_occupied_adjacents(grid, y, x)
    if grid.get(y, x) == 'L' and occupied_adjacents == 0:
        return '#'
    if grid.get(y, x) == '#' and occupied_adjacents >= 4:
        return 'L'

def update_position_visibles(grid, y, x):
    visible_seats = get_visible_seats(grid, y, x)
    if grid.get(y, x) == 'L' and visible_seats.count('#') == 0:
        return '#'
    if grid.get(y, x) == '#' and visible_seats.count('#') >= 5:
        return 'L'

def count_occupied_adjacents(grid, y, x):
    occupied = 0
    adjacent_coords = grid.get_adjacent_coords(y, x)
    for y, x in adjacent_coords:
        if grid.get(y, x) == '#':
            occupied += 1
    return occupied

def get_visible_seats(grid, y, x):
    found_seats = {}
    for i in range(1, max(grid.size())):
        for sign_y in [-1, 0, 1]:
            for sign_x in [-1, 0, 1]:
                pos_y = y + sign_y * i
                pos_x = x + sign_x * i
                direction_code = f'{sign_y}{sign_x}'
                try:
                    if grid.get(pos_y, pos_x) != '.' and direction_code not in found_seats and direction_code != '00' \
                       and pos_y >= 0 and pos_x >= 0:
                        found_seats[direction_code] = grid.get(pos_y, pos_x)
                except IndexError:
                    pass
                if len(found_seats) == 8:
                    return list(found_seats.values())
    return list(found_seats.values())

# --- Part 1 --- #

grid = Grid(rows)
end_grid = run_simulation(grid, consider='adjacents')
print(end_grid.count_occurence('#'))

# --- Part 2 --- #

end_grid = run_simulation(grid, consider='visible')
print(end_grid.count_occurence('#'))