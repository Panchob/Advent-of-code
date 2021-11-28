import os
import sys
import pygame
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Intcode.Intcode import Intcode


class Tile:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


class BrickBreak(Intcode):
    def __init__(self, file):
        Intcode.__init__(self, file)
        self.__tiles = []
        self.__paddle = None
        self.__ball = None
        self.__score = 0


    def render(self, input=None):
        self.run(input)
        self.__tiles = []
        output = self.getOutput()
        i = 0
        while i < len(output):
            self.__tiles.append(Tile(output[i], output[i + 1], output[i + 2]))
            self.updateGame()
            i += 3
    

    def updateGame(self):
        for tile in self.__tiles:
            if tile.id == 3:
                self.__paddle = tile
            elif tile.id == 4:
                self.__ball = tile
            elif tile.x == -1:
                self.__score = tile.id


    def countBlocks(self):
        nBblocks = 0
        for tile in self.__tiles:
            if tile.id == 2:
                nBblocks += 1
        return nBblocks

    
    def playGame(self):
        while True:
            if self.__ball.x < self.__paddle.x:
                input = -1
            elif self.__ball.x > self.__paddle.x:
                input = 1
            else:
                input = 0
            
            self.render(input)

            if self.isStopped():
                break

        print(self.__score)
    

    def displayGame(self):
        pygame.init()
        font = pygame.font.Font(None, 36)
        # Set up the drawing window
        screen = pygame.display.set_mode([1320, 600])

        # Run until the user asks to quit
        running = True
        input = 0
        screen.fill((0, 0, 0))
        
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            for tile in self.__tiles:
                if tile.id == 0:
                    color = (0, 0, 0)
                elif tile.id == 2:
                    color = (245, 66, 99)
                else:
                    color = (255, 255, 255)

                pygame.draw.rect(screen, color, [tile.x*30, tile.y*30, 30, 30])

            if self.__ball.x < self.__paddle.x:
                input = -1
            elif self.__ball.x > self.__paddle.x:
                input = 1
            else:
                input = 0
            
            self.render(input)

            if brickBreak.isStopped():
                running = False

            # Flip the display
            pygame.display.flip()
            pygame.time.Clock().tick(60)


if __name__ == '__main__': 
    brickBreak = BrickBreak("input.txt")
    brickBreak.render()
    print("Part 1:", brickBreak.countBlocks())
    brickBreak.playGame()
    

        
        



    
