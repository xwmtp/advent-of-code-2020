# https://adventofcode.com/2020/day/16

with open('Input16.txt', 'r') as file:
    input = file.read().split('\n\n')

def parse_fields(input):
    fields = {}
    for line in input.splitlines():
        if line == '':
            break
        field =  line.split(':')[0]
        ranges = line.split(':')[1].split('or')
        fields[field] = (range_to_tuple(ranges[0]), range_to_tuple(ranges[1]))
    return fields

def parse_tickets(input):
    tickets = []
    for line in input.splitlines()[1:]:
        tickets.append([int(n) for n in line.split(',')])
    return tickets

def range_to_tuple(range_string):
    nums = range_string.strip().split('-')
    return range(int(nums[0]), int(nums[1]) + 1)

fields = parse_fields(input[0])
my_ticket = parse_tickets(input[1])[0]
nearby_tickets = parse_tickets(input[2])

# --- Part 1 --- #

def number_in_ranges(number, ranges):
    return number in ranges[0] or number in ranges[1]

def valid_number(number, fields):
    return any(number_in_ranges(number, ranges) for ranges in fields.values())

def get_invalid_values(tickets, fields):
    return [number for ticket in tickets for number in ticket if not valid_number(number, fields)]

print(sum(get_invalid_values(nearby_tickets, fields)))

# --- Part 2 --- #

def get_valid_tickets(tickets, fields):
    return [ticket for ticket in tickets if all(valid_number(num, fields) for num in ticket)]

def determined_all_fields(possible_fields):
    return not any(len(col_possible_fields) > 1 for col_possible_fields in possible_fields.values())

def remove_from_sets(value, dict_of_sets):
    for key in dict_of_sets:
        if value in dict_of_sets[key] and len(dict_of_sets[key]) > 1:
            dict_of_sets[key].remove(value)
            if len(dict_of_sets[key]) == 1:
                remove_from_sets(list(dict_of_sets[key])[0], dict_of_sets)

def product(lst):
    result = 1
    for x in lst:
        result = result * x
    return result

def determine_fields(tickets, fields):
    possible_fields = {pos : set(fields.keys()) for pos in range(len(tickets[0]))}
    while(not determined_all_fields(possible_fields)):
        for ticket in tickets:
            for pos, value in enumerate(ticket):
                if len(possible_fields[pos]) < 2:
                    continue
                updated_fields = possible_fields[pos].copy()
                for field in possible_fields[pos]:
                    if not number_in_ranges(value, fields[field]):
                        updated_fields.remove(field)
                possible_fields[pos] = updated_fields
                if len(updated_fields) == 1:
                    remove_from_sets(list(updated_fields)[0], possible_fields)
    return {pos : list(fields)[0] for pos, fields in possible_fields.items()}

valid_tickets = get_valid_tickets(nearby_tickets, fields)
determined_fields = determine_fields(valid_tickets, fields)
departure_values = [my_ticket[pos] for pos, field in determined_fields.items() if 'departure' in field]

print(product(departure_values))
