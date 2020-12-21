# https://adventofcode.com/2020/day/20
from Tile import Tile
import math

with open('Input20.txt', 'r') as file:
    inputs = file.read().split('\n\n')

tiles_inputs = [t.splitlines() for t in inputs]
tiles = [Tile(t_inputs[0], [[c for c in line] for line in t_inputs][1:]) for t_inputs in tiles_inputs]

SQUARE_SIZE = int(math.sqrt(len(tiles)))
TILE_SIZE = len(tiles[0].grid.grid)

# --- Part 1 --- #

def get_tile_border_matches(tile, tiles):
    border_matches = {}
    borders = tile.borders()
    for name, border in borders.items():
        if 'flip' in name:
            continue
        for other_tile in tiles:
            if tile.id == other_tile.id:
                continue
            other_borders = other_tile.borders()
            for other_name, other_border in other_borders.items():
                if other_border == border:
                    if name not in border_matches:
                        border_matches[name] = other_tile.id

    return border_matches

border_matches = {tile.id : get_tile_border_matches(tile, tiles) for tile in tiles}

corner_tiles = [tile for tile in tiles if len(border_matches[tile.id]) == 2]

prod = 1
for id in [tile.id for tile in corner_tiles]:
    prod *= id
print(prod)

# --- Part 2 --- #

def solve_puzzle(start_tile, tiles):
    puzzle_grid = [[start_tile]]
    tile = start_tile
    for y in range(0, SQUARE_SIZE):
        if y > 0:
            puzzle_grid.append([])
        for x in range(0, SQUARE_SIZE):
            orientation = 'right'
            if x == 0:
                if y == 0:
                    continue
                tile = puzzle_grid[y-1][0]
                orientation = 'bottom'
            potentials = potential_matches(tile, tiles, border_matches, puzzle_grid)
            for other_tile in potentials:
                match = fit_together(tile, other_tile, orientation=orientation)
                if match:
                    puzzle_grid[y].append(other_tile)
                    tile = other_tile
                    break
            if not match:
                return print(f'ERROR, no match found y:{y},x:{x}') # should not happen
    return puzzle_grid

def potential_matches(tile, tiles, border_matches, puzzle_grid):
    potentials = [next(t for t in tiles if t.id == id) for id in border_matches[tile.id].values()]
    return [p for p in potentials if not any(p in row for row in puzzle_grid)]

def fit_together(tile, other_tile, orientation):
    for i in range(8):
        flip = i == 4
        if rotate_and_match(tile, other_tile, orientation, flip):
            return True
    return False

def rotate_and_match(tile, other_tile, orientation, flip):
    other_tile.rotate_clockwise(flip=flip)
    tile_border       = tile.right()      if orientation == 'right' else tile.bottom()
    other_tile_border = other_tile.left() if orientation == 'right' else other_tile.top()
    return tile_border == other_tile_border

top_left_tile = next(tile for tile in corner_tiles if 'bottom' in border_matches[tile.id] and 'right' in border_matches[tile.id])
puzzle_grid = solve_puzzle(top_left_tile, tiles)

def create_puzzle_image(puzzle_grid):
    image = []
    for puzzle_row in puzzle_grid:
        for y in range(1, TILE_SIZE-1):
            image.append([])
            for tile in puzzle_row:
                tile_row = tile.transformed_grid.grid[y]
                image[-1] += remove_border(tile_row)
    return Tile('Tile 0:', image)

def remove_border(row):
    return [char for x, char in enumerate(row) if x != 0 and x != TILE_SIZE - 1]

image = create_puzzle_image(puzzle_grid)
IMAGE_SIZE = len(image.grid.grid)

monster_strings = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]
MONSTER_PATTERN = [[c for c in string] for string in monster_strings]

MONSTER_Y = len(MONSTER_PATTERN)
MONSTER_X = len(MONSTER_PATTERN[0])

def match_monster(image, y, x):
    monster_coords = []
    for m_y in range(MONSTER_Y):
        for m_x in range(MONSTER_X):
            if MONSTER_PATTERN[m_y][m_x] == '#':
                #print(y, x, '//', m_y, m_x, '//', y+m_y, x+m_x)
                if image.transformed_grid.get(y + m_y, x + m_x) == '#':
                    monster_coords.append((y+m_y, x+m_x))
                else:
                    return False
    return monster_coords

def find_monster_coords(image):
    for i in range(8):
        flip = i == 4
        image.rotate_clockwise(flip = flip)

        all_monster_coords = []
        for y in range(IMAGE_SIZE-MONSTER_Y):
            for x in range(IMAGE_SIZE-MONSTER_X):
                monster_match = match_monster(image, y, x)
                if monster_match:
                    all_monster_coords += monster_match
        if len(all_monster_coords) > 0:
            return all_monster_coords

all_monster_coords = find_monster_coords(image)
roughness = 0
for y in range(IMAGE_SIZE):
    for x in range(IMAGE_SIZE):
        if image.transformed_grid.get(y, x) == '#' and (y, x) not in all_monster_coords:
            roughness += 1
print(roughness)