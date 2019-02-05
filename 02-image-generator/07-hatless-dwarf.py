"""
landscape generation topic: dwarves in front of their home

lets draw dwarf using as simplest geometry elements as possible 
"""
from PIL import Image, ImageDraw

WIDTH = 2000
HEIGHT = 400
FIGURE_HEIGHT = 80
DWARF_CLOTHES = (240, 30, 20)
GRAY_BEARD = (240, 240, 240)
FACE_COLOR = (255, 182, 193)
BACKGROUND = (110, 200, 110)


def beard(draw, leftmost_x, rightmost_x, head_center, r):
    head_x, head_y = head_center
    left_top = (leftmost_x, head_y + r // 2)
    right_top = (rightmost_x, head_y + r // 2)
    bottom = (head_x, head_y + 2*r)
    draw.polygon((left_top, right_top, bottom), fill=GRAY_BEARD)


def face(draw, head_center, r):
    head_x, head_y = head_center
    circle_bounding_box = ((head_x-r, head_y-r), (head_x+r, head_y+r))
    draw.ellipse(circle_bounding_box, fill=FACE_COLOR)


def body(draw, leftmost_x, bottom_y, body_height, body_width):
    bottom_left_corner = (leftmost_x, bottom_y)
    top_right_corner = (leftmost_x + body_width, bottom_y - body_height)
    draw.rectangle((bottom_left_corner, top_right_corner), fill=DWARF_CLOTHES)


def dwarf(draw, leftmost_x, bottom_y, figure_height):
    head_to_body_ratio = 0.2
    # half of head is within body rectangle
    body_height = figure_height // (1 + head_to_body_ratio / 2)
    body_width = figure_height//2.5
    head_x = leftmost_x + body_width//2
    head_y = bottom_y - body_height
    r = body_width // 1.5
    head_center = head_x, head_y
    body(draw, leftmost_x, bottom_y, body_height, body_width)
    face(draw, head_center, r)
    beard(draw, leftmost_x, leftmost_x + body_width, head_center, r)


def landscape(width, height, figure_height):
    im = Image.new("RGB", (width, height), BACKGROUND)

    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
    draw = ImageDraw.Draw(im)

    x0 = 20
    y0 = height - 70
    dwarf(draw, x0, y0, figure_height)
    dwarf(draw, x0 + 80, y0, figure_height)
    dwarf(draw, x0 + 190, y0, figure_height)
    dwarf(draw, x0 + 260, y0, figure_height)

    im.save("dwarves.png")
    im.show()


landscape(WIDTH, HEIGHT, FIGURE_HEIGHT)
