from PIL import Image
import random
import time


def main():
    WIDTH = 319
    HEIGHT = 168
    PIXEL_SIZE = 6
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
        new_candidates = children(x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR)
        if len(new_candidates) > 0:
            candidates_list.append(processed)
            candidates_list.append(random.choice(new_candidates))
    im = im.resize((WIDTH*PIXEL_SIZE, HEIGHT*PIXEL_SIZE))
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
            if is_safe_to_tunnel(parent_x, parent_y, up[0], up[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
                returned.append(up)
    if inside_image(left[0], left[1], WIDTH, HEIGHT):
        if pixels[left[0], left[1]] != PASSAGE_COLOR:
            if is_safe_to_tunnel(parent_x, parent_y, left[0], left[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
                returned.append(left)
    if inside_image(down[0], down[1], WIDTH, HEIGHT):
        if pixels[down[0], down[1]] != PASSAGE_COLOR:
            if is_safe_to_tunnel(parent_x, parent_y, down[0], down[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
                returned.append(down)
    if inside_image(right[0], right[1], WIDTH, HEIGHT):
        if pixels[right[0], right[1]] != PASSAGE_COLOR:
            if is_safe_to_tunnel(parent_x, parent_y, right[0], right[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
                returned.append(right)
    return returned


def is_safe_to_tunnel(parent_x, parent_y, x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    delta_x = x - parent_x
    delta_y = y - parent_y
    forward_x = x + delta_x
    forward_y = y + delta_y
    if is_populated(forward_x, forward_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    side_x = x + delta_y
    side_y = y + delta_x
    if is_populated(side_x, side_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    side_x = x - delta_y
    side_y = y - delta_x
    if is_populated(side_x, side_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    corner_x = x + delta_y + delta_x
    corner_y = y + delta_x + delta_y
    if is_populated(corner_x, corner_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    corner_x = x - delta_y + delta_x
    corner_y = y - delta_x + delta_y
    if is_populated(corner_x, corner_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    return True


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
