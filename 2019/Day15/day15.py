import os
import sys
import pygame
from collections import defaultdict
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Intcode.Intcode import Intcode


class World:
    def __init__(self, start):
        self.start = start
        self.destination = None
        self.__visited = []
        self.__filled = []
        self.graph = defaultdict(list)
        self.explored = False
        self.time = 0


    def appendTile(self, current, next):
        if next not in self.graph[current]:
            self.graph[current].append(next)
        if current not in self.graph[next]:
            self.graph[next].append(current)


    def pathToDestination(self, current):
        self.__visited.append(current)

        for tile in self.graph[current]:
            if tile == self.destination:
                print("Part 1:", len(self.__visited))
                break
            elif tile not in self.__visited:
                self.pathToDestination(tile)

        self.__visited.pop()
    

    def fillWithOxygen(self, positions):
        nextToFill = []

        for p in positions:
            self.__filled.append(p)
            for n in self.graph[p]:
                if n not in self.__filled:
                    nextToFill.append(n)

        if len(self.__filled) != len(self.graph.keys()):
            self.time += 1
            self.fillWithOxygen(nextToFill)



class Droid(Intcode):
    def __init__(self, file, start):
        Intcode.__init__(self, file)
        self.__direction = 1
        self.__position = start
    
    
    def move(self):
        self.run(self.__direction)
        directions = {
            1: (0, 1),
            2:  (0, - 1),
            3: (-1, 0),
            4: (1, 0)
        }
        incX, incY = directions[self.__direction]
        x, y = self.__position
        x += incX
        y += incY
        self.__position = (x, y)
    

    def turn(self, instruction):
        directions = [1, 4, 2, 3]
        i = directions.index(self.__direction)
        i = 0 if i + instruction == 0 else (i + instruction) % len(directions)
        self.__direction = directions[i]
    

    def explore(self, world):
        while not world.explored:
            current = self.__position
            self.move()
            status = self.getOutput()[0]

            if self.__position == world.start:
                world.explored = True

            if status == 0:
                # Turn right
                self.__position = current
                self.turn(1)
            else:
                # Turn left
                if status == 2:
                    world.destination = self.__position
                world.appendTile(current, self.__position) 
                self.turn(-1)


if __name__ == "__main__":
    startingPosition = (25, 25)
    droid = Droid("input.txt", startingPosition)
    world = World(startingPosition)
    droid.explore(world)
    world.pathToDestination(startingPosition)
    world.fillWithOxygen([world.destination])

    print(world.time)
    

    




path = []
validPaths = []
visited = []
TILE = 10
        
def turnRight(i):
    i += 1
    if i > 3:
        i = 0
    return i

def turnLeft(i):
    i -= 1
    if i < 0:
        i = 3
    return i

def fillOxygen(oxygens, world):
    nextIteration = []

    while oxygens:
        tile = oxygens.pop()
        x, y = tile
        adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for adjacent in adjacents:
            i, j = adjacent
            if world[(i, j)] == "path" or world[(i, j)] == "empty":
                world[(i, j)] = "oxygen"
                nextIteration.append(adjacent)

    oxygens.extend(nextIteration)
                    







if __name__ == "poop":
    robot = Intcode("input.txt")
    current = (25,25)
    start = (25,25)
    world = {current: "start"}
    path = [start]
    isGoalReached = False
    direction = 0
    time = -1
    oxygens = []

    screen = pygame.display.set_mode([500, 500])
    tiles = {}
    tileTypes = ["empty", "wall", "robot", "start", "path", "oxygen"]
    tileColors = ["white", "black", "blue", "orange", "lightgreen", "lightblue"]
    for i in range(len(tileTypes)):
        tiles[tileTypes[i]] = pygame.Surface((TILE, TILE))
        tiles[tileTypes[i]].fill(pygame.Color(tileColors[i]))

    mapExplored = False
    running = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x, y = current
        x += X[direction]
        y += Y[direction]
        
        if (x, y) == start:
            mapExplored = True

        if not mapExplored:
            result = robot.run(DIRECTIONS[direction])
            if result > 0:
                if (x,y) in world:
                    if not isGoalReached:
                        path.pop()
                else:
                    world[(x,y)] = "empty"
                    if result == 2:
                        print(len(path))
                        world[(x, y)] = "oxygen"
                        oxygens.append((x, y))
                        isGoalReached = True
                    if not isGoalReached:
                        world[(x,y)] = "path"
                        path.append((x, y))

                direction = turnLeft(direction)
                current = (x, y)
            else:
                direction = turnRight(direction)
                world[(x,y)] = "wall"
        else:
            if oxygens:
                time += 1
                fillOxygen(oxygens, world)
            else:
                print(time)
                running = False
            
        # TODO export in a function
        screen.fill(pygame.Color("grey50"))
        for  x, y in world:
            type = world[x, y]
            screen.blit(tiles[type], (x * TILE, y * TILE))
        x,y = current
        screen.blit(tiles["robot"], (x * TILE, y * TILE))


        pygame.display.flip()
        pygame.time.Clock().tick(60)
    

