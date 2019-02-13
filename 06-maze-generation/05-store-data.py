from PIL import Image
import random

WIDTH = 50
HEIGHT = 50
WHITE = (255, 255, 255)
PASSAGE_COLOR = WHITE
BLACK = (0, 0, 0)
WALL_COLOR = BLACK
PASSAGE = 1
WALL = 0


def move_in_random_cardinal_direction(point):
    randomized = random.randint(1, 4)
    if randomized == 1:
        return (point[0] + 1, point[1])
    elif randomized == 2:
        return (point[0] - 1, point[1])
    elif randomized == 3:
        return (point[0], point[1] + 1)
    else:
        return (point[0], point[1] - 1)


def is_outside_area(position, WIDTH, HEIGHT):
    if position[0] < 0:
        return True
    if position[0] >= WIDTH:
        return True
    if position[1] < 0:
        return True
    if position[1] >= HEIGHT:
        return True
    return False


def print_maze_to_console(MAZE):
    WIDTH = len(MAZE)
    HEIGHT = len(MAZE[0])
    for y in range(HEIGHT-1, -1, -1):
        for x in range(WIDTH):
            print(MAZE[x][y], end="")
        print()


def print_maze_to_image_file(MAZE, WALL_COLOR, PASSAGE_COLOR, filepath):
    WIDTH = len(MAZE)
    HEIGHT = len(MAZE[0])
    im = Image.new("RGB", (WIDTH, HEIGHT), WALL_COLOR)
    pixels = im.load()
    for x in range(WIDTH):
        for y in range(WIDTH):
            if MAZE[x][y] == PASSAGE:
                pixels[x, y] = PASSAGE_COLOR
    im.save(filepath)
    im.show()  # it may not work in rare cases, but generally very, very useful


def main():
    maze = []
    for _x in range(WIDTH):
        column = []
        for _y in range(WIDTH):
            column.append(WALL)
        maze.append(column)

    print_maze_to_console(maze)

    position = (WIDTH//2, HEIGHT//2)
    for _ in range(5000):
        x = position[0]
        y = position[1]
        maze[x][y] = PASSAGE
        position = move_in_random_cardinal_direction(position)
        if is_outside_area(position, WIDTH, HEIGHT):
            break

    print()
    print_maze_to_console(maze)
    print_maze_to_image_file(maze, WALL_COLOR, PASSAGE_COLOR, "maze.png")


main()
