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
    generate(pixels, WIDTH, HEIGHT, PASSAGE_COLOR)
    output_maze("maze.png", im, WIDTH, HEIGHT)


def generate(pixels, WIDTH, HEIGHT, PASSAGE_COLOR):
    """
    expands maze starting from (10, 10) as a seed location,
    as long as eligible places to carve new tunnels exist
    """
    candidates_list = [(10, 10)]
    while len(candidates_list) > 0:
        processed = candidates_list.pop()
        x, y = processed
        pixels[x, y] = PASSAGE_COLOR
        for child in children(x, y, pixels, WIDTH, HEIGHT):
            candidates_list.append(child)


def output_maze(image_output_filepath, image, WIDTH, HEIGHT):
    """
    shows maze image at the screen and
    outputs maze to specified location in image_output_filepath
    using file format implied by extensions
    """
    image.show()
    image.save(image_output_filepath)


def children(parent_x, parent_y, pixels, WIDTH, HEIGHT):
    """
    returns list of all currently eligible locations to expand from (parent_x, parent_y)
    list contains tuples of integers
    """
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
