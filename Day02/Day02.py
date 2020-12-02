# https://adventofcode.com/2020/day/2

with open('Input02.txt', 'r') as file:
    lines = file.readlines()


class Password:

    def __init__(self, line):
        split_line = line.split(' ')
        self.policy_number_1 = int(split_line[0].split('-')[0])
        self.policy_number_2 = int(split_line[0].split('-')[1])
        self.letter = split_line[1][:-1]
        self.password = split_line[2]

    def valid_part_1(self):
        occurences = count_occurences(self.letter, self.password)
        return occurences >= self.policy_number_1 and occurences <= self.policy_number_2

    def valid_part_2(self):
        symbol_pos_1 = self.password[self.policy_number_1-1]
        symbol_pos_2 = self.password[self.policy_number_2-1]
        return (symbol_pos_1 == self.letter and symbol_pos_2 != self.letter) or \
               (symbol_pos_1 != self.letter and symbol_pos_2 == self.letter)

def count_occurences(symbol, string):
    count = 0
    for i in range(len(string)):
        if string[i] == symbol:
            count += 1
    return count

# --- Part 1 --- #
passwords = [Password(l) for l in lines]
valid_passwords = [p for p in passwords if p.valid_part_1()]
print(len(valid_passwords))

# --- Part 2 --- #
valid_passwords = [p for p in passwords if p.valid_part_2()]
print(len(valid_passwords))