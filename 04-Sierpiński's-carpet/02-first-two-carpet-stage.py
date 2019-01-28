from PIL import Image
from PIL import ImageDraw

size = 300
carpet_color = (150, 0, 150)
hole_color = (255, 255, 255)
carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)
carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
draw = ImageDraw.Draw(carpet_with_first_hole)

# -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
rectangle_size = (size * 2/3 - 1, size * 2/3 - 1)

draw.rectangle(((size / 3, size / 3), rectangle_size), fill=hole_color)


carpet_without_hole.save("Sierpiński's carpet.gif", save_all=True, append_images=[carpet_with_first_hole], duration=1200, loop=0)
