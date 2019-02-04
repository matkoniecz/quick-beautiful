"""
Landscape generator

What it will be? Forest? Crowd? Train? Countryside? City with skyscrapers?
Factory? Mars/Moon colony? Fantasy land? Ocean island? Below water surface?
Inside a building? Fairy colony in mushrooms? Snail race?

During day? Night? Sunset?

Building blocks are the same but...
"""
from PIL import Image
width = 200
height = 200
RED = (255, 0, 0)
GREEN = (0, 255, 0)
im = Image.new("RGB", (width, height), RED)
pixels = im.load()
pixels[10, 10] = GREEN

im.save("generated.png")
im.show()  # it may not work in rare cases, but generally very, very useful
