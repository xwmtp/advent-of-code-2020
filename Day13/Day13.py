# https://adventofcode.com/2020/day/13

with open('Input13.txt', 'r') as file:
    input = file.read().splitlines()

earliest_timestamp = int(input[0])
lines = input[1].split(',')

# --- Part 1 --- #

buses = [int(l) for l in lines if l != 'x']

def earliest_depart_after_timestamp(bus, timestamp):
    if timestamp%bus == 0:
        return timestamp
    return timestamp+bus-timestamp%bus

def find_earliest_bus_after_timestamp(buses, timestamp):
    earliest_depart_found = float('inf')
    earliest_bus_found = None
    for bus in buses:
        earliest_bus_depart = earliest_depart_after_timestamp(bus, timestamp)
        if earliest_bus_depart < earliest_depart_found:
            earliest_depart_found = earliest_bus_depart
            earliest_bus_found = bus
    return earliest_bus_found, earliest_depart_found

bus, depart_time = find_earliest_bus_after_timestamp(buses, earliest_timestamp)
print((depart_time - earliest_timestamp) * bus)

# --- Part 2 --- #

# find a, b, and gcd so that a*x + b*x = gcd(a, b)
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (0, 1, b)
    else:
        x, y, gcd = extended_euclidean_algorithm(b % a, a)
        return (int(y-(b//a) * x), int(x), int(gcd))

def product(lst):
    result = 1
    for x in lst:
        result = result * x
    return result

def chinese_remainder_theorem(n_lst, t_lst):
    sum = 0
    N = product(n_lst)
    for n, t in zip(n_lst, t_lst):
        a, b, _ = extended_euclidean_algorithm(n, N/n)
        sum += t*b*N//n
    return sum % N

arrive_remainders = [(bus - lines.index(str(bus))) % bus for bus in buses]
print(chinese_remainder_theorem(buses, arrive_remainders))

