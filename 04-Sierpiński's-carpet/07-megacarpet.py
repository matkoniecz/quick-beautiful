from PIL import Image
from PIL import ImageDraw


def make_pattern(draw, x, y, section_size, remaining_levels):
    if remaining_levels <= 0:
        return
    hole_color = (255, 255, 255)
    corner = (x + section_size / 3, y + section_size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (x + section_size * 2/3 - 1, y + section_size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)
    parts = 3
    for x_index in range(parts):
        for y_index in range(parts):
            min_x_in_section = x + section_size * x_index / parts
            min_y_in_section = y + section_size * y_index / parts
            make_pattern(draw, min_x_in_section, min_y_in_section, section_size / 3, remaining_levels - 1)

def make_carpet(levels, size):
    carpet_color = (150, 0, 150)
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels)
    return carpet

levels = 7
size = 3**levels
carpets = []
first_carpet = make_carpet(0, size)
for i in range(levels - 1):
    carpets.append(make_carpet(i + 1, size))

first_carpet.save("Sierpiński's carpet.gif", save_all=True, append_images=carpets, duration=1200, loop=1)

