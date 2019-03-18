from PIL import Image
import random

WIDTH = 200
HEIGHT = 200
WHITE = (255, 255, 255)
PASSAGE_COLOR = WHITE
BLACK = (0, 0, 0)
WALL_COLOR = BLACK


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


def main():
    im = Image.new("RGB", (WIDTH, HEIGHT), WALL_COLOR)
    pixels = im.load()
    position = (WIDTH//2, HEIGHT//2)
    pixels[position[0], position[1]] = PASSAGE_COLOR
    position = move_in_random_cardinal_direction(position)
    pixels[position[0], position[1]] = PASSAGE_COLOR
    position = move_in_random_cardinal_direction(position)
    pixels[position[0], position[1]] = PASSAGE_COLOR

    im.save("maze.png")
    im.show()  # it may not work in rare cases, but generally very, very useful


main()