"""
landscape generation topic: dwarves in front of their home

lets draw dwarf using as simplest geometry elements as possible 
"""
from PIL import Image, ImageDraw

def hat(draw, x0, x1, head_x, head_y, r):
    draw.polygon(((x0 - 15, head_y), (x1 + 15, head_y), (head_x, head_y - 2*r)), fill=(240, 30, 20))

def beard(draw, x0, x1, head_x, head_y, r):
    draw.polygon(((x0, head_y + 10), (x1, head_y + 10), (head_x, head_y + 2*r)), fill=(240, 240, 240))

def dwarf(draw, x0, y0):
    figure_height = 60
    figure_width = 30
    x1 = x0 + figure_width
    y1 = y0 - figure_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=(240, 30, 20))
    head_x = (x0 + x1)/2
    head_y = y1
    r = figure_width / 1.5
    draw.ellipse(((head_x-r, head_y-r), (head_x+r, head_y+r)), fill=(255, 182, 193))
    hat(draw, x0, x1, head_x, head_y, r)
    beard(draw, x0, x1, head_x, head_y, r)


def grass(draw, width, height):
    x0 = 0
    y0 = height - 1
    x1 = width - 1
    y1 = height - grass_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=(20, 230, 20))


width = 2000
height = 400
im = Image.new("RGB", (width, height), (110, 200, 110))

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)

grass_height = int(height / 3)

x0 = 20
y0 = height - int(grass_height / 2)
dwarf(draw, x0, y0)
dwarf(draw, x0 + 80, y0)
dwarf(draw, x0 + 190, y0)
dwarf(draw, x0 + 260, y0)

im.save("dwarves.png")
im.show()
