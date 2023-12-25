"""
Each object is made up of a base shape and a line going up or down. On the end of the line could be another shaped
based on probability. If there is a shape generated at the end of the line, the processes starts again.
It's highly unlikely that there is a multi-object entity, but there still should be some.
"""
from shape import *
import random

"""
NOTES:
Start_xy should be in range of the baseline. 
"""


class Entity:

    SIZE_RANGE_A = 10
    SIZE_RANGE_B = 30

    def __init__(self, image, spawn_area: list, is_up: bool, color):
        self.image = image
        self.color = color

        random_pos = (
            random.randint(spawn_area[0][0], spawn_area[1][0]),
            random.randint(spawn_area[0][1], spawn_area[1][1])
        )
        self.COORDS = [random_pos]

        x = random_pos[0]

        iterations = random.randint(1, 5)

        try:
            for i in range(iterations):
                current_coord = self.COORDS[i]
                y = current_coord[1]
                new_coord = self.generate_coord(y=y, is_up=is_up)
                if 100 < new_coord < 3000:
                    self.COORDS.append((x, new_coord))

            size_arr = len(self.COORDS)

            for i in range(size_arr):
                if i < size_arr - 1 and size_arr > 1:
                    Line(image=self.image, start_xy=self.COORDS[i], end_xy=self.COORDS[i+1], main_line=False, color=self.color)

                start_shape = self.choose_shape()
                if i < size_arr - 1 or random.choice([True, False]):
                    self.draw_shape(shape_name=start_shape, xy=self.COORDS[i])

        except IndexError:
            pass


    @staticmethod
    def choose_shape():
        possible_shapes = [
            'Rectangle',
            'Circle',
            'Diamond'
        ]

        return random.choice(possible_shapes)


    def draw_shape(self, xy, shape_name: str):
        filled = random.choice([True, False])
        match shape_name:
            case 'Rectangle':
                size = (
                    random.randint(self.SIZE_RANGE_A, self.SIZE_RANGE_B),
                    random.randint(self.SIZE_RANGE_A, self.SIZE_RANGE_B)
                )
                Rectangle(image=self.image, filled=filled, center_xy=xy, size=size, color=self.color)
                return size[1]

            case 'Circle':
                size = random.randint(self.SIZE_RANGE_A, self.SIZE_RANGE_B)
                Circle(image=self.image, filled=filled, center_xy=xy, size=size, color=self.color)
                return size

            case 'Diamond':
                size = random.randint(self.SIZE_RANGE_A, self.SIZE_RANGE_B)
                Diamond(image=self.image, filled=filled, center_xy=xy, size=size, color=self.color)
                return size


    def generate_coord(self, y: int, is_up: bool):
        length = random.randint(self.SIZE_RANGE_A, self.SIZE_RANGE_B) * 5

        if is_up:
            new_y = y + length
        else:
            new_y = y - length

        return new_y



