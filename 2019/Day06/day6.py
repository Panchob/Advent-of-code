import os
import sys
from collections import defaultdict


class Space:
    def __init__(self, objects):
        self.__objects = objects
        self.__visited = []


    def totalOrbits(self, current, depth=0):
        total = depth
        self.__visited.append(current)

        for object in self.__objects[current]:
            if object not in self.__visited:
                total += self.totalOrbits(object, depth + 1)
        
        return total


    def pathBetween(self, current, destination):
        self.__visited.append(current)

        for object in self.__objects[current]:
            if object == destination:
                print("Minimal orbital transfer:", len(self.__visited))
                break
            elif object not in self.__visited:
                self.pathBetween(object, destination)

        self.__visited.pop()
    
    
    def emptyVisited(self):
        self.__visited = []


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        objects = defaultdict(list)

        for line in f:
            line = line.rstrip('\n')
            name, orbit = line.split(")")
            objects[name].append(orbit)
            objects[orbit].append(name)

    space = Space(objects)
    print("Total number of orbits:", space.totalOrbits('COM'))
    space.emptyVisited()
    # We want a path between what YOU and SAN are orbiting,
    # not YOU and SAN directly
    space.pathBetween(objects["YOU"][0], objects["SAN"][0])
