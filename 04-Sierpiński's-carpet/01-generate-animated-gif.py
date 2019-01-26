from packaging import version
from PIL import Image

width = 300
height = 300
im1 = Image.new("RGBA", (width, height), (255, 0, 0))
im2 = Image.new("RGBA", (width, height), (255, 255, 0))
im3 = Image.new("RGBA", (width, height), (255, 255, 255))
if version.parse(Image.PILLOW_VERSION) < version.parse("3.4"):
    print("Pillow in version not supporting making animated gifs")
    print("you need to upgrade library version")
    print("see release notes in")
    print("https://pillow.readthedocs.io/en/latest/releasenotes/3.4.0.html#append-images-to-gif")
else:
    im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=900, loop=0)
