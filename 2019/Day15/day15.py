import os
import sys
import pygame
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode


DIRECTIONS = [1, 4, 2, 3]
Y = [1, 0, -1, 0]
X = [0, 1, 0, -1]

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
                    

if __name__ == "__main__":
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
    

