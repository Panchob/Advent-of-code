import sys
import os
import math
import networkx as nx
from collections import defaultdict

class Maze():

    def __init__(self, graph):
        self.__graph = graph
        self.__G = nx.Graph()
        self.__portals = defaultdict(list)
        self.smallestPath = math.inf
        self.__visited = []

    def addAdjacents(self):
        for k in self.__G.nodes():
            x, y = k
            g = self.__graph
            adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            portalName = ""
            for a in adjacents:
                if a in g.keys():
                    if g[a] == ".":
                        self.__G.add_edge(k, a)
                    elif g[a].isalpha():
                        if a == adjacents[0]:
                            portalName = g[a] = g[a] + g[(x + 2, y)]
                        elif a == adjacents[1]:
                            portalName = g[a] = g[(x - 2, y)] + g[a]
                        elif a == adjacents[2]:
                            portalName = g[a] = g[a] + g[(x, y + 2)]
                        else:
                            portalName = g[a] =  g[(x, y - 2)] + g[a]
                        
                        self.__portals[portalName].append(k)

        for p in self.__portals.values():
            if len(p) == 2:
                self.__G.add_edge(p[0], p[1])

    def getStart(self):
        return self.__portals["AA"][0]

    def getDestination(self):
       return self.__portals["ZZ"][0]

    def pathBetween(self):
        return nx.shortest_path(self.__G, self.getStart(), self.getDestination())

    def listNodes(self):
        for k, v in self.__graph.items():
            if v == ".":
                self.__G.add_node(k)

    


if __name__ == "__main__":
    parsedFile = {}
    x,y = (0,0)
    G = nx.Graph()
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f.readlines():
            x = 0
            for c in line.rstrip("\n"):
                parsedFile[x,y] =  c
                x += 1
            y += 1

        maze = Maze(parsedFile)
        maze.listNodes()
        maze.addAdjacents()
        print(len(maze.pathBetween())-1)
