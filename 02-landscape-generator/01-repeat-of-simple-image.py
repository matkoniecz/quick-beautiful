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
im = Image.new("RGB", (width, height), (255, 0, 0))
pixels = im.load()
pixels[10, 10] = (0, 255, 0)

im.save("generated.png")
im.show()  # is it working on Windows?
