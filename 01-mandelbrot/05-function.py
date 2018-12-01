from PIL import Image


def get_color(x, y):
    if x < 50:
        return (220, 80, 00)
    if x > y:
        return (120, 30, 60)
    if 2 * x > y:
        return (220, 30, 60)
    return (250, 250, 50)


width = 500
height = 500
list_of_pixels = []
for _ in range(width*height):
    list_of_pixels.append((255, 0, 0))
im = Image.new("RGB", (width, height))
im.putdata(list_of_pixels)
pixels = im.load()

for x in range(width):
    for y in range(height):
        pixels[x, y] = get_color(x, y)

im.save("generated.png")
