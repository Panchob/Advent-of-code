from pathlib import Path
import math
file = Path("day05/input.txt")

ROWS = 127
COLUMNS = 7

def upperHalf(range):
    return [range[0] + round((range[1] - range[0])/2), range[1]]

def lowerHalf(range):
    return [range[0], range[0] + round((range[1] - range[0])/2) - 1]

MAPPING = {
    "F":lowerHalf,
    "B":upperHalf,
    "R":upperHalf,
    "L":lowerHalf
}

MAPPING_LAST ={"F":0, "B":1, "R":1, "L":0}

def findSeat(range, partition):
    for p in partition[:-1]:
        range = MAPPING[p](range)

    return range[MAPPING_LAST[partition[-1]]]


def listSeat(partitions):
    ids = []
    for partition in partitions:
        rowPartition, colPartition = partition[:-3], partition[-3:]
        rowRange, colRange = [0, ROWS], [0, COLUMNS]

        row = findSeat(rowRange, rowPartition)
        col = findSeat(colRange, colPartition)

        ids.append(row * 8 + col)

    return ids

def part1(partitions):
    print("Part 1:", max(listSeat(partitions)))

def part2(partitions):
    seats = listSeat(partitions)
    for id in range(min(seats), max(seats)):
        if id not in seats and id + 1 in seats and id - 1 in seats:
            print("Part 2:", id)
            break
    
if __name__ == "__main__":
    f = open(file)
    partitions = list(map(lambda l: l.rstrip(), f.readlines()))
    part1(partitions)
    part2(partitions)