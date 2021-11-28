import sys
import os
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Intcode.Intcode import Intcode


class Packet:
    def __init__(self, values, destination):
        self.values = values
        self.destination = destination
        self.time = 0


class Computer(Intcode):
    def __init__(self, file):
        Intcode.__init__(self, file)
        self.__receivedPackets = []
    

    def isIdle(self):
        if not self.__receivedPackets:
            return True
        else:
            False
    
    
    def boot(self, address):
        self.run(address)


    def storePacket(self, packet):
        self.__receivedPackets.append(packet)

    
    def receivePacket(self):
        if not self.__receivedPackets:
            self.run(-1)
        else:
            packet = self.__receivedPackets.pop(0)
            x, y = packet.values
            self.run(x)
            self.run(y)
    

    def sendPackets(self):
        out = self.getOutput()
        i = 0
        packets = []

        while i < len(out):
            packets.append(Packet((out[i+1], out[i+2]), out[i]))
            i += 3

        return packets
            

class Network:
    def __init__(self, size):
        self.__computers = [Computer("input.txt") for _ in range(size)]
        self.__size = size
        self.__nat = None
        self.__yValues = []


    def isIdle(self):
        res = True
        for c in self.__computers:
            if not c.isIdle():
                res = False
                break
        return res

  
    def bootAllComputers(self):
        for address in range(self.__size):
            self.__computers[address].boot(address)


    def communicate(self):
        found = False
        while not found:
            for computer in self.__computers:
                computer.receivePacket()
                packets = computer.sendPackets()

                for p in packets:
                    if p.destination == 255:
                        if self.__nat == None:
                            print("Part 1:", p.values[1])
                        self.__nat = p
                        nat = self.__nat
                        if self.isIdle():
                            self.__computers[0].storePacket(nat)
                            if nat.values[1] not in self.__yValues:
                                self.__yValues.append(nat.values[1])
                            else:
                                print("Part 2:", nat.values[1])
                                found = True

                        break
                    self.__computers[p.destination].storePacket(p)


if __name__ == "__main__":
    nic = Network(50)
    nic.bootAllComputers()
    nic.communicate()
    
