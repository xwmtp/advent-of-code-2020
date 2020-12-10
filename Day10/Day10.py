# https://adventofcode.com/2020/day/10

with open('Input10.txt', 'r') as file:
    input = file.read().splitlines()

portable_adapters = sorted([int(i) for i in input])
adapters = [0] + portable_adapters + [portable_adapters[-1] + 3]

# --- Part 1 --- #

def differences(lst):
    offset_lst = [0] + lst[0:-1]
    return  [n - n_prev for n, n_prev in zip(lst, offset_lst)][1:]

jolt_differences = differences(adapters)
print(jolt_differences.count(1) * jolt_differences.count(3))


# --- Part 2 --- #

def nums_to_str(nums):
    return ''.join([str(n) for n in nums])

# count all possible lists that can result from adding up two adjacent numbers in lst (repeatedly), while never having
# a new element exceed the 'max'.
# wrapper for recursive _contract
def contract_possibilities(nums, max):
    possible_lists=set(nums_to_str(nums))
    return len(_contract(nums, possibile_lsts=possible_lists, max=max))

def _contract(lst, possibile_lsts, max):
    for i in range(len(lst)-1):
        if lst[i] + lst[i+1] <= max:
            new_lst = lst.copy()
            new_lst[i:i+2] = [lst[i] + lst[i+1]]
            list_str = nums_to_str(new_lst)
            possibile_lsts.add(list_str)
            strs = list_str.split(str(max))
            for string in strs:
                _contract([int(c) for c in string], possibile_lsts, max=max)
    return possibile_lsts

def get_adapter_possibilities(jolt_differences):
    to_combine = []
    possibilities = 1
    for diff in jolt_differences:
        if diff < 3:
            to_combine.append(diff)
        else:
            if len(to_combine) > 0:
                possibilities *= contract_possibilities(to_combine, max=3)
            to_combine = []
    return possibilities

print(get_adapter_possibilities(jolt_differences))

