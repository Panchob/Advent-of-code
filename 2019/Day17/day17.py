import os
import sys
from collections import defaultdict
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Intcode.Intcode import Intcode

class Graph():
    def __init__(self, height):
        self.__height = height
        self.nodes = defaultdict(list)
        self.alignment = 0


    def calibrate(self):
        for node, adjacents in self.nodes.items():
            if len(adjacents) == 4:
                x, y = node
                self.alignment += (self.__height - y) * x


    def listAdjacents(self, node):
        x, y = node
        adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for a in adjacents:
            if a in self.nodes.keys():
                self.nodes[node].append(a)


if __name__ == "__main__":
    intcode = Intcode("input.txt")
    intcode.run()
    out = intcode.getOutput()


    length = 1
    with open(os.path.join(sys.path[0], "output.txt"), "w") as w:
        for n in out:
            if n == 10:
                length += 1
            w.write(chr(n))
    
    graph = Graph(length)
    with open(os.path.join(sys.path[0], "output.txt"), "r") as r:
        x, y = (0, length)
        for line in r.readlines():
            y -= 1
            x = 0
            for c in line:
                x += 1
                if c == "#":
                    graph.nodes[(x, y)] = []

    for node in graph.nodes.keys():
        graph.listAdjacents(node)

    graph.calibrate()
    print(graph.alignment)

    A = [ord(c) for c in "L,12,L,10,R,8,L,12\n"]
    B = [ord(c) for c in"R,8,R,10,R,12\n"]
    C = [ord(c) for c in "L,10,R,12,R,8\n"]
    mainRoutine = [ord(c) for c in "A,B,A,B,C,C,B,A,B,C\n"]

    intcode = Intcode("input_part2.txt")
    intcode.run()
    out = intcode.getOutput(ascii=True)[-6:-1]
    print("".join(out), mainRoutine)

    for i in mainRoutine:
        intcode.run(i)
    
    out = intcode.getOutput(ascii=True)
    print("".join(out), A)
    for i in A:
        intcode.run(i)

    out = intcode.getOutput(ascii=True)
    print("".join(out), B)
    for i in B:
        intcode.run(i)
    
    out = intcode.getOutput(ascii=True)
    print("".join(out), C)
    for i in C:
        intcode.run(i)
    

    out = intcode.getOutput(ascii=True)
    print("".join(out), "n")
    intcode.run(ord("n"))
    intcode.run(10)
    out = intcode.getOutput(ascii=True)
    print("".join(out))
        





