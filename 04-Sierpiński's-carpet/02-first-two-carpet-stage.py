from PIL import Image
from PIL import ImageDraw

size = 300
carpet_color = (150, 0, 150)
hole_color = (255, 255, 255)
carpet_without_hole = Image.new("RGBA", (size, size), carpet_color)
carpet_with_first_hole = Image.new("RGBA", (size, size), carpet_color)
draw = ImageDraw.Draw(carpet_with_first_hole)
draw.rectangle(((size / 3, size / 3), (size * 2/3, size * 2/3)), fill=hole_color)


carpet_without_hole.save("Sierpiński's carpet.gif", save_all=True, append_images=[carpet_with_first_hole], duration=1200, loop=0)
