import sys
import os

FIRST_PARAM = 0
SECOND_PARAM = 1
THIRD_PARAM = 2

class Intcode:
    def __init__(self, file):
        self.__memory = self.parse(file)[:]
        self.__output = []
        self.__pointer = 0
        self.__relativeBase = 0
        self.__waiting = False
        self.__stopped = False


    def parse(self, file):
        with open(os.path.join(sys.path[0], file), "r") as f:
            code = list(map(int, f.read().split(",")))
            buffer = [0] * 10000
            return code + buffer


    def positions(self, i):
        m = self.__memory
        # Append in the same order as the values in l. By using
        # modulo, if the length of the instruction is smaller than
        # the number of values, 0 is returned.
        modes = []
        modes.append((m[i]//100) % 10)
        modes.append((m[i]//1000) % 10)
        modes.append((m[i]//10000) % 10)

        # Start at one since the index is currently on
        # the instruction and not the first value. I reuse the same array
        # here to store the position (immediate or not) of the values.
        # Ex: j is 0 and position is 1 for [1002, 4, 3, 33]
        # modes = [0*][1][0]
        # l = ... [1002][4*][3][33] ... with * being the current index.
        position = 1
        for j in range(len(modes)):
            if i + position == len(m):
                break
            # Position mode
            if modes[j] == 0:
                modes[j] = m[i + position]
            # Immediate mode
            elif modes[j] == 1:
                modes[j] = i + position
            # Relative base mode
            else:
                modes[j] = self.__relativeBase + m[i + position]

            position += 1

        return modes
    

    def isStopped(self):
        return self.__stopped


    def getOutput(self):
        res = self.__output
        self.__output = []
        return res


    def run(self, input=None):
        p = self.__pointer
        m = self.__memory
        increment = 0

        while p < len(m):
            instruction = m[p] % 100
            if instruction == 99:
                self.__stopped = True
                break

            pos = self.positions(p)

            # 1 - addition
            if instruction == 1:
                m[pos[THIRD_PARAM]] = m[pos[FIRST_PARAM]] + m[pos[SECOND_PARAM]]
                increment = 4
            # 2 - multiplication
            elif instruction == 2:
                m[pos[THIRD_PARAM]] = m[pos[FIRST_PARAM]] * m[pos[SECOND_PARAM]]
                increment = 4
            # 3 - Store input value
            elif instruction == 3:
                if input == None:
                    self.__waiting = True
                    self.__pointer = p
                    break
                else:
                    m[pos[FIRST_PARAM]] = input
                    input = None
                    increment = 2
            # 4 - output value
            elif instruction == 4:
                self.__output.append((m[pos[FIRST_PARAM]]))
                increment = 2
            # 5 - Jump if true
            elif instruction == 5:
                if m[pos[FIRST_PARAM]] != 0:
                    p = m[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 6 - Jump if false
            elif instruction == 6:
                if m[pos[FIRST_PARAM]] == 0:
                    p = m[pos[SECOND_PARAM]]
                    increment = 0
                else:
                    increment = 3
            # 7 - Less than
            elif instruction == 7:
                if m[pos[FIRST_PARAM]] < m[pos[SECOND_PARAM]]:
                    m[pos[THIRD_PARAM]] = 1
                else:
                    m[pos[THIRD_PARAM]] = 0
                increment = 4
            # 8 - Equals
            elif instruction == 8:
                if m[pos[FIRST_PARAM]] == m[pos[SECOND_PARAM]]:
                    m[pos[THIRD_PARAM]] = 1
                else:
                    m[pos[THIRD_PARAM]] = 0
                increment = 4
            # 9 - Adjust relative base
            elif instruction == 9:
                self.__relativeBase += m[pos[FIRST_PARAM]]
                increment = 2
            # Bad instruction
            else:
                break
            p += increment