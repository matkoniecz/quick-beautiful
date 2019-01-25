from PIL import Image, ImageDraw

def hat(draw, x0, x1, head_x, head_y, r):
    draw.polygon(((x0 - 15, head_y), (x1 + 15, head_y), (head_x, head_y - 2*r)), fill=(240, 30, 20))

def beard(draw, x0, x1, head_x, head_y, r):
    draw.polygon(((x0, head_y + 10), (x1, head_y + 10), (head_x, head_y + 2*r)), fill=(240, 240, 240))

def dwarf(draw, x0, y0, figure_height):
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


def house_wall(draw, house_height, house_width, left_house_wall_x, house_base_y):
    coordinates = ((left_house_wall_x, house_base_y), (left_house_wall_x + house_width, house_base_y - house_height))
    draw.rectangle(coordinates, fill=(230, 150, 100))


def house_door(draw, house_height, house_width, left_house_wall_x, house_base_y, figure_height):
    door_height = figure_height * 1.2
    door_width = door_height / 1.6
    draw.rectangle(((left_house_wall_x + house_width/10, house_base_y), (left_house_wall_x + house_width/10 + door_width, house_base_y - door_height)), fill=(200, 120, 90))

def house_roof(draw, house_height, house_width, left_house_wall_x, house_base_y):
    draw.polygon(((left_house_wall_x - 15, house_base_y - house_height), (left_house_wall_x + house_width + 15, house_base_y - house_height), (left_house_wall_x + house_width/2, house_base_y - house_height*2)), fill=(240, 60, 60))

def house(draw, height, width, grass_height, figure_height):
    house_height = 250
    house_width = 300

    left_house_wall_x = width - house_width * 2
    house_base_y = height - grass_height / 2
    house_height = 120
    house_wall(draw, house_height, house_width, left_house_wall_x, house_base_y)
    house_door(draw, house_height, house_width, left_house_wall_x, house_base_y, figure_height)
    house_roof(draw, house_height, house_width, left_house_wall_x, house_base_y)

width = 2000
height = 400
im = Image.new("RGB", (width, height), (110, 200, 110))

# https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
draw = ImageDraw.Draw(im)
grass_height = int(height / 3)
figure_height = 80
grass(draw, width, height, grass_height)
house(draw, height, width, grass_height, figure_height)


x0 = 20
y0 = height - int(grass_height / 2)
dwarf(draw, x0, y0, figure_height)
dwarf(draw, x0 + 80, y0, figure_height)
dwarf(draw, x0 + 190, y0, figure_height)
dwarf(draw, x0 + 260, y0, figure_height)

im.save("dwarves.png")
im.show()
