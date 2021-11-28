from math import gcd

NUMBER_OF_STEPS = 1000


def updateSystem(moons, nbOfSteps):
    for _ in range(nbOfSteps):
        for m in moons:
            others = filter(lambda x: x != m, moons)
            for other in others:
                m.changeVelocity(other)
        for m in moons:
            m.updatePosition()


def separateAxis(moons):
    axes = []
    for i in range(3):
        axis = []
        for m in moons:
            axis.append(Moon([m.position[i]], [0]))
        axes.append(axis)
    return axes


def totalEnergy(moons):
    total = 0
    for m in moons:
        total += m.energy()
    return total


def repeatAfter(axis):
    positions = [a.position[0] for a in axis]
    repeated = False
    i = 1

    while not repeated:
        updateSystem(axis, 1)
        i += 1
        updatedPositions = [a.position[0] for a in axis]
        if updatedPositions == positions:
            repeated = True
    return i


def allSystemRepeat(axes):
    cycles = []
    # For each sets of moons, find the cycle of x, y and z.
    for axis in axes:
        cycles.append(repeatAfter(axis))

    lcm = cycles[0]
    for i in cycles[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm


class Moon:
    def __init__(self, position, velocity=[0, 0, 0]):
        self.position = position
        self.__dimension = len(position)
        self.velocity = velocity[:]
    
    
    def changeVelocity(self, other):
        for i in range(self.__dimension):
            if self.position[i] > other.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < other.position[i]:
                self.velocity[i] += 1


    def updatePosition(self):
       for i in range(self.__dimension):
            self.position[i] += self.velocity[i]
    

    def energy(self):
        p = map(abs, self.position)
        v = map(abs, self.velocity)
        return sum(p) * sum(v)


if __name__ == '__main__': 
    io = Moon([13, -13, -2])
    europa = Moon([16, 2, -15])
    ganymede = Moon([7, -18, -12])
    callisto = Moon([-3, -8, -8])
    moons = [io, europa, ganymede, callisto]
    axes = separateAxis(moons[:])

    updateSystem(moons, NUMBER_OF_STEPS)

    print("Energy after", NUMBER_OF_STEPS,"steps:", totalEnergy(moons))   
    print("The moons cycle after:", allSystemRepeat(axes), "steps")
