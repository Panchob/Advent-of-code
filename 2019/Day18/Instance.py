from itertools import combinations
from itertools import permutations

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (1, 0)
DOWN = (-1, 0)

class Instance():
    def __init__(self, graph):
        self.__graph = graph[:]
        self.__position = self.getCurrentPosition()
        self.__nbSteps = 0
        self.__foundNextToken = False
        self.__positions = {}
        # Everything that "@" has access to.
        self.__tokens = []
        self.__keys = []

    def position(self):
        return self.__position


    def getValue(self, position):
        x, y = position
        return self.__graph[x][y]
    

    def getPostionFromValue(self, value):
        return self.__positions[value]


    def setValueAt(self, position, value):
        x, y = position
        self.__graph[x][y] = value


    def setCurrentPosition(self, position):
        self.setValueAt(self.__position, ".")
        self.setValueAt(position, "@")
        self.__position = position


    def toggleFound(self):
        self.__foundNextToken = not self.__foundNextToken
    

    def addSteps(self, steps):
        self.__nbSteps += steps


    def nbSteps(self):
        return self.__nbSteps


    def updateTokens(self):
        self.__tokens = self.listAvailableElementsFromPosition(self.__position)

    
    def keyFound(self, keys):
        self.__keys.extend(keys)


    def keys(self):
        return self.__keys
    
    def listPositions(self):
        x = 0
        y = 0

        for line in self.__graph:
            for c in line:
                if c.isalpha():
                    self.__positions[c] = (x, y)
                y += 1
            x +=1
            y = 0

    def listAvailableElementsFromPosition(self, position, direction=None):
        x,y = position
        keysAndDoors = []
        current = self.getValue(position)

        if current != '#':
            if current.isalpha():
                keysAndDoors.append(current)
                if current.isupper():
                    # Consider close doors as wall. (duh)
                    return keysAndDoors

            for d in getDirectionsWithoutBacktracking(direction):
                res = self.listAvailableElementsFromPosition((x + d[0], y + d[1]), d)
                if res:
                    keysAndDoors.extend(res)

        return keysAndDoors

    def nbStepTo(self, goal, position, direction=None, steps=0):

        if self.__foundNextToken:
            return 0

        current = self.getValue(position)
        res = 0

        if current != '#':
            if current == goal:
                self.__foundNextToken = True
                self.setCurrentPosition(position)
                return steps

            x, y = position
            for d in getDirectionsWithoutBacktracking(direction):
                res += self.nbStepTo(goal, (x + d[0], y + d[1]), d, steps + 1)
        
        return res


    def generateAllPossiblePath(self):
        paths = []
        keysC =[]
        keys = list(filter(lambda c: c.islower(), self.__tokens))
        keysC.extend(keys[:])
        doors = list(filter(lambda c: c.isupper(), self.__tokens))

        if len(keys) > 2:
            for i in range(2, len(keys)):
                comb = list(combinations(keys[:], i))
                for j in comb:
                    s = ''.join(j) 
                    keysC.append(s)
            per = list(permutations(keys[:]))
            for j in per:
                s = ''.join(j)
                keysC.append(s)
        elif len(keys) == 2:
            s = ''.join(keys)
            keysC.append(s)

        if not keysC:
            for door in doors:
                paths.append(door)
                
        for k in keysC:
            for door in doors:
                if door.lower() in k or door.lower() in self.__keys:
                    paths.append(k + door)
        
        if not paths:
            paths = keysC
        
        return paths
                

    def getCurrentPosition(self):   
            for x in range(1, len(self.__graph) - 1):
                for y in range(1, len(self.__graph[0]) - 1):
                    if self.getValue((x,y)) == '@':
                        return (x, y)
        

def getDirectionsWithoutBacktracking(lastDirection):
    directions = [RIGHT, LEFT, UP, DOWN]

    if lastDirection == RIGHT:
        directions.pop(1)
    elif lastDirection == LEFT:
        directions.pop(0)
    elif lastDirection == UP:
        directions.pop(3)
    elif lastDirection == DOWN:
        directions.pop(2)

    return directions