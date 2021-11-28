from pathlib import Path
file = Path("day07/input.txt")

relations={}

def parseColor(text):
    return "".join(text.split(" ")[:-1])

def findShiny(current):
    if len(relations[current]) == 0:
        return 0

    found = 0
    for bag in relations[current]:
        if bag["color"] == "shinygold":
           found += 1 
        else:
           found += findShiny(bag["color"])

    return found


def contain(current):
    if len(relations[current]) == 0:
        return 1

    total = 1
    for bag in relations[current]:
        total += bag["quantity"] * contain(bag["color"])

    return total

def part1():
    total = 0
    for bag in relations.keys():
        if findShiny(bag) > 0:
            total += 1

    print("Part 1:", total)

def part2():
    print("Part 2:", contain("shinygold") - 1)


if __name__ == "__main__":
    f = open(file)

    for line in f.readlines():
        parent, children = line.split("contain")
        key = parseColor(parent.rstrip())
        value = []

        for c in children.split(","):
            number, color = c.strip().split(' ', 1)

            if number != "no" :
                value.append ({
                    "quantity": int(number),
                    "color": parseColor(color)
                })

        relations[key] = value

    part1()
    part2()