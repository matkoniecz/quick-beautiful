from PIL import Image
width = 20
height = 20
list_of_pixels = []
for _ in range(width*height):
    list_of_pixels.append((255, 0, 0))
im = Image.new("RGB", (width, height))
im.putdata(list_of_pixels)
pixels = im.load()
pixels[10, 10] = (0, 255, 0)
im.save("generated.png")
