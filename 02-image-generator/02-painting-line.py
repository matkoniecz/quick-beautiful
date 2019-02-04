from PIL import Image, ImageDraw
width = 200
height = 200
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
im = Image.new("RGB", (width, height), GRAY)

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
draw.line((20, 20, 50, 300), fill=WHITE)

im.save("generated.png")
im.show()
