from PIL import Image
width = 2
height = 2
list_of_pixels = [(255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]
print(list_of_pixels)
im = Image.new("RGB", (width, height))
im.putdata(list_of_pixels)
im.save("generated.png")
