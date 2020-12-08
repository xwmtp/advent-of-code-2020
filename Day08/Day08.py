# https://adventofcode.com/2020/day/8

with open('Input08.txt', 'r') as file:
    input = file.read().splitlines()

instructions = [(instr.split()[0], int(instr.split()[1])) for instr in input]

class Machine:

    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.position = 0
        self.past_positions = set()

    def run(self):
        self.reset()
        while(True):
            instr, arg = self.instructions[self.position]
            if instr == 'acc':
                self.accumulate(arg)
            if instr == 'jmp':
                self.jump(arg)
            if instr == 'nop':
                self.no_operation()
            if self.repeat_instruction():
                return self.accumulator, False
            if self.terminate():
                return self.accumulator, True

    def accumulate(self, acc):
        self.accumulator += acc
        self.update_position(1)

    def jump(self, jmp):
        self.update_position(jmp)

    def no_operation(self):
        self.update_position(1)

    def update_position(self, offset):
        self.past_positions.add(self.position)
        self.position += offset

    def reset(self):
        self.accumulator = 0
        self.past_positions = set()

    def repeat_instruction(self):
        return self.position in self.past_positions

    def terminate(self):
        return self.position == len(instructions)


# --- Part 1 --- #

machine = Machine(instructions)
accumulator, terminated = machine.run()
print(accumulator)

# --- Part 2 --- #

def fix_instructions(instrs):
    for i in range(len(instrs)):
        if instrs[i][0] != 'acc':
            new_instrs = instrs.copy()
            new_instr = 'jmp' if instrs[i][0] == 'nop' else 'nop'
            new_instrs[i] = (new_instr, instrs[i][1])
            accumulator, terminated = Machine(new_instrs).run()
            if terminated:
                return accumulator

print(fix_instructions(instructions))
