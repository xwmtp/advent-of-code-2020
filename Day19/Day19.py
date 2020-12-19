# https://adventofcode.com/2020/day/19
from copy import deepcopy

with open('Input19.txt', 'r') as file:
    input = file.read().split('\n\n')

rules_input = input[0].splitlines()
messages = input[1].splitlines()

def parse_rules(rule_lines):
    rules = {}
    for line in rule_lines:
        sides = line.split(':')
        left_side = sides[0]
        right_side_str = sides[1]
        if '"' in right_side_str:
            right_side = [right_side_str.strip().replace('"','|')]
        else:
            sub_rules = (right_side_str + ' ').split('|')
            right_side = set(sub_rule.replace(' ','|') for sub_rule in sub_rules)
        rules[left_side] = right_side
    return rules

def is_only_letters(rule):
    return all(no_digits(subrule) for subrule in rule)

def no_digits(string):
    return not any(char.isdigit() for char in string)

# take the rules with just one letter as right-hand and fill them in throughout the dictionary
def fill_in_letters(rules):
    new_rules = deepcopy(rules)
    for id, rule in rules.items():
        if len(rule) == 1 and is_only_letters(rule):
            for n_id, n_rule in new_rules.items():
                new_rule = set()
                for subrule in n_rule:
                    new_rule.add(subrule.replace(f'|{id}|', rule[0]))
                new_rules[n_id] = new_rule
    return new_rules

def get_all_matches(rules, start='0', max_length = None):
    if not max_length:
        max_length = float("inf")
    return [message.replace("|","") for message in _get_all_matches(rules, f"|{start}|", set(), max_length)]

def _get_all_matches(rules, subrule, results, max_length):
    length = len(subrule.replace('|',''))
    if is_only_letters(subrule) and length <= max_length:
        results.add(subrule)
    if length >= max_length:
        return

    for id in subrule[1:-1].split('|'):
        if not no_digits(id):
            for new_substring in rules[id]:
                new_subrule = subrule.replace(f'|{id}|', new_substring, 1)
                _get_all_matches(rules, new_subrule, results, max_length=max_length)
    return results

rules = parse_rules(rules_input)
rules = fill_in_letters(rules)

# rule 0 -> 8 11 -> 42 42 31
matches_rule_42  = get_all_matches(rules, '42')
matches_rule_31  = get_all_matches(rules, '31')

num_valid_messages = 0
for message in messages:
    if message[:8] in matches_rule_42 and message[8:16] in matches_rule_42 and message[16:] in matches_rule_31:
        num_valid_messages += 1
print(num_valid_messages)


# --- Part 2 --- #

MAX_MESSAGE = len(max(messages, key=lambda x: len(x)))
# all matches for rule 42 and 31 have length 8
BLOCK_LENGTH = len(matches_rule_42[0])

# a stands for 42, b stands for 31
new_rules = {
    '0' : ['|8|11|'],
    '8' : ['|a|', '|a|8|'],
    '11' : ['|a|b|' , '|a|11|b|']
}

patterns = get_all_matches(new_rules, '0', max_length=MAX_MESSAGE // BLOCK_LENGTH + 1)

def matches_pattern(message, pattern):
    i = 0
    for char in pattern:
        block = message[i:i + BLOCK_LENGTH]
        if char == 'a':
            results = matches_rule_42
        else:
            results = matches_rule_31
        if block not in results:
            return False
        i += BLOCK_LENGTH
    return True

valid_message_count = 0
for message in messages:
    num_blocks = len(message) // BLOCK_LENGTH
    matching_patterns = [pattern for pattern in patterns if len(pattern) == num_blocks]
    if any(matches_pattern(message, pattern) for pattern in matching_patterns):
        valid_message_count += 1
print(valid_message_count)
