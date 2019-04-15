from PIL import Image, ImageDraw


def main():
    """generates an animated gif of the initial stages of Sierpiński's carpet"""
    size = 300
    PURPLE = (150, 0, 150)
    WHITE = (255, 255, 255)
    carpet_color = PURPLE
    hole_color = WHITE
    carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)
    carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet_with_first_hole)

    corner = (size / 3, size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (size * 2/3 - 1, size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)

    animation = [carpet_without_hole, carpet_with_first_hole]
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

main()
