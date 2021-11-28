from pathlib import Path
file = Path("day08/input.txt")

TOGGLE = {
    "jmp":"nop",
    "nop":"jmp",
    "acc":"acc"
}

def game(instructions):
    history = set()
    accumulator = 0
    index = 0

    while index < len(instructions):
        if index in history:
            return (False, accumulator)
        else:
            history.add(index)

        if instructions[index][0] == "acc":
            accumulator += int(instructions[index][1])
            index += 1
        elif instructions[index][0] == "jmp":
            index += int(instructions[index][1])
        elif instructions[index][0] == "nop":
            index += 1
    
    return (True, accumulator)


def part1(instructions):
    print("Part 1:", game(instructions))
        
    
def part2(instructions):
    for instruction in instructions:
        instruction[0] = TOGGLE[instruction[0]]
        result = game(instructions)

        if result[0]:
            print("Part 2:", result[1])
            break
        else:
            instruction[0] = TOGGLE[instruction[0]]
    

if __name__ == "__main__":
    f = open(file)

    instructions = list(map(lambda l: l.rstrip().split(" "), f.readlines()))
    part1(instructions)
    part2(instructions)
       

