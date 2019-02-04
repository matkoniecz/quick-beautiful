from PIL import Image, ImageDraw
width = 200
height = 200
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
im = Image.new("RGB", (width, height), GRAY)

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
draw.line((20, 20, 50, 300), fill=WHITE)

x0 = 50
y0 = 59
x1 = 100
y1 = 190
draw.rectangle(((x0, y0), (x1, y1)), fill=RED)

im.save("generated.png")
im.show()
