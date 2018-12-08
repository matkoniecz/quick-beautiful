from PIL import Image


width = 500
height = 500
# https://pillow.readthedocs.io/en/latest/reference/Image.html
im = Image.new("RGB", (width, height), (255, 0, 0))
pixels = im.load()

for x in range(width):
    for y in range(height):
        pixels[x, y] = (x, y, 255)

im.save("generated.png")
im.show()
