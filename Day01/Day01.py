# https://adventofcode.com/2020/day/1

with open('Input01.txt', 'r') as file:
    lines = file.readlines()

expenses = [int(line) for line in lines]

# --- Part 1 --- #

def find_two_expenses_with_sum(expenses, sum):
    for i in range(len(expenses)):
        expense1 = expenses[i]
        for j in range(i, len(expenses)):
            if i == j:
                continue
            expense2 = expenses[j]
            if expense1 + expense2 == sum:
                return expense1 * expense2


found = find_two_expenses_with_sum(expenses, 2020)
print(found)


# --- Part 2 --- #

def find_three_expenses_with_sum(expenses, sum):
    for i in range(len(expenses)):
        expense1 = expenses[i]
        for j in range(len(expenses)):
            expense2 = expenses[j]
            for k in range(len(expenses)):
                expense3 = expenses[k]
                if i == j == k:
                    continue
                if expense1 + expense2 + expense3 == sum:
                    return expense1 * expense2 * expense3

found = find_three_expenses_with_sum(expenses, 2020)
print(found)

