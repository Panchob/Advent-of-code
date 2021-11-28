import os
import sys
from collections import defaultdict
import math


# Components as key and their
# spares production as value.
spares = {}
# Components as key and the number they produce
# for each conversion.
quantities = {}
# Components as key and their recipe as a list for
# a value.
conversions = {}

TRILLION = 1000000000000


def countOres(current, q):

    if q == 0:
        return 0

    q -= checkForSpares(current, q)
    spares[current] += (quantities[current] *
                        math.ceil(q / quantities[current])) - q
    totalOres = 0

    for elem in conversions[current]:
        if elem[1] == "ORE":
            return elem[0] * math.ceil(q / quantities[current])
        else:
            totalOres += countOres(elem[1], math.ceil(
                                   q / quantities[current]) * elem[0])
    return totalOres


# Two conditions for spares.
# 1. I have more spares than the current demanded quantity.
# 2. I have enough spares to reduce the ores comsumption by one iteration
# of the current recipe.
def checkForSpares(current, q):
    r = 0
    # Ex: I Need 7A and have 9 spares.
    if spares[current] > q:
        r = q * (math.floor(spares[current]/q))
    # Ex: I need 21 A and have 2 spares and 10A -> 10 ORES
    # I need to only use 1 spares to use the recipe 2 times instead
    # of 3.
    elif math.ceil((q - spares[current]) / quantities[current]) <\
    math.ceil(q / quantities[current]):
        r = spares[current]

    spares[current] -= r
    return r


def limitedOres(num):
    global spares
    isTrillionUsed = False
    # Increment is initialized at one zero less than the
    # starting one million.
    inc = 100000

    while not isTrillionUsed:
        # Reset the spares dic since its shared between executions.
        spares = spares.fromkeys(spares, 0)
        usedOres = countOres("FUEL", num)
        if usedOres >= TRILLION:
            if inc == 1:
                isTrillionUsed = True
            num -= inc
            inc = int(inc/10)
        else:
            num += inc
    return num


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        conversions = defaultdict(list)
        for line in f.readlines():
            line = line.strip("\n")
            components, result = line.split("=>")
            num, key = result.split(" ")[1:]
            quantities[key] = int(num)
            spares[key] = 0
            components = components.rstrip().split(", ")
            for c in components:
                comp = c.split(" ")
                conversions[key].append((int(comp[0]), comp[1]))
        g = countOres("FUEL", 1)
        print(g)

        # One million seems like a good starting point.
        print(limitedOres(1000000))
