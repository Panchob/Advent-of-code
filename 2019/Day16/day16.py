import os
import sys

PATTERN = [0, 1, 0, -1]

# TODO: I remember somebody doing this with modulo, I should look into it.
def next(current):
    if current == len(PATTERN) - 1:
        return 0
    else:
        return current + 1

# Skip all zero. Continue at the next index that have a value.
def phase(signal):
    # output to use by the next phase
    out = []
    # The current amount that the current number in PATTERN
    # must be repeated.
    mult = 1
    # The current position in PATTERN
    pos = 1

    for _ in range(len(signal)):
        # To count the number of time we used the current
        # pattern position (start at one).
        iteration = 1
        result = 0
        # Current position in the signal.
        i = 0
        while i <= len(signal) - 1:
            if PATTERN[pos] == 0:
                i += (mult - iteration)
                iteration = mult
            else:
                result += PATTERN[pos] * signal[i]
                iteration += 1
                i += 1

            if iteration >= mult:
                iteration = 0
                pos = next(pos)

        out.append(abs(result) % 10)
        mult += 1
        pos = 0
    return out
        
def multiphasing(signal, nb):
    out = signal
    for _ in range(nb):
        out = phase(out)

    return ''.join([str(l) for l in out[0:8]])

# The end of the sequence always follow the same pattern.
# TODO: Still very slow, I had to let it run 1h before having the
# answer. Insert maybe too slow, reversed as well.
def offsetPhasing(signal):
    out = []
    previous = 0
    for n in reversed(signal):
        current = (previous + n) % 10
        out.insert(0, current)
        previous = current
    return out


if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        signal = [int(c) for c in f.read()]

        #Part 1
        print(multiphasing(signal, 100))

        # Part 2
        f.seek(0)
        input = f.read() * 10000
        offset = int(''.join([i for i in input[0:7]]))
        signal = [int(c) for c in input[offset::]]

        for i in range(100):
            signal = offsetPhasing(signal)

        
        print(''.join([str(l) for l in signal[0:8]]))
