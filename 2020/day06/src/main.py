from pathlib import Path
file = Path("day06/input.txt")

def part1(groups):
    total = 0
    for group in groups:
        groupAnswers=set()
        for person in group:
            for answer in person:
                groupAnswers.add(answer)
        total += len(groupAnswers)

    print("Part1:", total)

def part2(groups):
    total = 0
    for group in groups:
        groupAnswers={}
        for person in group:
            for answer in person:
                if answer in groupAnswers:
                    groupAnswers[answer] += 1
                else:
                    groupAnswers[answer] = 1
        for value in groupAnswers.values():
            if value == len(group):
                total += 1
    print("Part 2:", total)


if __name__ == "__main__":
    f = open(file)
    groups = []
    temp = f.read().split("\n\n")
    for g in temp:
        groups.append(g.split("\n"))
    
    part1(groups)
    part2(groups)
    