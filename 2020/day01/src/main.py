from pathlib import Path
file = Path("day01/input.txt")

def part1(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if(numbers[i] + numbers[j] == 2020):
                print("PART 1:", numbers[i] * numbers[j])
                break

def part2(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if(numbers[i] + numbers[j] + numbers[k] == 2020):
                    print("PART 2:", numbers[i] * numbers[j] * numbers[k])
                    break


if __name__ == "__main__":
    f = open(file)
    numbers = list(map(lambda l : int(l), f.readlines()))
    part1(numbers)
    part2(numbers)
