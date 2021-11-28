from pathlib import Path
file = Path("day11/input.txt")

seats = []
def checkAdjacent(index):
    x, y = index
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0) and validateIndex(x + i, y + j) and seats[x + i][ y + j] == "#":
                count += 1
    return count


def validateIndex(x , y):
    return  x >= 0 and \
            x < len(seats) and\
            y >= 0 and\
            y < len(seats[0])

def checkLine(index):
    increments = [(1,0), (0, 1), (1,1), (-1, 0), (0,-1), (-1, -1), (-1, 1), (1, -1)]
    occupied = 0
    for increment in increments:
        occupied += findInline(increment, index)
    return occupied


def findInline(increment, index):
    x, y = index
    dx, dy = increment

    while(True):
        x = x + dx
        y = y + dy
        if validateIndex(x, y):
            if seats[x][y] == "L":
                return 0
            elif seats[x][y] == "#":
                return 1
        else:
            return 0
        

functionMapping = {
    "part1" : checkAdjacent,
    "part2" : checkLine
}

def choosingProcess(part, limit):
    model = []
    rowIndex = 0
    global seats

    for row in seats:
        newRow = ["."] * len(row)
        for colIndex in range(len(row)):
            if row[colIndex] == "L":
                if functionMapping[part]((rowIndex, colIndex)) == 0 :
                    newRow[colIndex] = "#"
                else:
                    newRow[colIndex] = "L"
            elif row[colIndex] == "#":
                if functionMapping[part]((rowIndex, colIndex)) >= limit:
                    newRow[colIndex] = "L"
                else:
                    newRow[colIndex] = "#"
        model.append(newRow)
        rowIndex += 1

    if model == seats:
        return False
    else: 
        seats = model
        return True

def part1():
    notSameAsBefore = True
    count = 0
    while(notSameAsBefore):
        notSameAsBefore = choosingProcess("part1", 4)  

    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    print("Part 1:", count)

def part2():
    notSameAsBefore = True
    count = 0
    while(notSameAsBefore):
        notSameAsBefore = choosingProcess("part2", 5) 

    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    print("Part 2:", count)
           

if __name__ == "__main__":
    f = open(file)
    for l in f.readlines():
        seats.append(l.rstrip())
    seatsCopy = seats
    part1()
    seats = seatsCopy
    part2()


       

