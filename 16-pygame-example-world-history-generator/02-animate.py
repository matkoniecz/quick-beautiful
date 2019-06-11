import pygame
import sys
import time
from pygame.locals import *


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (240, 240, 240)
    BLUE = (100, 100, 255)

    x = -180

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAY.fill(WHITE)
        pygame.draw.rect(DISPLAY, BLUE, (x, 50, 180, 180))
        x+=1
        time.sleep(0.01)
        pygame.display.update()


main()
