# https://adventofcode.com/2020/day/6

with open('Input06.txt', 'r') as file:
    input = file.read()

groups = [group.split() for group in input.split('\n\n')]

# --- Part 1 --- #

def count_group_union(group):
    return len(set(''.join(group)))

group_counts = [count_group_union(group) for group in groups]
print(sum(group_counts))

# --- Part 2 --- #

def count_group_intersection(group):
    answer_sets = [set(answers) for answers in group]
    return len(set.intersection(*answer_sets))

group_counts = [count_group_intersection(group) for group in groups]
print(sum(group_counts))