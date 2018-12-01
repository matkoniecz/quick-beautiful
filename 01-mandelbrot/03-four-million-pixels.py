from PIL import Image
width = 2000
height = 2000
list_of_pixels = []
for _ in range(width*height):
    list_of_pixels.append((255, 0, 0))
im = Image.new("RGB", (width, height))
im.putdata(list_of_pixels)
im.save("generated.png")
