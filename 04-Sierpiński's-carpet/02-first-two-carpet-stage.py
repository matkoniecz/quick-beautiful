from PIL import Image
from PIL import ImageDraw

def save_animated_gif(filename, images, duration):
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image = images[0]
    other_images = images[1:]
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

size = 300
carpet_color = (150, 0, 150)
hole_color = (255, 255, 255)
carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)
carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
draw = ImageDraw.Draw(carpet_with_first_hole)

# -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
rectangle_size = (size * 2/3 - 1, size * 2/3 - 1)

draw.rectangle(((size / 3, size / 3), rectangle_size), fill=hole_color)

animation = [carpet_without_hole, carpet_with_first_hole]
save_animated_gif("Sierpiński's carpet.gif", animation, 1200)
