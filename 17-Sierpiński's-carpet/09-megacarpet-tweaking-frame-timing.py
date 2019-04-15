from PIL import Image, ImageDraw


def main():
    """generates an animated gif of the initial stages of Sierpiński's carpet"""
    FRACTAL_DEPTH = 7
    size = 3**FRACTAL_DEPTH
    carpets = []
    for i in range(-1, FRACTAL_DEPTH - 1):
        carpets.append(make_carpet(i + 1, size))

    standard_frame_time_in_ms = 1200
    durations = [standard_frame_time_in_ms] * FRACTAL_DEPTH
    durations[0] /= 2  # first stage visible for a short time
    durations[-1] *= 4  # final stage of animation visible for a long time

    save_animated_gif("Sierpiński's carpet.gif", carpets, durations)


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
    DARK_GREEN = (5, 60, 20)
    LIGHT_GREEN = (5, 205, 65)
    carpet_color = DARK_GREEN
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels, hole_color=LIGHT_GREEN)
    return carpet


main()
