"""
This draws the baseline or base axis. On or close to this line all entities instantiate.
"""
import random
from shape import Line


class BaseLine:

    def __init__(self, image, start_xy, iterations):
        self.image = image
        self.start_xy = start_xy
        self.COORDS = [self.start_xy]
        self.generate_coords(iterations)


        for i in range(len(self.COORDS)+1):
            if i <= len(self.COORDS):
                connection_coords = self.generate_connection_coords(self.COORDS[i], self.COORDS[i+1])
                if connection_coords is not None:
                    self.COORDS.insert(i+1, connection_coords)

                self.draw_base_line(self.COORDS[i], self.COORDS[i+1])


    def generate_coords(self, max_iter: int):

        for i in range(max_iter):
            coord = (
                self.start_xy[0] + (random.randint(1, 30) * 10),
                self.start_xy[1] + (random.randint(1, 30) * 10)
            )

            self.COORDS.append(coord)


    @staticmethod
    def generate_connection_coords(xy1, xy2):
        # Takes coords and returns coords that are in between them if they are not on the same axis.
        # Prevents the creation of diagonal lines.
        # Takes a list of two coords [(x1, y1), (x2, y2)]

        # If the coords on of the axi are the same, there is a straight line so no need for a connection coord.
        if xy1[0] == xy2[0] or xy1[1] == xy2[1]:
            return None

        choice = random.choice([True, False])

        if choice:
            connection_coords = (xy2[0], xy1[1])
        else:
            connection_coords = (xy1[0], xy2[1])

        return connection_coords


    def draw_base_line(self, start_xy, end_xy):
        Line(image=self.image, start_xy=start_xy, end_xy=end_xy, main_line=True)


