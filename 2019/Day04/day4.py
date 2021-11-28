START_VALUE = 402328
END_VALUE = 864247


def isValid(password):
    isValid = False
    currentSequence = password[0]

    for number in password[1:]:
        # The password is always increasing
        if number < currentSequence:
            isValid = False
            break
        # It's not valid unless it have at least one repetition.
        if number != currentSequence:
            currentSequence = number
        else:
            isValid = True
    return isValid


def hasAGroupOfTwoMatchingDigits(password):
    currentSequence = password[0]
    sequenceSize = 1
    hasValidGroup = False

    for number in password[1:]:
        if number != currentSequence:
            currentSequence = number
            sequenceSize = 1
        else:
            sequenceSize = sequenceSize + 1
            hasValidGroup = True if sequenceSize == 2 else False
   
    return (hasValidGroup)


if __name__ == "__main__":
    part1 = 0
    part2 = 0
    validPasswords = []

    for n in range(START_VALUE, END_VALUE):
        # Change each number into an array
        password = [x for x in str(n)]

        if isValid(password):
            validPasswords.append(password)
    
    part1 = len(validPasswords)

    for password in validPasswords:
        if hasAGroupOfTwoMatchingDigits(password):
            part2 += 1

    print("Part one:", part1)
    print("part two:", part2)
