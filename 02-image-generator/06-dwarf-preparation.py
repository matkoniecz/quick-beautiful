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


def body():
    print("draw dwarf body - red rectangle")


def face():
    print("draw dwarf face - pink circle")


def beard():
    print("draw dwarf beard - gray triangle")


def dwarf():
    print()
    print("drawing dwarf!")
    body()
    face()
    beard()


def landscape():
    dwarf()
    dwarf()
    dwarf()


landscape()
