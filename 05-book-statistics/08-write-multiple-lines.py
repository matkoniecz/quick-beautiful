from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

def generate_image_with_text(text_lines):
    width = 200
    height = 200
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    im = Image.new("RGB", (width, height), WHITE)
    y_line_anchor = 10
    font=ImageFont.truetype("unifont-12.0.01.ttf",14)
    for line in text_lines:
        ImageDraw.Draw(
            im
        ).text(
            (10, y_line_anchor),
            line,
            BLACK,
            font=font
        )
        y_line_anchor += 18

    im.show()

generate_image_with_text(['first line', 'second line', 'third line', 'fourth very very very very very long line'])

