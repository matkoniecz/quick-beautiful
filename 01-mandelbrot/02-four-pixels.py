from PIL import Image
width = 2
height = 2
# https://pillow.readthedocs.io/en/latest/reference/Image.html
im = Image.new("RGB", (width, height), (255, 0, 0))
im.save("generated.png")
im.show()
