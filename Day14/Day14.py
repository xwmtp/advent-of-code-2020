# https://adventofcode.com/2020/day/14

with open('Input14.txt', 'r') as file:
    input = file.read().splitlines()

def parse_input(input):
    program = []
    for line in input:
        words = line.split()
        if words[0] == 'mask':
            program.append(('mask', words[2]))
        else:
            mem_slot = int(words[0].replace('mem[', '').replace(']', ''))
            program.append((mem_slot, int(words[2])))
    return program

def num_to_bits36(num):
    binary = bin(num)[2:]
    return ['0'] * (36 - len(binary)) + [b for b in binary]

def bits36_to_num(bits):
    return int(''.join(bits), 2)

# --- Part 1 --- #

def apply_mask_v1(bits, mask):
    masked_bits = bits.copy()
    for i, m in enumerate(mask):
        if m != 'X':
            masked_bits[i] = m
    return masked_bits

def decoder_v1(program):
    mask = 'X' * 36
    memory = {}
    for instruction in program:
        if instruction[0] == 'mask':
            mask = instruction[1]
        else:
            mem_slot, value = instruction
            bits = num_to_bits36(value)
            masked_bits = apply_mask_v1(bits, mask)
            memory[mem_slot] = bits36_to_num(masked_bits)
    return memory

program = parse_input(input)
memory = decoder_v1(program)
print(sum(memory.values()))

# --- Part 2 --- #

def apply_mask_v2(bits, mask):
    num = 0
    floating_nums = []
    for i, m in enumerate(mask):
        if m == '1' or (m == '0' and bits[i] == '1'):
            num += 2**(36-i-1)
        if m == 'X':
            floating_nums.append(2**(36-i-1))
    return calculate_mem_slots(num, floating_nums)

def calculate_mem_slots(starting_num, floating_nums):
    mem_slots = [starting_num]
    for num in floating_nums:
        new_mem_slots = []
        for slot in mem_slots:
            new_mem_slots.append(slot + num)
        mem_slots += new_mem_slots
    return mem_slots

def decoder_v2(program):
    mask = 'X' * 36
    memory = {}
    for instruction in program:
        if instruction[0] == 'mask':
            mask = instruction[1]
        else:
            mem_slot, value = instruction
            mem_slots_to_update = apply_mask_v2(num_to_bits36(mem_slot), mask)
            for slot in mem_slots_to_update:
                memory[slot] = value
    return memory

memory = decoder_v2(program)
print(sum(memory.values()))
