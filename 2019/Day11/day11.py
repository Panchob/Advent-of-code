import sys
import os
from tkinter import *
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Intcode.Intcode import Intcode

class Painter(Intcode):
    def __init__(self, file):
        self.__canvas = {}
        self.__position = (50, 50) 
        self.__direction = "U"
        Intcode.__init__(self, file)

    def paints(self, firstInput):
        input = firstInput
        while not self.isStopped():
            self.run(input)
            out = self.getOutput()
            x, y = self.__position
            self.__canvas[(x, y)] = 0 if out[0] == 0 else 1
            self.turn(out[1])
            x, y = self.move()

            if (x, y) in self.__canvas:
                input = self.__canvas[(x, y)]
            else:
                input = 0
    

    def turn(self, instruction):
        directions = ["U", "R", "D", "L"]
        i = directions.index(self.__direction)
        instruction = -1 if instruction == 0 else instruction

        if i + instruction != 0:
            # Cycle trough the directions
            self.__direction = directions[(i + instruction) % len(directions)]
        else:
            self.__direction = 'U'


    def move(self):
        angles = {
            "U": (0, -25),
            "D":  (0, 25),
            "L": (-25, 0),
            "R": (25, 0)
        }
        x, y = self.__position
        incX, incY = angles[self.__direction]
        x += incX
        y += incY
        self.__position = (x, y)
        return (x, y)


    def numberOfPanelPainted(self):
        return len(self.__canvas)
    

    def printMessage(self):
        tk = Tk()
        tk.title("Points")
        c = Canvas(tk, width=1150, height=275)
        c.pack(expand=1, fill=BOTH)

        for k, v in self.__canvas.items():
            x, y = k
            if v == 1:
                c.create_rectangle(x, y, x + 20, y + 20, outline="#fb0", fill="#fb0")

        mainloop()


if __name__ == "__main__":
    painter = Painter("input.txt")
    painter.paints(0)
    print("Part 1: The robots painted", painter.numberOfPanelPainted(), "panels")

    painter = Painter("input.txt")
    painter.paints(1)
    painter.printMessage()

