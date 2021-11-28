from pathlib import Path
file = Path("day14/input.txt")
binList = {}
key = 0

def part1(instructions):
    memory = {}

    for instruction in instructions:
        mask = instruction['mask'][::-1]
        newNum = [0] * len(mask)
        binary = bin(instruction['num'])
        binary = str(binary)[2:]
        binary = binary[::-1]
        memory[instruction['mem']] = 0


        for idx, n in enumerate(binary):
            newNum[idx] = n

        for idx, n in enumerate(mask):
            if mask[idx] != "X":
                newNum[idx] = n

        for idx, n in enumerate(newNum):
            if n == "1":
                memory[instruction['mem']] += pow(2, idx)

    print(sum(memory.values()))

def genbin(n, bs = ''):
    if n-1:
        genbin(n-1, bs + '0')
        genbin(n-1, bs + '1')
    else:
        binList[key].append('0' + bs)
        binList[key].append('1' + bs)

def part2(instructions):
    memory = {}
    for instruction in instructions:
        global key
        mask = instruction['mask'][::-1]
        newNum = [0] * len(mask)
        binary = bin(instruction['mem'])
        binary = str(binary)[2:]
        binary = binary[::-1]
        perm = 0

        for idx, n in enumerate(binary):
            newNum[idx] = n

        for idx, n in enumerate(mask):
            if n == 'X':
                perm += 1
                newNum[idx] = n
            elif n == '1':
                newNum[idx] = n

        if perm not in binList.keys():
            key = perm
            binList[perm] = []
            genbin(perm)

        for b in binList[perm]:
            idx = 0
            address = 0
            for i, n in enumerate(newNum):
                if n == "X":
                    if  b[idx] == "1":
                        address += pow(2, i)
                    idx += 1
                elif n == "1":
                   address += pow(2, i)

            memory[address] = instruction['num']
        
    
    print(sum(memory.values()))


if __name__ == "__main__":
    f = open(file)
    mask = ""
    instructions = []

    for l in f.readlines():
        mem = 0
        num = ""
        if l[:4] == "mask":
            mask = l[7:].rstrip()
        elif l[:3] == "mem":
            mem, num = l.split("]")
            mem = int(mem[4:])
            num = int(num[3:])

            instructions.append({
                "mask":mask,
                "mem":mem,
                "num":num
            })

    part1(instructions)
    part2(instructions)
