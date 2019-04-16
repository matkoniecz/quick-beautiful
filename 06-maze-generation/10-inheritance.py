"""
maze generator
"""
import random
from PIL import Image


def main():
    WIDTH = 319
    HEIGHT = 168
    TILE_SIZE_PX = 6
    WHITE = (255, 255, 255)
    PASSAGE_COLOR = WHITE
    BLACK = (0, 0, 0)
    WALL_COLOR = BLACK
    maze = Maze(width=WIDTH, height=HEIGHT)
    maze.output_maze("maze.png", passage_color=PASSAGE_COLOR, wall_color=WALL_COLOR, tile_size_in_pixels=TILE_SIZE_PX)
    maze = MazeWithWideCorridors(width=WIDTH, height=HEIGHT)
    maze.output_maze("maze_alternative.png", passage_color=PASSAGE_COLOR, wall_color=WALL_COLOR, tile_size_in_pixels=TILE_SIZE_PX)


class Maze:
    """
    generates maze using DFS based algorithm
    """

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.PASSAGE_COLOR = (255, 255, 255)
        self.WALL_COLOR = (0, 0, 0)
        self.image = Image.new("RGB", (self.WIDTH, self.HEIGHT), self.WALL_COLOR)
        self.pixels = self.image.load()
        self.generate()

    def generate(self):
        """
        expands maze starting from (0, 0) as a seed location,
        as long as eligible places to carve new tunnels exist
        """
        candidates_list = []
        candidates_list.append((0, 0))
        while len(candidates_list) > 0:
            processed = candidates_list.pop()
            x = processed[0]
            y = processed[1]
            self.pixels[x, y] = self.PASSAGE_COLOR
            new_candidates = self.children(x, y)
            if len(new_candidates) > 0:
                candidates_list.append(processed)
                candidates_list.append(random.choice(new_candidates))

    def output_maze(self, image_output_filepath, tile_size_in_pixels=1, passage_color=(255, 255, 255), wall_color=(0, 0, 0)):
        """
        shows maze image at the screen and
        outputs maze to specified location in image_output_filepath
        using file format implied by extensions
        """
        output = Image.new("RGB", (self.WIDTH, self.HEIGHT))
        output_pixels = output.load()
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if self.pixels[x, y] == self.PASSAGE_COLOR:
                    output_pixels[x, y] = passage_color
                else:
                    output_pixels[x, y] = wall_color
        output = output.resize((self.WIDTH*tile_size_in_pixels, self.HEIGHT*tile_size_in_pixels))
        output.show()
        output.save(image_output_filepath)

    def children(self, parent_x, parent_y):
        """
        returns list of all currently eligible locations to expand from (parent_x, parent_y)
        list contains tuples of integers
        """
        up = (parent_x, parent_y - 1)
        left = (parent_x - 1, parent_y)
        right = (parent_x + 1, parent_y)
        down = (parent_x, parent_y + 1)
        returned = []
        if self.is_safe_to_tunnel(parent_x, parent_y, up[0], up[1]):
            returned.append(up)
        if self.is_safe_to_tunnel(parent_x, parent_y, left[0], left[1]):
            returned.append(left)
        if self.is_safe_to_tunnel(parent_x, parent_y, down[0], down[1]):
            returned.append(down)
        if self.is_safe_to_tunnel(parent_x, parent_y, right[0], right[1]):
            returned.append(right)
        return returned

    def is_safe_to_tunnel(self, parent_x, parent_y, x, y):
        """
        returns true if location (x, y) can be turned into a passage
        false otherwise

        protects agains going outside image or making
        loop or passage wider than 1 tile

        returns false if (x, y) is not inside the image
        returns false if (x, y) is already a passage
        returns false if there are passages around (x, y) that are
        not on (parent_x, parent_y) location or around it
        returns true if location (x, y) can be turned into a passage
        """
        if not self.inside_image(x, y):
            return False
        if self.pixels[x, y] == self.PASSAGE_COLOR:
            return False
        if self.is_colliding_with_other_tunnels(parent_x, parent_y, x, y):
            return False
        return True

    def is_colliding_with_other_tunnels(self, parent_x, parent_y, x, y):
        """
        checks whatever tunnel at this legal location can
        be placed without colliding with other tunnels
        """
        for offset in self.offsets_to_surrounding_tiles():
            if self.is_populated(x + offset[0], y + offset[1]):
                x_distance_to_parent = abs(x + offset[0] - parent_x)
                y_distance_to_parent = abs(y + offset[1] - parent_y)
                if x_distance_to_parent + y_distance_to_parent > 1:
                    return True
        return False

    def offsets_to_surrounding_tiles(self):
        """
        returns list of 2-tuples with distances to
        each of 8 neighbouring tiles
        """
        return [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]

    def is_populated(self, x, y):
        """returns true if this locations contains passage, false if wall or is outside image"""
        if not self.inside_image(x, y):
            return False
        if self.pixels[x, y] == self.PASSAGE_COLOR:
            return True
        return False

    def inside_image(self, x, y):
        """
        returns true if (x, y) is inside image,
        return false otherwise
        """
        if x < 0:
            return False
        if y < 0:
            return False
        if x >= self.WIDTH:
            return False
        if y >= self.HEIGHT:
            return False
        return True


class MazeWithWideCorridors(Maze):
    def is_colliding_with_other_tunnels(self, parent_x, parent_y, x, y):
        """
        checks whatever tunnel at this legal location can
        be placed without colliding with other tunnels
        """
        for offset in self.offsets_to_surrounding_tiles():
            if self.is_populated(x + offset[0], y + offset[1]):
                x_distance_to_parent = abs(x + offset[0] - parent_x)
                y_distance_to_parent = abs(y + offset[1] - parent_y)
                if x_distance_to_parent > 1 or y_distance_to_parent > 1:
                    return True
        return False


main()
