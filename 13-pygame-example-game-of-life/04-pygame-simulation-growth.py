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
                self.world[x].append(0)
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        self.world[x][y] = 1

    def evolve(self):
        x_size = len(self.world)
        y_size = len(self.world[0])

        new_world = []
        for x in range(x_size):
            new_world.append([])
            for y in range(y_size):
                new_world[x].append(0)

        for x in range(x_size):
            for y in range(y_size):
                new_world[x][y] = 0
                for delta_x in [-1, 0, 1]:
                    for delta_y in [-1, 0, 1]:
                        checked_x = (x + delta_x + x_size) % x_size
                        checked_y = (y + delta_y + y_size) % y_size
                        if self.world[checked_x][checked_y] == 1:
                            new_world[x][y] = 1

        self.world = new_world

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
    world = World((80, 80))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        world.show_world_state()
        world.evolve()
        time.sleep(0.2)


main()
