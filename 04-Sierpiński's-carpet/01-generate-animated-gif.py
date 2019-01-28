from packaging import version
from PIL import Image

def save_animated_gif(filename, images, duration):
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image = images[0]
    other_images = images[1:]
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration)

def check_version():
    if version.parse(Image.PILLOW_VERSION) >= version.parse("3.4"):
        return
    print("Pillow in version not supporting making animated gifs")
    print("you need to upgrade library version")
    print("see release notes in")
    print("https://pillow.readthedocs.io/en/latest/releasenotes/3.4.0.html#append-images-to-gif")
    raise RuntimeError("upgrade pillow library, to at least 3.4")

check_version()
width = 300
height = 300
im1 = Image.new("RGBA", (width, height), (255, 0, 0))
im2 = Image.new("RGBA", (width, height), (255, 255, 0))
im3 = Image.new("RGBA", (width, height), (255, 255, 255))
save_animated_gif("out.gif", [im1, im2, im3], 900)
