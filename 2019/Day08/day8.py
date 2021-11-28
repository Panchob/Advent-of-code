import numpy as np
import os
import sys
import webbrowser
WIDTH = 25
HEIGHT = 6


def findLayer(image):
    layer = []
    i = 0
    out = 0
    currentMin = sys.maxsize

    for c in image:
        layer.append(int(c))
        i += 1

        # The layer is complete.
        if i == WIDTH * HEIGHT:
            i = 0
            l = np.array(layer)
            zeroCount = np.count_nonzero(l == 0)
            oneCount = np.count_nonzero(l == 1)
            twoCount = np.count_nonzero(l == 2)

            if zeroCount < currentMin:
                currentMin = zeroCount
                # The output is the number of 1 and 2 digits multiplied
                # together
                out = oneCount * twoCount
            # Refresh for next layer
            layer = []
    return out


def decodeImage(image):
    layer = []
    message = np.full((HEIGHT, WIDTH), 'O')

    i = 0
    j = 0
    # By going from top to bottom, I just have to overwrite what came before.
    for c in image:
        if(c == '0' and message[j][i] == 'O'):
            message[j][i] = ' '
        elif (c == '1' and message[j][i] == 'O'):
            message[j][i] = 'X'
        i += 1
        if i == WIDTH:
            i = 0
            j += 1
            if j == HEIGHT:
                j = 0

    np.savetxt(os.path.join(sys.path[0], "out.txt"), message, fmt='%s')

if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        image = f.read()
        print(findLayer(image))
        decodeImage(image)
        webbrowser.open(os.path.join(sys.path[0], "out.txt"))
