# https://adventofcode.com/2020/day/3

with open('Input03.txt', 'r') as file:
    map = file.read().splitlines()

def count_trees(map, slope_x, slope_y):
    x = 0
    y = 0
    trees = 0
    while y < len(map) - slope_y:
        x += slope_x
        y += slope_y
        if map[y][x % len(map[0])] == '#':
            trees += 1
    return trees

# --- Part 1 --- #

print(count_trees(map, 3, 1))

# --- Part 2 --- #

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = 1
for slope in slopes:
    trees = count_trees(map, slope[0], slope[1])
    total_trees *= trees
print(total_trees)
