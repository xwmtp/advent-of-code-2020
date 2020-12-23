# https://adventofcode.com/2020/day/23

input = '219347865'

class Cups:

    def __init__(self, init_circle, init_cup):
        self.circle = init_circle
        self.total_cups = len(init_circle)
        self.min_cup = min(init_circle)
        self.max_cup = max(init_circle)
        self.current_cup = init_cup

    def play(self, rounds):
        for r in range(rounds):
            if r >0 and r % 1000000 == 0:
                print(f"Move {r}...")
            self.move()
        return self.circle

    def move(self):
        picked_up = self._pick_up_cups()
        destination = self.get_destination_cup(picked_up)
        self._place_cups(picked_up, destination)
        self.current_cup = self.circle[self.current_cup]

    def get_destination_cup(self, picked_up):
        cup = self.current_cup
        while True:
            cup = cup - 1
            if cup < self.min_cup:
                cup = self.max_cup
            if cup not in picked_up:
                return cup

    def _pick_up_cups(self):
        picked_up = []
        cup = self.current_cup
        for i in range(3):
            select_cup = self.circle[cup]
            picked_up.append(select_cup)
            cup = select_cup
        self.circle[self.current_cup] = self.circle[cup]
        return picked_up

    def _place_cups(self, picked_up, destination):
        self.circle[picked_up[-1]] = self.circle[destination]
        self.circle[destination] = picked_up[0]

def cups_to_circle(cups):
    circle = {}
    for i, cup in enumerate(cups[:-1]):
        circle[cup] = cups[i+1]
    circle[cups[-1]] = cups[0]
    return circle

def circle_to_cups(circle, start_cup):
    cups = []
    cup = start_cup
    while True:
        cups.append(cup)
        cup = circle[cup]
        if cup == start_cup:
            break
    return cups

# --- Part 1 --- #

init_cups = [int(c) for c in input]
init_circle = cups_to_circle(init_cups)
game = Cups(init_circle, init_cups[0])
circle = game.play(100)
print(''.join([str(c) for c in circle_to_cups(circle, 1)[1:]]))

# --- Part 2 --- #

init_cups = [int(c) for c in input] + [n for n in range(10, 1000001)]
init_circle = cups_to_circle(init_cups)
game = Cups(init_circle, init_cups[0])
circle = game.play(10000000)

cup_1 = circle[1]
cup_2 = circle[cup_1]
print(cup_1 * cup_2)
