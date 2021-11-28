from pathlib import Path
file = Path("day09/input.txt")
    
def part1(sequence):
    base = 25
    limit = 0

    for num in sequence[base:]:
        valid=False
        preamble = sequence[limit:base+limit]
        for i in preamble:
            if num - i in preamble:
                valid=True
                break
        
        if not valid:
            print("Part 1:", num)
            break
        limit+=1

def part2(sequence):
    base = 0
    while base < len(sequence):
        subSeq = []
        index = 0
        while sum(subSeq) < 18272118:
            subSeq.append(sequence[base + index])
            index += 1
        
        if sum(subSeq) == 18272118:
            print("Part 2:", min(subSeq) + max(subSeq))
            break
        base += 1

if __name__ == "__main__":
    f = open(file)
    sequence = list(map( lambda l: int(l.rstrip()), f.readlines()))
    part1(sequence)
    part2(sequence)
       

