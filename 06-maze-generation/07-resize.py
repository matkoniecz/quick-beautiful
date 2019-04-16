import random
from PIL import Image


def main():
    WIDTH = 319
    HEIGHT = 168
    TILE_SIZE_IN_PIXELS = 6
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
    im = im.resize((WIDTH*TILE_SIZE_IN_PIXELS, HEIGHT*TILE_SIZE_IN_PIXELS))
    im.show()
    im.save("maze.png")


def children(parent_x, parent_y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    up = (parent_x, parent_y - 1)
    left = (parent_x - 1, parent_y)
    right = (parent_x + 1, parent_y)
    down = (parent_x, parent_y + 1)
    returned = []
    if is_safe_to_tunnel(parent_x, parent_y, up[0], up[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        returned.append(up)
    if is_safe_to_tunnel(parent_x, parent_y, left[0], left[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        returned.append(left)
    if is_safe_to_tunnel(parent_x, parent_y, down[0], down[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        returned.append(down)
    if is_safe_to_tunnel(parent_x, parent_y, right[0], right[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        returned.append(right)
    return returned


def is_safe_to_tunnel(parent_x, parent_y, x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    """
    returns true if location (x, y) can be turned into a passage
    false otherwise

    protects agains going outside image or making
    loop or passage wider than 1 tile

    returns false if (x, y) is not inside the image
    returns false if (x, y) is already a passage
    returns false if there are passages around (x, y) that are
    not on (parent_x, parent_y) location or around it
    returns true if location (x, y) can be turned into a passage
    """
    if not inside_image(x, y, WIDTH, HEIGHT):
        return False
    if pixels[x, y] == PASSAGE_COLOR:
        return False
    if is_colliding_with_other_tunnels(parent_x, parent_y, x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
        return False
    return True


def is_colliding_with_other_tunnels(parent_x, parent_y, x, y, pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    """
    checks whatever tunnel at this legal location can
    be placed without colliding with other tunnels
    """
    for offset in offsets_to_surrounding_tiles():
        if is_populated(x + offset[0], y + offset[1], pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
            x_distance_to_parent = x + offset[0] - parent_x
            y_distance_to_parent = y + offset[1] - parent_y
            if abs(x_distance_to_parent) + abs(y_distance_to_parent) > 1:
                return True
    return False

def offsets_to_surrounding_tiles():
    return [(1, 0), (1, -1), (0, -1), (-1, -1),
            (-1, 0), (-1, 1), (0, 1), (1, 1)]


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
