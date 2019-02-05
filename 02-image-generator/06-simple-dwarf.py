"""
landscape generation topic: dwarves in front of their home

lets draw dwarf using as simplest geometry elements as possible 
"""
from PIL import Image, ImageDraw

DWARF_CLOTHES = (240, 30, 20)
GRAY_BEARD = (240, 240, 240)
FACE_COLOR = (255, 182, 193)
BACKGROUND = (110, 200, 110)

def hat(draw, x0, x1, head_center, r):
    head_x, head_y = head_center
    left_bottom = (x0 - 15, head_y)
    right_bottom = (x1 + 15, head_y)
    top = (head_x, head_y - 2*r)
    draw.polygon((left_bottom, right_bottom, top), fill=DWARF_CLOTHES)


def beard(draw, x0, x1, head_center, r):
    head_x, head_y = head_center
    left_top = (x0, head_y + 10)
    right_top = (x1, head_y + 10)
    bottom = (head_x, head_y + 2*r)
    draw.polygon((left_top, right_top, bottom), fill=GRAY_BEARD)


def face(draw, head_center, r):
    head_x, head_y = head_center
    circle_bounding_box = ((head_x-r, head_y-r), (head_x+r, head_y+r))
    draw.ellipse(circle_bounding_box, fill=FACE_COLOR)


def dwarf(draw, x0, y0, figure_height):
    figure_width = figure_height//2.5
    x1 = x0 + figure_width
    y1 = y0 - figure_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=DWARF_CLOTHES)
    head_x = (x0 + x1)//2
    head_y = y1
    r = figure_width // 1.5
    head_center = head_x, head_y
    face(draw, head_center, r)
    hat(draw, x0, x1, head_center, r)
    beard(draw, x0, x1, head_center, r)

def landscape():
    width = 2000
    height = 400
    im = Image.new("RGB", (width, height), BACKGROUND)

    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
    draw = ImageDraw.Draw(im)

    figure_height = 80

    x0 = 20
    y0 = height - 70
    dwarf(draw, x0, y0, figure_height)
    dwarf(draw, x0 + 80, y0, figure_height)
    dwarf(draw, x0 + 190, y0, figure_height)
    dwarf(draw, x0 + 260, y0, figure_height)

    im.save("dwarves.png")
    im.show()

landscape()
