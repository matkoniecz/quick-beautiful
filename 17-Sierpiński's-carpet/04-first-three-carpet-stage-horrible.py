from PIL import Image, ImageDraw


def main():
    """generates an animated gif of the initial stages of Sierpiński's carpet"""
    size = 300
    PURPLE = (150, 0, 150)
    WHITE = (255, 255, 255)
    carpet_color = PURPLE

    carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)

    carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet_with_first_hole)
    make_hole(draw, 0, 0, size, hole_color=WHITE)

    third_carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(third_carpet)
    make_hole(draw, 0, 0, size, hole_color=WHITE)
    make_hole(draw, 0, 0, size/3, hole_color=WHITE)
    make_hole(draw, 0, size/3, size/3, hole_color=WHITE)
    make_hole(draw, 0, size*2/3, size/3, hole_color=WHITE)
    make_hole(draw, size/3, 0, size/3, hole_color=WHITE)
    make_hole(draw, size/3, size/3, size/3, hole_color=WHITE)
    make_hole(draw, size/3, size*2/3, size/3, hole_color=WHITE)
    make_hole(draw, size*2/3, 0, size/3, hole_color=WHITE)
    make_hole(draw, size*2/3, size/3, size/3, hole_color=WHITE)
    make_hole(draw, size*2/3, size*2/3, size/3, hole_color=WHITE)

    animation = [carpet_without_hole, carpet_with_first_hole, third_carpet]
    save_animated_gif("Sierpiński's carpet.gif", animation, 1200)


def save_animated_gif(filename, images, duration):
    """merges files into a single animated gif and saves it at the specified location"""
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image, *other_images = images
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

def make_hole(draw, x, y, section_size, hole_color):
    corner = (x + section_size / 3, y + section_size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (x + section_size * 2/3 - 1, y + section_size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)


main()
