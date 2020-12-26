# https://adventofcode.com/2020/day/25

with open('Input25.txt', 'r') as file:
    card_key, door_key = [int(line) for line in file.read().splitlines()]

def find_loop_size(public_key, subject_number):
    loop_size = 0
    value = 1
    while value != public_key:
        value *= subject_number
        value = value % 20201227
        loop_size += 1
    return loop_size

card_loop_size = find_loop_size(card_key, 7)
door_loop_size = find_loop_size(door_key, 7)

def get_encryption_key(key, loop_size):
    value = 1
    for i in range(loop_size):
        value *= key
        value = value % 20201227
    return value

print(get_encryption_key(card_key, door_loop_size))
