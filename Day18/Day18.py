# https://adventofcode.com/2020/day/18
import re

with open('Input18.txt', 'r') as file:
    input = file.read().splitlines()

expressions = [line.replace(' ','') for line in input]

# --- Part 1 --- #

class Plus:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def __str__(self):
        return f"{{{self.left}+{self.right}}}"

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def __str__(self):
        return f"{{{self.left}*{self.right}}}"

class Num:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return int(self.num)

    def __str__(self):
        return str(self.num)

def find_closed_parentheses(string, start_pos=0):
    parentheses_stack = []
    for i, char in enumerate(string):
        if char == '(':
            parentheses_stack.append('(')
        elif char == ')':
            parentheses_stack.pop()
        if len(parentheses_stack) == 0:
            return string[1:i], i+1 + start_pos

def evaluate_with_equal_precedence(expression):
    reverse_expression = reverse(expression)
    return parse_expression(reverse_expression).eval()

def reverse(expression):
    rev = expression.replace('(','l').replace(')','r')
    rev = rev.replace('l', ')').replace('r', '(')
    return rev[::-1]

def parse_expression(expression):
    if len(expression) == 1:
        return Num(expression)
    pos = 0
    char = expression[pos]
    # left
    if char == '(':
        left_side, pos = find_closed_parentheses(expression)
        if pos == len(expression):
            return parse_expression(expression[1:-1])
        left_side = parse_expression(left_side)
    else: #number
        left_side = Num(char)
        pos += 1
    symbol = expression[pos]
    # right
    right_side = parse_expression(expression[pos+1:])
    if symbol == '+':
        return Plus(left_side, right_side)
    if symbol == '*':
        return Multiply(left_side, right_side)

answers = [evaluate_with_equal_precedence(expr) for expr in expressions]
print(sum(answers))

# --- Part 2 --- #

def remove_trivial_brackets(expression):
    num_brackets = re.findall(r"\(\d+\)", expression)
    for num_bracket in num_brackets:
        expression = expression.replace(num_bracket, num_bracket[1:-1])
    return expression

def evaluate_with_plus_precedence(expr):
    expr = remove_trivial_brackets(expr)
    if not any(x in expr for x in ['(', '+', '*']):
        return int(expr)
    if not '+' in expr:
        expr = evaluate_and_replace(re.findall(r"\d+\*\d+", expr), expr)
        return evaluate_with_plus_precedence(expr)
    simple_plus_brackets = re.findall(r"\(\d+(?:\+\d+)+\)", expr)
    expr = evaluate_and_replace(simple_plus_brackets, expr)

    simple_mults_brackets = re.findall(r"\(\d+(?:\*\d+)+\)", expr)
    expr = evaluate_and_replace(simple_mults_brackets, expr)

    single_pluses = re.findall(r"\d+\+\d+", expr)
    expr = evaluate_and_replace(single_pluses, expr)

    return evaluate_with_plus_precedence(expr)

def evaluate_and_replace(simples, expression):
    new_expression = expression
    for simple in simples:
        pattern = simple
        for symbol in ['+', '*', '(', ')']:
            pattern = pattern.replace(symbol, "\\" + symbol)
        pattern = '(?<!\d)' + pattern + '(?!\d)'
        new_expression = re.sub(pattern, str(evaluate_simple(simple)), new_expression)
    return new_expression

def evaluate_simple(simple_expr):
    simple_expr = simple_expr.replace('(','').replace(')','')
    symbol = '+' if '+' in simple_expr else '*'
    numbers = [int(n) for n in simple_expr.split(symbol)]
    if symbol == '+':
        return sum(numbers)
    else:
        prod = 1
        for num in numbers:
            prod *= num
        return prod

answers = [evaluate_with_plus_precedence(expr) for expr in expressions]
print(sum(answers))
