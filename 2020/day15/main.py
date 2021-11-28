

def findLastNumber(input, occ):
    start = len(input)
    occurrences = {}
    count = {}
    last = input[-1]

    for idx, i in enumerate(input):
        count[i] = 1
        occurrences[i] = idx + 1
        

    for i in range(start, occ):
        if count[last] == 1:
            last = 0
        else:
            newNum = i - occurrences[last]
            occurrences[last] = i
            last = newNum

        if last not in occurrences.keys():
            occurrences[last] = i + 1
            count[last] = 1
        else:
            count[last] += 1


    return(last)

def part1(input):
    print("Part 1:", findLastNumber(input, 2020))

def part2(input):
    print("Part 2:", findLastNumber(input, 30000000))
    

if __name__ == "__main__":
    input = [16,12,1,0,15,7,11]
    part1(input)
    part2(input)