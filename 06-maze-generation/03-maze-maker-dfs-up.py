from PIL import Image


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
        for child in children(x, y, pixels, WIDTH, HEIGHT):
            candidates_list.append(child)
    im.show()
    im.save("maze.png")


def children(parent_x, parent_y, pixels, WIDTH, HEIGHT):
    up = (parent_x, parent_y - 1)
    returned = []
    if inside_image(up[0], up[1], WIDTH, HEIGHT):
        returned.append(up)
    return returned


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
