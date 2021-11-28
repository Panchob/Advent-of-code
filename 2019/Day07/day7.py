from Intcode import Intcode
import sys
import os
import itertools

class Amplifier(Intcode):
   def __init__(self, file, phase):
      self.__phase = phase
      Intcode.__init__(self, file)
   

   def runPhase(self):
      self.run(self.__phase)
   

   def outputSignal(self, input):
      self.run(input)
      return self.getOutput()[0]


def startAmps(amplifiers):
   for amp in amplifiers:
      amp.runPhase()


def findBestOutput(signal, feedbackloop):
   sequences = itertools.permutations(signal)
   maxOut = 0

   for seq in sequences:
      amplifiers = []
      out = 0
      amplifiers = [Amplifier("input.txt", int(phase)) for phase in seq]
      startAmps(amplifiers)

      if feedbackloop:
         i = 0
         currentAmp = amplifiers[0]

         while not currentAmp.isStopped():
            out = currentAmp.outputSignal(out)
            i += 1
            currentAmp = amplifiers[i % len(amplifiers)]

      else:
         for amp in amplifiers:
             out = amp.outputSignal(out)
      
      maxOut = out if out > maxOut else maxOut

   return maxOut


if __name__ == "__main__":

   part1Signal = ['4','3', '2', '1','0']
   part2Signal = ['5', '6', '7', '8', '9']

   print("Part 1:", findBestOutput(part1Signal, feedbackloop=False))
   print("Part 2:", findBestOutput(part2Signal, feedbackloop=True))