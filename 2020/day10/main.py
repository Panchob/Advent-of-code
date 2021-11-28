from pathlib import Path
file = Path("day10/input.txt")

def part1(jolts):
    ones = 0
    threes = 0
    index = 0

    if jolts[0] == 1:
        ones = 1
    else:
        threes = 1

    while index < len(jolts) - 1:
        if jolts[index] + 1 == jolts[index+1]:
            ones += 1
        else:
            threes += 1
        index += 1
    
    print("Part 1: There are {} of 1 and {} difference of 3. Multiplied = {}".format(ones, threes, ones * threes) )


def part2(jolts):
    diffs = [1] * len(jolts) 

    for i in range(1, len(jolts)):
        diff = 0
        for j in range(max(0, i - 3), i):
            if jolts[i] - jolts[j] <= 3:
                diff += diffs[j]
        
        diffs[i] = diff
    
    print("Part 2:", diffs[-1])
        


if __name__ == "__main__":
    f = open(file)
    jolts = [0] + list(map(lambda l: int(l.rstrip()), f.readlines()))
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    part1(jolts)
    part2(jolts)

       

