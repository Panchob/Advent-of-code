import os
import sys
from Intcode import Intcode

    
if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:

        intCode = Intcode("input.txt")
        intCode.run(1)
        print("Part 1:", intCode.getOutput()[0])

        intCode = Intcode("input.txt")
        intCode.run(2)
        print("Part 2:", intCode.getOutput()[0])

        



    
