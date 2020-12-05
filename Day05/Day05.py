# https://adventofcode.com/2020/day/5

with open('Input05.txt', 'r') as file:
    boarding_passes = file.read().splitlines()

# --- Part 1 --- #

def get_half(lower, upper, half):
    if half == 'F' or half == 'L':
        return lower, lower + (upper - lower) // 2
    if half == 'B' or half == 'R':
        return lower + (upper - lower) // 2 + 1, upper

def binary_search(init_lower, init_upper, halfs):
    if len(halfs) == 0:
        return
    lower, upper = get_half(init_lower, init_upper, halfs[0])
    for half in halfs[1:]:
        lower, upper = get_half(lower, upper, half)
    return upper

def boarding_pass_to_id(boarding_pass):
    row = binary_search(0, 127, boarding_pass[:7])
    column = binary_search(0, 7, boarding_pass[7:])
    return row * 8 + column

seat_ids = [boarding_pass_to_id(boarding_pass) for boarding_pass in boarding_passes]
print(max(seat_ids))

# --- Part 2 --- #

def find_missing_number(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            return lst[i] - 1

sorted_seats = sorted(seat_ids)
print(find_missing_number(sorted_seats))

