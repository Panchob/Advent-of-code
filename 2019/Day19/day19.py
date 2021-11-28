import os
import sys
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Intcode.Intcode import Intcode


class Drone(Intcode):
    def __init__(self, file, gridSize):
        Intcode.__init__(self, file)
        self.__gridSize = gridSize

    def nbOfAffectedPoints(self):
        total = 0
        for y in range(self.__gridSize):
            for x in range(self.__gridSize):
                self.run(x)
                self.run(y)
                total += self.getOutput()[0]
                self.reset()

        return total

    def displayBeam(self):
        with open(os.path.join(sys.path[0], "output.txt"), "w") as w:
            for y in range(500):
                for x in range(300):
                    self.run(x)
                    self.run(y)
                    out = self.getOutput()[0]
                    if out == 1:
                        p = "#"
                    else:
                        p = "."
                    w.write(p)
                    self.reset()
                w.write("\n")
    
    def findSquare(self):
        found = False
        row = 0

        x, y = (0, 760)
        while not found:
            self.run(x)
            self.run(y)
            out = self.getOutput()[0]
            if out == 1:
                seqX = 1
                pos = (x,y)

                while True:
                    x += 1
                    self.reset()
                    self.run(x)
                    self.run(y)
                    out = self.getOutput()[0]
                    if out == 1:
                        seqX += 1
                    else:
                        y += 1
                        x = x - seqX - 1
                        break

                if seqX >= 100:
                    x, y = pos
                    seqY = 1
                    while x <= pos[0] + (seqX - 100):
                        y += 1
                        self.reset()
                        self.run(x)
                        self.run(y)
                        out = self.getOutput()[0]
                        if out == 1:
                            seqY += 1
                        else:
                            if seqY >= 100:
                                found = True
                                print(x, pos[1])
                                break
                            else:
                                print("seq:", seqX, seqY)
                                y = pos[1]
                                seqY = 1
                                x += 1
                    x = pos[0] - 1
                    y = pos[1] + 1
    

            x += 1
            self.reset()





if __name__ == '__main__':
    drone = Drone("input.txt", 500)
    #print(drone.nbOfAffectedPoints())
    drone.findSquare()
        
            
            