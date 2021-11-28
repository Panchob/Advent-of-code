from pathlib import Path
file = Path("day03/input.txt")

def part1(input):
    pos = 0
    tree = 0
    for i in input:
        if i[pos] == "#" :
            tree += 1
        pos += 3
        if pos + 3 >= len(i):
            pos = pos - len(i)

    print("Part1: ",tree)


def part2(input, slope):
    pos = 0
    tree = 0
    index = 0

    while index < len(input):
        current = input[index]
        if current[pos] == "#" :
            tree += 1
        pos += slope[0]
        if pos + 3 >= len(current):
            pos = pos - len(current)
        index += slope[1]

    return tree


if __name__ == "__main__":
    f = open(file)
    input = list(map(lambda l: l.rstrip(), f.readlines()))
    part1(input)

    slopes = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    total = 1
    for slope in slopes:
        total *= part2(input, slope)
    
    print("Part2:", total)
