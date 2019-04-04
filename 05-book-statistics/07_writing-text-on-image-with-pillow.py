from PIL import ImageDraw
from PIL import Image

width = 200
height = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
im = Image.new("RGB", (width, height), WHITE)

ImageDraw.Draw(
    im
).text(
    (10, 10),
    'Hello world!',
    BLACK
)

im.show()
