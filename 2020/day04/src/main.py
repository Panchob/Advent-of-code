import re
from pathlib import Path
file = Path("day04/input.txt")

FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def birth(year):
    return len(year) == 4 and int(year) >= 1920 and int(year) <= 2002

def issue(year):
    return len(year) == 4 and int(year) >= 2010 and int(year) <= 2020

def expiration(year):
    return len(year) == 4 and int(year) >= 2020 and int(year) <=2030

def height(value):
    h, m = value[:-2], value[-2:]
    if m == "cm":
        return int(h) >= 150 and int(h) <= 193
    elif m == 'in':
        return int(h) >= 59 and int(h) <= 76
    else:
        return False

def hair(color):
    h, v = color[0], color[1:]
    return h == "#" and len(v) == 6 and bool(re.match('[0-9]|[a-f]', v))

def eye(color):
    return color in EYE_COLORS

def passport(id):
    return len(id) == 9 and id.isnumeric()

VALIDATIONS = {
    "byr":birth,
    "iyr":issue,
    "eyr":expiration,
    "hgt":height,
    "hcl":hair,
    "ecl":eye,
    "pid":passport
}

def part1(passports):
    valid = 0
    for passport in passports:
        fieldSet = set()
        for field in passport:
            key, _ = field.split(":")
            if key != "cid":
                fieldSet.add(key)
        if fieldSet == FIELDS:
            valid += 1

    print("Part1:", valid)

def part2(passports):
    valid = 0
    for passport in passports:
        fieldSet = set()
        for field in passport:
            key, value = field.split(":")
            if key != "cid":
                if VALIDATIONS[key](value):
                    fieldSet.add(key)
                else:
                    break
        if fieldSet == FIELDS:
            valid += 1

    print("Part2:", valid)

if __name__ == "__main__":
    f = open(file)
    passports = []
    paragraphs = f.read().split("\n\n")
    for p in paragraphs:
        lines = p.split("\n")
        passport = []
        for line in lines:
            passport += line.split(" ")
        
        passports.append(passport)

    part1(passports)
    part2(passports)