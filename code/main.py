# importing the required modules
import pygame
from pygame.locals import *
import time

SIZE = 40
class apple:
   def __init__ (self, parent_screen):
     self.block = pygame.image.load("apple.jpg").convert()
     self.parent_screen = parent_screen
     self.x = SIZE*3
     self.y = SIZE*3

   def draw(self):
       self.parent_screen.blit(self.image, (self.x, self.y))
       pygame.display.flip()


class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length

        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    # this is to control the direction during keystrokes
    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()


    def draw(self):
        self.parent_screen.fill((3, 248, 252))
        for i in range(self.length):
         self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
         pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = apple(self.surface)
        self.apple.draw()

    def run(self):
        running = True
    #While for the navigation of the block
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            self.apple.draw()

            time.sleep(.3)

if __name__ == '__main__':
    game = Game()
    game.run()











