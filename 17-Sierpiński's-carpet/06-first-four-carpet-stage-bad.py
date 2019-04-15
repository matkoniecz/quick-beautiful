from PIL import Image, ImageDraw


def main():
    """generates an animated gif of the initial stages of Sierpiński's carpet"""
    size = 300
    carpet_without_hole = make_carpet(0, size)
    carpet_with_first_hole = make_carpet(1, size)
    third_carpet = make_carpet(2, size)
    fourth_carpet = make_carpet(3, size)

    animation = [carpet_without_hole, carpet_with_first_hole, third_carpet, fourth_carpet]
    save_animated_gif("Sierpiński's carpet.gif", animation, 1200)


def save_animated_gif(filename, images, duration):
    """
    Saves a file with animated GIF in location specified by filename parameter.
    Frames are specified as list of images in the images parameter.
    durations to display each frame are specified as a list, with milliseconds as the unit,
    list should have the same length as images list.
    """
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image, *other_images = images
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

def make_pattern(draw, x, y, section_size, remaining_levels, hole_color):
    if remaining_levels <= 0:
        return
    corner = (x + section_size // 3, y + section_size // 3)
    paint_square(draw, corner, section_size // 3, hole_color)
    parts = 3
    for x_index in range(parts):
        for y_index in range(parts):
            x_anchor = x + section_size * x_index / parts
            y_anchor = y + section_size * y_index / parts
            new_size = section_size / 3
            new_levels = remaining_levels - 1
            make_pattern(draw, x_anchor, y_anchor, new_size, new_levels, hole_color)

def paint_square(draw, upper_left_corner, square_size, square_color):
    """
    paint square at specified location
    upper_left_corner is an (x, y) tuple
    both upper_left_corner and square_size is specified in pixels
    draw contains ImageDraw object to be drawn on
    """
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/1668
    opposite_corner = (upper_left_corner[0] + square_size - 1, upper_left_corner[1] + square_size - 1)
    draw.rectangle((upper_left_corner, opposite_corner), fill=square_color)

def make_carpet(levels, size):
    PURPLE = (150, 0, 150)
    WHITE = (255, 255, 255)
    carpet_color = PURPLE
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels, hole_color=WHITE)
    return carpet


main()
