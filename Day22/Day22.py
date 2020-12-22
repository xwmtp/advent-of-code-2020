# https://adventofcode.com/2020/day/22

with open('Input22.txt', 'r') as file:
    inputs = file.read().split('\n\n')

def calculate_score(deck):
    return sum((i + 1) * card for i, card in enumerate(deck))

class Combat:

    def __init__(self, deck_p1, deck_p2):
        self.deck_p1 = deck_p1.copy()
        self.deck_p2 = deck_p2.copy()
        self.round = 1

    def play_game(self):
        while not self.game_over():
            self.play_round()
        return self.winner()

    def play_round(self):
        card_p1 = self.deck_p1.pop()
        card_p2 = self.deck_p2.pop()
        if card_p1 > card_p2:
            self.deck_p1 = [card_p2, card_p1] + self.deck_p1
        else:
            self.deck_p2 = [card_p1, card_p2] + self.deck_p2
        self.round += 1

    def game_over(self):
        return len(self.deck_p1) == 0 or len(self.deck_p2) == 0

    def winner(self):
        if not self.game_over():
            return
        if len(self.deck_p1) > 0:
            return 'p1', self.deck_p1
        else:
            return 'p2', self.deck_p2

    def __str__(self):
        return f'Round {self.round}\nPlayer 1: {self.deck_p1[::-1]}\nPlayer 2: {self.deck_p2[::-1]}'

deck_p1 = [int(l) for l in inputs[0].splitlines()[1:]][::-1]
deck_p2 = [int(l) for l in inputs[1].splitlines()[1:]][::-1]

game = Combat(deck_p1, deck_p2)
_, winner_deck = game.play_game()
print(calculate_score(winner_deck))


# --- Part 2 --- #

class RecursiveCombat(Combat):
    games_started = 0

    def __init__(self, deck_p1, deck_p2):
        super().__init__(deck_p1, deck_p2)
        self.past_configurations = {}

    def play_game(self):
        RecursiveCombat.games_started += 1
        result = super(RecursiveCombat, self).play_game()
        return result

    def play_round(self):
        sum_p1 = sum(self.deck_p1)
        if sum_p1 not in self.past_configurations:
            self.past_configurations[sum_p1] = []
        self.past_configurations[sum_p1].append((self.deck_p1.copy(), self.deck_p2.copy()))
        card_p1 = self.deck_p1.pop()
        card_p2 = self.deck_p2.pop()
        if (self.play_recurse_game(card_p1, card_p2)):
            recurse_game = RecursiveCombat(self.deck_p1[-card_p1:].copy(), self.deck_p2[-card_p2:].copy())
            winner, winner_deck = recurse_game.play_game()
        else:
            winner = 'p1' if card_p1 > card_p2 else 'p2'
        if winner == 'p1':
            self.deck_p1 = [card_p2, card_p1] + self.deck_p1
        else:
            self.deck_p2 = [card_p1, card_p2] + self.deck_p2
        self.round += 1

    def play_recurse_game(self, card_p1, card_p2):
        return len(self.deck_p1) >= card_p1 and len(self.deck_p2) >= card_p2

    def repeated_configuration(self):
        sum_p1 = sum(self.deck_p1)
        if sum_p1 in self.past_configurations:
            return (self.deck_p1, self.deck_p2) in self.past_configurations[sum_p1]
        return False

    def game_over(self):
        return super().game_over() or self.repeated_configuration()

    def __str__(self):
        return f'Game: {RecursiveCombat.games_started}\n{super().__str__()}'

game = RecursiveCombat(deck_p1, deck_p2)
_, winner_deck = game.play_game()
print(calculate_score(winner_deck))