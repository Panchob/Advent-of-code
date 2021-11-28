
import sys
import os

ANS = 19690720

def run(l):
    i = 0

    while i < len(l):
        instruction = l[i]

        # 99 - End
        if instruction == 99:
            break
        # The two values to use.
        v1 = l[i + 1]
        v2 = l[i + 2]
        # Where to store the result.
        r = l[i + 3]

        # 1 - addition
        if  instruction == 1:
            l[r] = l[v1] + l[v2]
        # 2 - multiplication
        elif l[i] == 2:
            l[r] = l[v1] * l[v2]
        else:
            break
        # increment by 4 to get to the next instruction
        i += 4

    return l


def part2(l):
    output = 0
    current = 1 # noun position

    while(output != ANS):
        # Using a copy act as a data refresh
        output = run(l[:])[0]

        if(output < ANS):
            l[current] += 1
        elif(output > ANS):
            l[current] -= 1
            current += 1 # verb position

    # The given answer format is 100 * noun + verb   
    print("Part 2:", 100 * l[1] + l[2])


if __name__ == '__main__': 
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        l = list(map(int, f.read().split(",")))
        # Uses a copy to use it in part 1 and 2
        print("Part 1:", run(l[:])[0])
        part2(l)
