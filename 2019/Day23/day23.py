import sys
import os
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

# In a list since other option is [x, y]
DEFAULT_INPUT = [-1]

class Computer(Intcode):
    def __init__(self, file):
         super().__init__(file)
         self.__packets = []


    def __repr__(self):
        return 'Computer[packets: %i, idle: %s]' % (self.numberOfPacket(), self.waiting)

    def receivePacket(self, packet):
        self.__packets.append(packet)

    def numberOfPacket(self):
        return len(self.__packets)
    

    def getFirstPacket(self, time):
        if self.__packets and self.__packets[0].isUsable(time):
            return self.__packets.pop(0)
    

    def createPacket(self, input, time):
        packet = None

        for i in input:
            address = self.run(i)
        
        if address:
            x = self.run()
            y = self.run()
            packet = Packet(address, x, y, time)
        
        return packet
        

class Packet:
    def __init__(self, address, x, y, time):
        self.__address = address
        self.__x = x
        self.__y = y
        self.__time = time


    def __repr__(self):
        return 'Packet(Address: %i, x: %i, y: %i)' % (self.__address, self.__x, self.__y)


    def isUsable(self, time):
        return self.__time <= time


    def getXY(self):
        return [self.__x, self.__y]


    def addDelay(self, delay):
        self.__time += delay


    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address


class Network:
    def  __init__(self, size):
       self.__computers = [Computer("input.txt") for _ in range(50)]
       self.__time = 0
       self.__nat = None


    def bootAll(self):
        for address in range(len(self.__computers)):
            self.__computers[address].run(address)


    def communicate(self):
        for computer in self.__computers:
            currentPacket = computer.getFirstPacket(self.__time)
        
            if currentPacket:
                packetToSend = computer.createPacket(currentPacket.getXY(), self.__time)
            else:
                packetToSend = computer.createPacket(DEFAULT_INPUT, self.__time)

            self.send(packetToSend)


    def addTime(self):
        self.__time += 1
    

    def send(self, packet):
        if packet:
            address = packet.getAddress()

            if address == 255:
                if not self.__nat:
                    print("FOUND IT:", packet)
                packet.setAddress(0)
                self.__nat = packet
            else:
                self.__computers[address].receivePacket(packet)
            

    def resume(self):
        self.send(self.__nat)
        return self.__nat.getXY()


    def isIdle(self):
        for computer in self.__computers:
            if not computer.waiting or computer.numberOfPacket() > 0:
                return False
        return True



if __name__ == "__main__":
    network = Network(50)
    network.bootAll()

    while True:
        network.communicate()
        network.addTime()
        lastY = 0

        if network.isIdle():
            currentY = network.resume()[1]
            if currentY == lastY:
                print("PART TWO", lastY)
                break
            lastY = currentY
