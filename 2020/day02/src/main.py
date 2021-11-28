from pathlib import Path
file = Path("day02/input.txt")

def part1(input):
    valid = 0
    for i in input:
        letterCount = i["text"].count(i["letter"])
        if letterCount <= i["max"] and letterCount >= i["min"]:
            valid += 1
    
    print("Part1", valid)
        
def part2(input):
    valid = 0
    for i in input:
        index1, index2 = map(lambda n: n - 1, [i["min"], i["max"]])
        if (i["text"][index1] == i["letter"]) ^ (i["text"][index2] == i["letter"]):
            valid+= 1

    print("Part2", valid)


if __name__ == "__main__":
    f = open(file)
    input = []

    for line in f.readlines():
        rule, text = line.split(":")
        min, rest = rule.split("-")
        max, letter = rest.split(" ")
        input.append({
            "min": int(min),
            "max": int(max),
            "letter":letter,
            "text": text.strip()
        })

    part1(input)
    part2(input)
    
