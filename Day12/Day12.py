# https://adventofcode.com/2020/day/12

with open('Input12.txt', 'r') as file:
    actions = file.read().splitlines()

DIRECTIONS = ['N', 'E', 'S', 'W']

# --- Part 1 --- #

class Ferry:

    def __init__(self):
        self.facing = 'E'
        self.x = 0
        self.y = 0

    def navigate(self, instructions):
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            if action in DIRECTIONS:
                self.move(action, value)
            if action == 'F':
                self.move(self.facing, value)
            if action in ['L', 'R']:
                self.turn(action, value)

    def move(self, direction, units):
        if direction == 'N':
            self.y += units
        if direction == 'E':
            self.x += units
        if direction == 'S':
            self.y -= units
        if direction == 'W':
            self.x -= units

    def turn(self, direction, degrees):
        turns = degrees // 90
        current_facing_index = DIRECTIONS.index(self.facing)
        if direction == 'L':
            new_facing_index = (current_facing_index - turns) % 4
        else:
            new_facing_index = (current_facing_index + turns) % 4
        self.facing = DIRECTIONS[new_facing_index]

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)

ferry = Ferry()
ferry.navigate(actions)
print(ferry.manhatten_distance())


# --- Part 2 --- #

class AdvancedFerry:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def navigate(self, instructions):
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            if action in DIRECTIONS:
                self.move_waypoint(action, value)
            if action == 'F':
                self.move(value)
            if action in ['L', 'R']:
                self.turn(action, value)

    def move_waypoint(self, direction, units):
        if direction == 'N':
            self.waypoint_y += units
        if direction == 'E':
            self.waypoint_x += units
        if direction == 'S':
            self.waypoint_y -= units
        if direction == 'W':
            self.waypoint_x -= units

    def move(self, units):
        dx = self.waypoint_x - self.x
        dy = self.waypoint_y - self.y
        self.x += dx * units
        self.y += dy * units
        self.waypoint_x = self.x + dx
        self.waypoint_y = self.y + dy

    def turn(self, direction, degrees):
        turns = degrees // 90
        for _ in range(turns):
            self.turn_once(direction)

    def turn_once(self, direction):
        dx = self.waypoint_x - self.x
        dy = self.waypoint_y - self.y
        if direction == 'L':
            self.waypoint_x = self.x - dy
            self.waypoint_y = self.y + dx
        if direction == 'R':
            self.waypoint_x = self.x + dy
            self.waypoint_y = self.y - dx

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)

    def print_stats(self):
        print(f"ferry {self.x, self.y}, waypoint {self.waypoint_x, self.waypoint_y}")

ferry = AdvancedFerry()
ferry.navigate(actions)
print(ferry.manhatten_distance())
