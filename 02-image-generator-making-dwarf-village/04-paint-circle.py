from PIL import Image, ImageDraw
WIDTH = 200
HEIGHT = 200
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
im = Image.new("RGB", (WIDTH, HEIGHT), GRAY)

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
draw.line((20, 20, 50, 300), fill=WHITE)

x0 = 50
y0 = 59
x1 = 100
y1 = 190
draw.rectangle(((x0, y0), (x1, y1)), fill=RED)

x = 100
y = 94
r = 30
draw.ellipse(((x-r, y-r), (x+r, y+r)), fill=GREEN)

im.save("generated.png")
im.show()
