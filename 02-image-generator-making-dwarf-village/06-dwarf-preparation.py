"""
landscape generation topic: dwarves in front of their home

lets draw dwarf using as simplest geometry elements as possible 
"""
WIDTH = 2000
HEIGHT = 400
FIGURE_HEIGHT = 80
DWARF_CLOTHES = (240, 30, 20)
GRAY_BEARD = (240, 240, 240)
FACE_COLOR = (255, 182, 193)
BACKGROUND = (110, 200, 110)


def landscape():
    """draw landscape with dwarfs in it"""
    dwarf()
    dwarf()
    dwarf()


def dwarf():
    """draw dwarf"""
    print()
    print("drawing dwarf!")
    body()
    face()
    beard()


def beard():
    """draw beard of a dwarf"""
    print("draw dwarf beard - gray triangle")


def face():
    """draw face of a dwarf"""
    print("draw dwarf face - pink circle")


def body():
    """draw body of a dwarf"""
    print("draw dwarf body - red rectangle")


landscape()
