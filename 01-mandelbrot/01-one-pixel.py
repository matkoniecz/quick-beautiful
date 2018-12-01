from PIL import Image
width = 1
height = 1
list_of_pixels = [(255, 0, 0)]
# https://pillow.readthedocs.io/en/5.3.x/reference/Image.html
im = Image.new("RGB", (width, height))
im.putdata(list_of_pixels)
im.save("generated.png")
