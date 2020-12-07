# https://adventofcode.com/2020/day/7

with open('Input07.txt', 'r') as file:
    raw_rules = file.read().splitlines()

def parse_rule(raw_rule):
    words = raw_rule.split()
    left_side_rule = ' '.join(words[:2])
    right_side = ' '.join(words[4:]).split(',')
    right_side_rules = []
    for rule in right_side:
        rule_words = rule.split()
        if rule_words[0] == 'no':
            right_side_rules.append('-')
        else:
            right_side_rules.append((int(rule_words[0]), ' '.join(rule_words[1:3])))
    return left_side_rule, right_side_rules

rules = dict(parse_rule(raw_rule) for raw_rule in raw_rules)


class Luggage_processing:

    def __init__(self, rules):
        self.rules = rules
        self.target_bag_containers = set()
        self.containing_bags = {}

    def count_target_bag_containers(self, target_bag):
        self.target_bag_containers = set()
        for bag in self.rules:
            if self.contains_bag(bag, target_bag):
                self.target_bag_containers.add(bag)
        return len(self.target_bag_containers)

    def contains_bag(self, starting_bag, target_bag):
        if starting_bag in self.target_bag_containers:
            return True
        for bag in self.rules[starting_bag]:
            if bag == '-':
                return False
            if bag[1] == target_bag:
                return True
            if self.contains_bag(bag[1], target_bag):
                self.target_bag_containers.add(bag[1])
                return True
        return False

    def count_containing_bags(self, target_bag):
        total_count = 0
        if target_bag in self.containing_bags:
            return self.containing_bags[target_bag]
        for bag in self.rules[target_bag]:
            if bag != '-':
                total_count += bag[0] + bag[0] * self.count_containing_bags(bag[1])
        self.containing_bags[target_bag] = total_count
        return total_count


# --- Part 1 --- #
luggage = Luggage_processing(rules)
print(luggage.count_target_bag_containers('shiny gold'))

# --- Part 2 --- #
print(luggage.count_containing_bags('shiny gold'))


