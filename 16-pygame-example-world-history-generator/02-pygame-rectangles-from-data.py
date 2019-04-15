import pygame
import sys
import time
import random
from pygame.locals import *


class World:
    def __init__(self, size):
        self.world = []
        self.background = (240, 240, 240)
        self.cell_size = 10
        self.display = pygame.display.set_mode(
            (size[0] * self.cell_size, size[1] * self.cell_size), 0, 32)
        for x in range(size[0]):
            self.world.append([])
            for y in range(size[1]):
                self.world[x].append(random.randint(0, 1))

    def show_world_state(self):
        self.display.fill(self.background)
        for x in range(len(self.world)):
            for y in range(len(self.world[x])):
                color = None
                BLUE = (70, 70, 255)
                RED = (255, 70, 70)
                if self.world[x][y] == 0:
                    color = BLUE
                else:
                    color = RED
                pygame.draw.rect(self.display, color, (x * self.cell_size,
                                                       y * self.cell_size, self.cell_size, self.cell_size))
        pygame.display.update()


def main():
    pygame.init()
    world = World((100, 10))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.01)
        world.show_world_state()


main()
