from PIL import Image
import random

def move_in_random_cardinal_direction(point):
    randomized = random.randint(1, 4)
    if randomized == 1:
        return (point[0] + 1, point[1])
    elif randomized == 2:
        return (point[0] - 1, point[1])
    elif randomized == 3:
        return (point[0], point[1] + 1)
    else:
        return (point[0], point[1] - 1)

def is_illegal_position(position, WIDTH, HEIGHT):
    if position[0] < 0:
        return True
    if position[0] >= WIDTH:
        return True
    if position[1] < 0:
        return True
    if position[1] >= HEIGHT:
        return True
    return False

WIDTH = 200
HEIGHT = 200
WHITE = (255, 255, 255)
PASSAGE = WHITE
BLACK = (0, 0, 0)
WALL = BLACK
im = Image.new("RGB", (WIDTH, HEIGHT), WALL)
pixels = im.load()
position = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
for _ in range(5000):
    pixels[position[0], position[1]] = PASSAGE
    position = move_in_random_cardinal_direction(position)
    if is_illegal_position(position, WIDTH, HEIGHT):
        break

im.save("maze.png")
im.show()  # it may not work in rare cases, but generally very, very useful
