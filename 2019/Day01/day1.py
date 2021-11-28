import math
import os
import sys

def fuelMassToLift(moduleMass):
    return math.floor((int(moduleMass) / 3) - 2)


def fuelMass(previousFuelmass):
    if previousFuelmass <= 0:
        return 0
    else:
        return previousFuelmass + fuelMass(fuelMassToLift(previousFuelmass))


if __name__ == '__main__':
    part1 = 0
    part2 = 0

    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

        for module in f.readlines():
            fuel = fuelMassToLift(module)
            # Get the total mass of fuel used to send the rocket
            # in orbit.
            part1 += fuel
            
            # Same thing, but including the fuel mass.
            part2 += fuelMass(fuel)

    print("PART 1:", part1)
    print("PART 2:", part2)
