from PIL import Image, ImageDraw
width = 200
height = 200
im = Image.new("RGB", (width, height), (100, 100, 100))

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
draw.line((20, 20, 50, 300), fill=(255, 255, 255))

x0 = 50
y0 = 59
x1 = 100
y1 = 190
draw.rectangle(((x0, y0), (x1, y1)), fill=(255, 0, 0))

x = 100
y = 94
r = 30
draw.ellipse(((x-r, y-r), (x+r, y+r)), fill=(0, 255, 0))

for i in range(10):
    x0 = i * 20
    y0 = i * 20
    x1 = x0 + 10
    y1 = y0 + 10
    draw.rectangle(((x0, y0), (x1, y1)), fill=(255, 255, 0))

draw.polygon(((10, 10), (10, 190), (157, 15)), fill=(50, 200, 250))

im.save("generated.png")
im.show()
