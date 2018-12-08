from PIL import Image, ImageDraw
width = 200
height = 200
im = Image.new("RGB", (width, height), (100, 100, 100))

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
draw.line((20, 20, 50, 300), fill=(255, 255, 255))

im.save("generated.png")
im.show()
