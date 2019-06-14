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
    
    def neighbor_count(self, x, y, x_size, y_size):
        count = 0
        neighbors = [
            {"x": -1, "y": -1},
            {"x": -1, "y": 0},
            {"x": -1, "y": 1},
            {"x": 0, "y": -1},
            {"x": 0, "y": 1},
            {"x": 1, "y": -1},
            {"x": 1, "y": 0},
            {"x": 1, "y": 1},
        ]
        for delta in neighbors:
            checked_x = (x + delta["x"] + x_size) % x_size
            checked_y = (y + delta["y"] + y_size) % y_size
            if self.world[checked_x][checked_y] == 1:
                count += 1
        return count

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
                # https://en.wikipedia.org/wiki/Cellular_automaton
                # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
                # Any live cell with two or three live neighbours lives on to the next generation.
                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                new_world[x][y] = 0
                count = self.neighbor_count(x, y, x_size, y_size)
                if self.world[x][y] == 1:
                    if count == 2 or count == 3:
                        new_world[x][y] = 1
                elif count == 3:
                    new_world[x][y] = 1


        self.world = new_world


    def show_world_state(self):
        self.display.fill(self.background)
        for x in range(len(self.world)):
            for y in range(len(self.world[x])):
                color = None
                WHITE = (255, 255, 255)
                BLACK = (0, 0, 0)
                if self.world[x][y] == 0:
                    color = WHITE
                else:
                    color = BLACK
                size = self.cell_size
                pixel_x = x * size
                pixel_y = y * size
                pygame.draw.rect(self.display, color, (pixel_x, pixel_y, size, size))
        pygame.display.update()


def main():
    pygame.init()
    world = World((50, 50))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        world.show_world_state()
        world.evolve()


main()
