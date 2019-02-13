from PIL import Image
import random

WIDTH = 200
HEIGHT = 200
WHITE = (255, 255, 255)
PASSAGE = WHITE
BLACK = (0, 0, 0)
WALL = BLACK
im = Image.new("RGB", (WIDTH, HEIGHT), WALL)
pixels = im.load()
pixels[random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)] = PASSAGE

im.save("maze.png")
im.show()  # it may not work in rare cases, but generally very, very useful
