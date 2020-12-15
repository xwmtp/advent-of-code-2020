# https://adventofcode.com/2020/day/15

starting_numbers = [6,19,0,5,7,13,1]

class MemoryGame:

    def __init__(self, starting_numbers):
        self.starting_numbers = starting_numbers
        self.init_game()

    def init_game(self):
        self.previous_number = self.starting_numbers[-1]
        self.turn = len(starting_numbers) + 1
        self.last_spoken = {n: i + 1 for i, n in enumerate(starting_numbers)}

    def next_number(self):
        previous_number = self.previous_number
        if previous_number not in self.last_spoken:
            return self.speak(0)
        age = self.turn - 1 - self.last_spoken[previous_number]
        return self.speak(age)

    def speak(self, number):
        self.last_spoken[self.previous_number] = self.turn - 1
        self.turn += 1
        self.previous_number = number
        return number

    def play_till_turn_n(self, n):
        self.init_game()
        if self.turn >= n:
            return
        while True:
            if self.turn % 1000000 == 0:
                print(f'Turn {self.turn}...')
            num = self.next_number()
            if self.turn == n+1:
                return num

# --- Part 1 --- #

game = MemoryGame(starting_numbers)
print(game.play_till_turn_n(2020))

# --- Part 2 --- #

print(game.play_till_turn_n(30000000))
