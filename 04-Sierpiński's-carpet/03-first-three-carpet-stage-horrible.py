from PIL import Image
from PIL import ImageDraw


def make_hole(draw, x, y, section_size):
    hole_color = (255, 255, 255)
    corner = (x + section_size / 3, y + section_size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (x + section_size * 2/3 - 1, y + section_size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)


size = 300
carpet_color = (150, 0, 150)

carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)

carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
draw = ImageDraw.Draw(carpet_with_first_hole)
make_hole(draw, 0, 0, size)

third_carpet = Image.new("RGBA", (size, size), carpet_color)
draw = ImageDraw.Draw(third_carpet)
make_hole(draw, 0, 0, size)
make_hole(draw, 0, 0, size/3)
make_hole(draw, 0, size/3, size/3)
make_hole(draw, 0, size*2/3, size/3)
make_hole(draw, size/3, 0, size/3)
make_hole(draw, size/3, size/3, size/3)
make_hole(draw, size/3, size*2/3, size/3)
make_hole(draw, size*2/3, 0, size/3)
make_hole(draw, size*2/3, size/3, size/3)
make_hole(draw, size*2/3, size*2/3, size/3)

carpet_without_hole.save("Sierpiński's carpet.gif", save_all=True, append_images=[carpet_with_first_hole, third_carpet], duration=1200, loop=0)
