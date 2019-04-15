from PIL import Image, ImageDraw

WIDTH = 2000
HEIGHT = 400
FIGURE_HEIGHT = 80
DWARF_CLOTHES = (240, 30, 20)
GRAY_BEARD = (240, 240, 240)
FACE_COLOR = (255, 182, 193)
GRASS = (20, 230, 20)
BACKGROUND = (110, 200, 110)
HOUSE_WALL = (230, 150, 100)


def main():
    landscape(WIDTH, HEIGHT, FIGURE_HEIGHT)


def landscape(width, height, figure_height):
    im = Image.new("RGB", (width, height), BACKGROUND)

    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
    draw = ImageDraw.Draw(im)
    grass_height = height // 3
    grass(draw, width, height, grass_height)

    house_width = min(300, width // 3)
    left_house_wall_x = width - house_width * 2
    house_base_y = height - grass_height // 2
    lower_left_house_anchor = (left_house_wall_x, house_base_y)
    house_height = min(figure_height * 3, int(house_base_y * 0.8))
    house_size = (house_width, house_height)
    house(draw, lower_left_house_anchor, house_size)

    x0 = 20
    y0 = height - grass_height // 2
    dwarf(draw, x0, y0, figure_height)
    dwarf(draw, x0 + 80, y0, figure_height)
    dwarf(draw, x0 + 190, y0, figure_height)
    dwarf(draw, x0 + 260, y0, figure_height)

    im.save("dwarves.png")
    im.show()


def grass(draw, width, height, grass_height):
    x0 = 0
    y0 = height - 1
    x1 = width - 1
    y1 = height - grass_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=GRASS)


def house(draw, lower_left_anchor, wall_size):
    left_x, left_y = lower_left_anchor
    wall_width, wall_height = wall_size
    right_upper_corner = (left_x + wall_width, left_y - wall_height)
    coordinates = (lower_left_anchor, right_upper_corner)
    draw.rectangle(coordinates, fill=HOUSE_WALL)


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
    hat(draw, leftmost_x, leftmost_x + body_width, head_center, r)
    beard(draw, leftmost_x, leftmost_x + body_width, head_center, r)


def hat(draw, x0, x1, head_center, r):
    head_x, head_y = head_center
    left_bottom = (x0 - r // 1.5, head_y)
    right_bottom = (x1 + r // 1.5, head_y)
    top = (head_x, head_y - 2*r)
    draw.polygon((left_bottom, right_bottom, top), fill=DWARF_CLOTHES)


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


main()
