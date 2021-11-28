import os
import sys


def minDistanceOriginAnd(intersections):
    # Center is (0, 0) so distance is simply x + y.
    distances = [abs(x) + abs(y) for x, y in intersections]
    return min(distances)


def minStepsToReachIntersection(wires):
    intersections = intersectionsBetweenWires(wires)
    steps = []
    for i in intersections:
        # Since everything start at (0,0), the index is
        # the number of steps.
        steps.append(wires[0].index(i) + wires[1].index(i))
    return min(steps)


def intersectionsBetweenWires(wires):
    intersections = set(wires[0]).intersection(wires[1])
    # The center is by definition an intersections so we have 
    # to remove it.
    intersections.remove((0,0))
    return intersections


def getWireFrom(instructions):
    # Also represent the center of the board
    wire = [(0, 0)]
    x, y = (0, 0)
    directions = {
        "U": (0, 1),
        "D":  (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    for instruction in instructions:
        d = instruction[0]
        occurrence = int(instruction[1:])
        incX, incY = directions[d]

        for n in range(occurrence):
            x += incX
            y += incY
            wire.append((x, y))

    return wire


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        instructions = []
        for line in f:
            instructions.append(line.split(","))

        # Map all positions for both wires
        wires = [getWireFrom(i) for i in instructions] 

        # Get all intersections of those wires
        intersections = intersectionsBetweenWires(wires)

        print("Part 1:", minDistanceOriginAnd(intersections))
        print("Part 2:", minStepsToReachIntersection(wires))
