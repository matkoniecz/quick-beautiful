from PIL import Image
import random
import time


def main():
    WIDTH = 100
    HEIGHT = 100
    WHITE = (255, 255, 255)
    PASSAGE_COLOR = WHITE
    BLACK = (0, 0, 0)
    WALL_COLOR = BLACK
    im = Image.new("RGB", (WIDTH, HEIGHT), WALL_COLOR)
    pixels = im.load()

    candidates_list = []
    candidates_list.append((10, 10))
    while len(candidates_list) > 0:
        processed = candidates_list.pop()
        x = processed[0]
        y = processed[1]
        pixels[x, y] = PASSAGE_COLOR
        for child in children(x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
            candidates_list.append(child)
    im.show()
    im.save("maze.png")


def children(parent_x, parent_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    up = (parent_x, parent_y - 1)
    left = (parent_x - 1, parent_y)
    right = (parent_x + 1, parent_y)
    down = (parent_x, parent_y + 1)
    returned = []
    if inside_image(up[0], up[1], WIDTH, HEIGHT):
        if pixels[up[0], up[1]] != PASSAGE_COLOR:
            returned.append(up)
    if inside_image(left[0], left[1], WIDTH, HEIGHT):
        if pixels[left[0], left[1]] != PASSAGE_COLOR:
            returned.append(left)
    if inside_image(down[0], down[1], WIDTH, HEIGHT):
        if pixels[down[0], down[1]] != PASSAGE_COLOR:
            returned.append(down)
    if inside_image(right[0], right[1], WIDTH, HEIGHT):
        if pixels[right[0], right[1]] != PASSAGE_COLOR:
            returned.append(right)
    return returned


def is_populated(x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    """returns true if this locations contains passage, false if wall or is outside image"""
    if not inside_image(x, y, WIDTH, HEIGHT):
        return False
    if pixels[x, y] == PASSAGE_COLOR:
        return True
    return False


def inside_image(x, y, WIDTH, HEIGHT):
    """
    returns true if (x, y) is inside image of size (WIDTH, HEIGHT),
    return false otherwise
    """
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= WIDTH:
        return False
    if y >= HEIGHT:
        return False
    return True


main()
