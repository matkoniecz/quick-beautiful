from PIL import Image


def get_color(x, y):
    r = 40
    center = (30, 200)
    if ((x-center[0])**2 + (y-center[1])**2) < r * r:
        return (10, 250, 10)
    if x < 50:
        return (220, 80, 00)
    if x > y:
        return (120, 30, 60)
    if 2 * x > y:
        return (220, 30, 60)
    return (250, 250, 50)


width = 500
height = 500
# https://pillow.readthedocs.io/en/latest/reference/Image.html
im = Image.new("RGB", (width, height), (255, 0, 0))
pixels = im.load()

for x in range(width):
    for y in range(height):
        pixels[x, y] = get_color(x, y)

im.save("generated.png")
im.show()
