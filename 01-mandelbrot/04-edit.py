from PIL import Image
width = 200
height = 200
# https://pillow.readthedocs.io/en/latest/reference/Image.html
im = Image.new("RGB", (width, height), (255, 0, 0))
pixels = im.load()
x = 5 # indexed from left
y = 40 # indexed from top
pixels[x, y] = (0, 255, 0)
im.save("generated.png")
im.show()
