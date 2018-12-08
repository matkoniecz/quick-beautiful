from PIL import Image


def scale_position(from_to, value, max_value):
    return from_to[0] + (from_to[1]-from_to[0])*(float(value)/max_value)


def get_color(x, y, X, Y, WIDTH, HEIGHT):
    kx = scale_position(X, x, WIDTH)
    ky = scale_position(Y, y, HEIGHT)
    MAX_IT = 300
    c = complex(kx, ky)
    z = complex(0.0, 0.0)
    for i in range(MAX_IT):
        z = z * z + c
        if abs(z) >= 2.0:
            return (0, int(((i*1.0/MAX_IT)**0.5)*255), 0)
    return (0, 0, 0)


def mandebrot(X, Y, WIDTH, HEIGHT, filename):
    # https://pillow.readthedocs.io/en/latest/reference/Image.html
    im = Image.new("RGB", (WIDTH, HEIGHT), (255, 0, 0))
    pixels = im.load()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            pixels[x, y] = get_color(x, y, X, Y, WIDTH, HEIGHT)

    im.save(filename)
    im.show()


WIDTH = 750
HEIGHT = 750
mandebrot((-1.6, 0.6), (-1.1, 1.1), WIDTH, HEIGHT, "1.png")
mandebrot((-1.0, 0), (-1.1, -0.1), WIDTH, HEIGHT, "2.png")
mandebrot((-0.7, -0.4), (-0.75, -0.45), WIDTH, HEIGHT, "3.png")
mandebrot((-0.6, -0.5), (-0.7, -0.6), WIDTH, HEIGHT, "4.png")
mandebrot((-0.55, -0.5), (-0.7, -0.65), WIDTH, HEIGHT, "5.png")
