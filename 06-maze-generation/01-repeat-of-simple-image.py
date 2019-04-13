from PIL import Image
WIDTH = 200
HEIGHT = 200
WHITE = (255, 255, 255)
PASSAGE_COLOR = WHITE
BLACK = (0, 0, 0)
WALL_COLOR = BLACK
im = Image.new("RGB", (WIDTH, HEIGHT), WALL_COLOR)
pixels = im.load()
pixels[10, 10] = PASSAGE_COLOR

im.save("maze.png")
im.show()  # it may not work in rare cases, but generally very, very useful
