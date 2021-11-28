import sys
import os
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

# Simple loop that output and text based adventure game.
# Not automated at all but pretty fun!
if __name__ == "__main__":
    droid = Intcode(file="input.txt", OutputAsASCII=True)

    while not droid.isStopped():
        print("".join(droid.getOutput()))
        command = input() + "\n"

        for i in map(ord, command):
            droid.run(i)