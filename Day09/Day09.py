# https://adventofcode.com/2020/day/9

with open('Input09.txt', 'r') as file:
    input = file.read().splitlines()

numbers = [int(i) for i in input]

# --- Part 1 --- #

def find_addends(numbers, sum):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                return numbers[i], numbers[j]

def find_invalid_sum_number(numbers, offset):
    position = offset
    prev_numbers = numbers[position-offset:position]
    while(position < len(numbers)):
        addends = find_addends(prev_numbers, numbers[position])
        if not addends:
            return numbers[position]
        position+=1
        prev_numbers = numbers[position-offset:position]

invalid_number = find_invalid_sum_number(numbers, 25)
print(invalid_number)

# --- Part 2 --- #

def find_contiguous_addends_2(numbers, sum):
    rev_numbers = numbers[::-1]
    for i in range(len(rev_numbers)):
        current_sum = rev_numbers[i]
        for j in range(i+1, len(rev_numbers)):
            if current_sum > sum:
                break
            current_sum += rev_numbers[j]
            if current_sum == sum:
                return rev_numbers[i:j+1]

contiguous_set = find_contiguous_addends_2(numbers, invalid_number)
print(min(contiguous_set) + max(contiguous_set))



# --- Alternate solution Part 2 --- #

# Alternate solution where you keep moving all the numbers one place to the right to add
# them to the original list, so that after n times on each position it shows the sum of the
# element and n previous ones in the original list.
# Turned out slower.
def find_contiguous_addends_2(numbers, sum):
    offset_numbers = numbers
    sum_numbers = offset_numbers
    num_addends = 2
    while(num_addends <= len(numbers)):
        offset_numbers = [0] + offset_numbers[0:-1]
        sum_numbers = [n + n_prev for n, n_prev in zip(sum_numbers, offset_numbers)]
        try:
            sum_index = sum_numbers.index(sum)
            return numbers[sum_index - num_addends + 1:sum_index]
        except ValueError:
            num_addends += 1

