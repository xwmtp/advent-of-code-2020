# https://adventofcode.com/2020/day/4

with open('Input04.txt', 'r') as file:
    input = file.read()

raw_passports = input.split('\n\n')
passports = [dict(field.split(':') for field in raw_passport.split()) for raw_passport in raw_passports]

# --- Part 1 --- #

def is_valid_part_1(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    return True

valid_passports = [passport for passport in passports if is_valid_part_1(passport)]
print(len(valid_passports))

# --- Part 2 --- #

def is_valid_part_2(pp):
    try:
        return verify_birth_year(pp['byr']) and verify_issue_year(pp['iyr']) and verify_exp_year(pp['eyr']) and \
               verify_height(pp['hgt']) and verify_hair_color(pp['hcl']) and verify_eye_color(pp['ecl']) and \
               verify_passport_id(pp['pid'])
    except (KeyError, ValueError):
        return False

def verify_birth_year(byr):
    return int(byr) >= 1920 and int(byr) <= 2002

def verify_issue_year(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020

def verify_exp_year(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030

def verify_height(hgt):
    unit = hgt[-2:]
    hgt = int(hgt[:-2])
    if unit == 'cm':
        return hgt >= 150 and hgt <= 193
    elif unit == 'in':
        return hgt >= 59 and hgt <= 76
    else:
        return False

def verify_hair_color(hcl):
    has_hash = hcl[0] == '#'
    length_7 = len(hcl) == 7
    valid_chars = all([char.isdigit() or char in ['a', 'b', 'c', 'd', 'e', 'f'] for char in hcl[1:]])
    return has_hash and length_7 and valid_chars

def verify_eye_color(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def verify_passport_id(pid):
    return len(pid) == 9 and pid.isdigit()


valid_passports = [p for p in passports if is_valid_part_2(p)]
print(len(valid_passports))
