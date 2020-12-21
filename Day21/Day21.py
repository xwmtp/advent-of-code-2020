# https://adventofcode.com/2020/day/21

with open('Input21.txt', 'r') as file:
    lines = file.read().splitlines()

def parse_input(lines):
    foods = []
    for id, line in enumerate(lines):
        ingredients_str, allergens_str = line[:-1].split(' (contains ')
        ingredients = ingredients_str.split()
        allergens = allergens_str.split(', ')
        foods.append(Food(ingredients, allergens, id))
    return foods

class Food:

    def __init__(self, ingredients, allergens, id):
        self.ingredients = ingredients
        self.allergens = allergens
        self.id = id

    def __str__(self):
        return f"{self.id} : {' '.join(self.allergens)} | {' '.join(self.ingredients)}"

    def contains(self, ingredient):
        return ingredient in self.ingredients

    def has_allergen(self, allergen):
        return allergen in self.allergens

    def set_ingredients(self, new_ingredients):
        self.ingredients = new_ingredients

FOODS = parse_input(lines)

unique_allergens = set([allergen for food in FOODS for allergen in food.allergens])
unique_ingredients = set([ingredient for food in FOODS for ingredient in food.ingredients])

ingredient_counts = {}
for ingredient in unique_ingredients:
    count = 0
    for food in FOODS:
        if ingredient in food.ingredients:
            count += 1
    ingredient_counts[ingredient] = count

sorted_ingredients = [ingr[0] for ingr in sorted(ingredient_counts.items(), key=lambda c: c[1])]

cant_contain = {}
for ingredient in sorted_ingredients:
    cant_contain[ingredient] = set()
    for allergen in unique_allergens:
        for food in FOODS:
            if not food.contains(ingredient) and food.has_allergen(allergen):
                cant_contain[ingredient].add(allergen)

safe_ingredients = [ingr for ingr, allergens in cant_contain.items() if len(allergens) == len(unique_allergens)]
safe_ingredient_appearances = sum([food.contains(ingr) for ingr in safe_ingredients for food in FOODS])
print(safe_ingredient_appearances)

# --- Part 2 --- #

def update_foods(safe_ingredients):
    for food in FOODS:
        new_ingredients = [ingr for ingr in food.ingredients if ingr not in safe_ingredients]
        food.set_ingredients(new_ingredients)

def remove_from_entries(elem, dct):
    for key in dct:
        if len(dct[key]) > 1 and elem in dct[key]:
            dct[key].remove(elem)

def determine_allergens(can_contain):
    while any(len(allergens) > 1 for allergens in can_contain.values()):
        for ingredient in allergen_ingredients:
            if len(can_contain[ingredient]) == 1:
                remove_from_entries(can_contain[ingredient][0], can_contain)

# remove safe ingredients from FOODS
update_foods(safe_ingredients)

allergen_ingredients = [ingredient for ingredient, allergens in cant_contain.items() if len(allergens) < len(unique_allergens)]
can_contain = {ingr : [a for a in unique_allergens if a not in cant_contain[ingr]] for ingr in allergen_ingredients}
determine_allergens(can_contain)

sorted_dangerous_ingredients = [ingr[0] for ingr in sorted(can_contain.items(), key=lambda c: c[1][0])]
print(','.join(sorted_dangerous_ingredients))
