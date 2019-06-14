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
        windows_size = (size[0] * self.cell_size, size[1] * self.cell_size)
        self.display = pygame.display.set_mode(windows_size, 0, 32)
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
                size = self.cell_size
                pixel_x = x * size
                pixel_y = y * size
                pygame.draw.rect(self.display, color, (pixel_x, pixel_y, size, size))

        pygame.display.update()


def main():
    pygame.init()
    while True:
        world = World((100, 10))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        world.show_world_state()
        time.sleep(0.5)


main()
