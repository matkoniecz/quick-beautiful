from PIL import Image, ImageDraw


def hat(draw, x0, x1, head_x, head_y, r):
    left_bottom = (x0 - 15, head_y)
    right_bottom = (x1 + 15, head_y)
    top = (head_x, head_y - 2*r)
    draw.polygon((left_bottom, right_bottom, top), fill=(240, 30, 20))


def beard(draw, x0, x1, head_x, head_y, r):
    left_top = (x0, head_y + 10)
    right_top = (x1, head_y + 10)
    bottom = (head_x, head_y + 2*r)
    draw.polygon((left_top, right_top, bottom), fill=(240, 240, 240))


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


def grass(draw, width, height, grass_height):
    x0 = 0
    y0 = height - 1
    x1 = width - 1
    y1 = height - grass_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=(20, 230, 20))


def house(draw, lower_left_house_anchor, house_size):
    left_house_wall_x, left_house_wall_y = lower_left_house_anchor
    wall_width, wall_height = house_size
    coordinates = ((left_house_wall_x, left_house_wall_y), (left_house_wall_x + wall_width, left_house_wall_y - wall_height))
    draw.rectangle(coordinates, fill=(230, 150, 100))


width = 2000
height = 400
im = Image.new("RGB", (width, height), (110, 200, 110))

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
grass_height = int(height / 3)
figure_height = 80
grass(draw, width, height, grass_height)

house_width = min(300, width / 3)
left_house_wall_x = width - house_width * 2
house_base_y = height - grass_height / 2
lower_left_house_anchor = (left_house_wall_x, house_base_y)
house_height = min(figure_height * 3, house_base_y * 0.8)
house_size = (house_width, house_height)
house(draw, lower_left_house_anchor, house_size)


x0 = 20
y0 = height - int(grass_height / 2)
dwarf(draw, x0, y0)
dwarf(draw, x0 + 80, y0)
dwarf(draw, x0 + 190, y0)
dwarf(draw, x0 + 260, y0)

im.save("dwarves.png")
im.show()
