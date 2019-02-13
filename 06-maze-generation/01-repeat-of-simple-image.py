from PIL import Image
width = 200
height = 200
WHITE = (255, 255, 255)
PASSAGE = WHITE
BLACK = (0, 0, 0)
WALL = BLACK
im = Image.new("RGB", (width, height), WALL)
pixels = im.load()
pixels[10, 10] = PASSAGE

im.save("maze.png")
im.show()  # it may not work in rare cases, but generally very, very useful
