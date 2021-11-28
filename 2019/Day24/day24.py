import sys
import os
import math

class Eris():
    def __init__(self, graph):
        self.__graph = graph
        self.__nextGraph = {}
        self.__ratings = []

    def updateGraph(self):
        nextGraph = {}
        
        for k, v in self.__graph.items():
            x, y, z = k
            adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            count = 0
            for a in adjacents:
                if a in self.__graph.keys():
                    if self.__graph[a] == "#":
                        count += 1
            if v == "#" and count != 1:
                nextGraph[k] = "."
            elif v == "." and (count == 1 or count == 2):
                nextGraph[k] = "#"
            else:
                nextGraph[k] = v
        
        self.__graph = nextGraph

    @staticmethod
    def getMiddleAdjacents(pos):
        x, y, z = pos
        position = (x, y)
        adjacents = []

        if position == (1,2):
             adjacents = [(0,0,z),(0,1,z),(0,2,z),(0,3,z),(0,4,z)]
        elif position == (2,1):
            adjacents = [(0,0,z),(1,0,z),(2,0,z),(3,0,z),(4,0,z)]
        elif position == (2,3):
            adjacents = [(0,4,z),(1,4,z),(2,4,z),(3,4,z),(4,4,z)]
        elif position == (3,2):
            adjacents = [(4,0,z),(4,1,z),(4,2,z),(4,3,z),(4,4,z)]
        return adjacents     




    def updateGraphWithDepth(self):
        middleSection = [(2, 1), (3, 2), (1, 2), (2,3)]
        self.__nextGraph = {}
        
        for k, v in self.__graph.items():
            x, y, z = k
            count = 0
            adjacents = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z)]
            
            if v == "#":
                if (x == 0 or x == 4 or y == 0 or y == 4):
                    if (x, y, z - 1) not in self.__nextGraph.keys() and (x, y, z - 1) not in self.__graph.keys():
                        self.createLayer((x, y, z - 1))
                        self.updateOuterLayer(z - 1)
                        
                elif (x, y) in middleSection:
                    if (x, y, z + 1) not in self.__nextGraph.keys() and (x, y, z + 1) not in self.__graph.keys():
                        self.createLayer((x, y, z + 1))
                        self.updateInnerLayer(z + 1)

            if x == 0:
                adjacents.append((1, 2, z - 1))
            if x == 4:
                adjacents.append((3, 2, z - 1))
            if y == 0:
                adjacents.append((2, 1, z - 1))
            if y == 4:
                adjacents.append((2, 3, z - 1))
            if (x,y) in middleSection:
                adjacents.extend(self.getMiddleAdjacents((x,y,z+1)))
            
            for a in adjacents:
                if a in self.__graph.keys():
                    if self.__graph[a] == "#":
                        count += 1
            if v == "#" and count != 1:
                self.__nextGraph[k] = "."
            elif v == "." and (count == 1 or count == 2):
                self.__nextGraph[k] = "#"
            else:
                self.__nextGraph[k] = v
        self.__graph = self.__nextGraph
                


    def createLayer(self, position):
        x, y, z = position
        for j in range(5):
            for i in range(5):
                if (i, j) == (2, 2):
                   self.__nextGraph[(i, j, z)]  = "?"
                else:
                    self.__nextGraph[(i, j, z)]  = "."
    

    def updateInnerLayer(self, z):
        middleSection = [(2, 1), (3, 2), (1, 2), (2,3)]

        for x,y in  middleSection:
            if self.__graph[x, y, z - 1] == "#":
                adjacents = self.getMiddleAdjacents((x, y, z))
                for a in adjacents:
                    self.__nextGraph[a] = "#"

    def updateOuterLayer(self, z):
        totals = [0, 0, 0, 0]
        middleSection = [(1, 2, z), (3, 2, z), (2, 1, z), (2, 3, z)]
        for k, v in self.__graph.items():
            x, y, bz = k
            if bz == z + 1:
                if v == "#":
                    if x == 0 and z == z - 1:
                        totals[0] += 1
                    if x == 4:
                        totals[1] += 1
                    if y == 0:
                        totals[2] += 1
                    if y == 4:
                        totals[3] += 1
        i = 0
        for p in middleSection:
            if totals[i] == 1 or totals[i] == 2:
                self.__nextGraph[p] = "#"
            i += 1



    def finFirstReapeatingLayer(self):
        found = False
        self.__ratings.append(self.bioRating())
        while not found:
            self.updateGraph()
            rating = self.bioRating()
            if rating in self.__ratings:
                found = True
                print(rating)
            else:
                self.__ratings.append(rating)



    def bioRating(self):
        rating = 0
        for k, v in self.__graph.items():
            if v == "#":
                rating += math.pow(2, k[0] + 5*k[1])
        return rating

    def countBugs(self):
        total = 0
        for v in self.__graph.values():
            if v == "#":
                total += 1
        return total

if __name__ == "__main__":
    graph = {}
    x,y = (0,0)
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f.readlines():
            for c in line.rstrip("\n"):
                if (x, y) == (2, 2):
                    graph[x,y,0] = "?"
                else:
                    graph[(x,y,0)] = c
                x += 1
            x = 0
            y += 1
    
    eris = Eris(graph)
    #eris.finFirstReapeatingLayer()
    for _ in range(200):
        eris.updateGraphWithDepth()
    
    print(eris.countBugs())
