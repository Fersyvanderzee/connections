"""
All possible figures
"""

from PIL import ImageDraw

"""
TO DO:

Draw polygon for a filled diamond.
"""


class Figures:

    def __init__(self, line_w_big, line_w_small, image):
        self.line_w_big = line_w_big
        self.line_w_small = line_w_small
        self.draw = ImageDraw.Draw(image)


    def draw_rectangle(self, filled: bool, start_xy: tuple, size: tuple):
        """
            Draw a rectangle on the specified image.

            Parameters:
            - filled (bool): A boolean indicating whether the rectangle should be filled (True) or outlined (False).
            - start_xy (tuple): A tuple containing the (x, y) coordinates of the top-left corner of the rectangle.
            - size (tuple): A tuple containing the width and height of the rectangle.

            Raises:
            - ValueError: If the 'filled' parameter is not a boolean, or if 'start_xy' or 'dimensions' are not tuples.

            Note:
            - If 'filled' is True, the rectangle will be filled with a white color.
            - If 'filled' is False, the rectangle will be outlined with a white color, and the outline width is determined by the 'line_w_small' attribute of the object.
        """

        if not isinstance(filled, bool):
            raise ValueError("filled should be a bool.")

        if not isinstance(start_xy, tuple) or not isinstance(size, tuple):
            raise ValueError("start_xy and dimensions should both be bools.")

        if filled:
            fill = (255, 255, 255)
            outline = None
            width = 0
        else:
            fill = None
            outline = (255, 255, 255)
            width = self.line_w_small

        self.draw.rectangle(
            xy=(start_xy[0], start_xy[1], start_xy[0] + size[0], start_xy[1] + size[1]),
            fill=fill, outline=outline, width=width
        )


    def __draw_diamond_line(self, center_xy: tuple, size: int):
        """
            Draw a diamond on the image using the specified center coordinates and size.

            Parameters:
            - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the diamond.
            - size (int): The size of the diamond (distance from the center to each vertex).

            Raises:
            - ValueError: If the center_xy parameter is not a tuple, or if 'size' is not an int.

            Note:
            - The diamond is drawn using the current object's attributes for line color and width.
              The fill color is set to white (255, 255, 255), and the line width is determined by the 'line_w_small' attribute.

        """

        if not isinstance(center_xy, tuple):
            raise ValueError("filled should be a bool.")

        if not isinstance(size, int):
            raise ValueError("size should be an int.")


        size = size / 2

        fill = (255, 255, 255)
        width = self.line_w_small

        x, y = center_xy

        points = [
            (x, y - size),  # Top vertex
            (x + size, y),  # Right vertex
            (x, y + size),  # Bottom vertex
            (x - size, y),  # Left vertex
        ]

        self.draw.line(points + [points[0]], fill=fill, width=width)


    def __draw_diamond_filled(self, center_xy: tuple, size: int):
        """
            Draw a filled diamond on the image using the specified center coordinates and size.

            Parameters:
            - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the diamond.
            - size (int): The size of the diamond (distance from the center to each vertex).

            Raises:
            - ValueError: If 'center_xy' is not a tuple, or if 'size' is not an integer.

             Note:
            - The diamond is defined by its four vertices: top, right, bottom, and left.
            - The 'fill' parameter specifies the RGB color values for filling the diamond, and 'outline' is set to None for a filled shape.
            - The 'width' parameter is set to 0, as width is not applicable for filled shapes.

        """

        if not isinstance(center_xy, tuple):
            raise ValueError("filled should be a bool.")

        if not isinstance(size, int):
            raise ValueError("size should be an int.")

        size = size / 2

        x, y = center_xy

        points = [
            (x, y - size),  # Top vertex
            (x + size, y),  # Right vertex
            (x, y + size),  # Bottom vertex
            (x - size, y),  # Left vertex
        ]

        fill = (255, 255, 255)

        self.draw.polygon(points, fill=fill, outline=None, width=0)


    def draw_diamond(self, filled: bool, center_xy: tuple, size: int):
        if filled:
            self.__draw_diamond_filled(center_xy=center_xy, size=size)
        else:
            self.__draw_diamond_line(center_xy=center_xy, size=size)


    def draw_circle(self, filled: bool, center_xy: tuple, size: int):
        """
            Draw a circle on the image using the specified parameters.

            Parameters:
            - filled (bool): A boolean indicating whether the circle should be filled (True) or outlined (False).
            - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the circle.
            - size (int): The diameter of the circle.

            Raises:
            - ValueError: If the 'filled' parameter is not a boolean, or if 'center_xy' is not a tuple, or if 'size' is not an integer.

            Note:
            - If 'filled' is True, the circle will be filled with a white color.
            - If 'filled' is False, the circle will be outlined with a white color, and the outline width is determined by the 'line_w_small' attribute of the object.

        """

        if not isinstance(filled, bool):
            raise ValueError("filled should be a bool.")

        if not isinstance(center_xy, tuple) or not isinstance(size, int):
            raise ValueError("start_xy and dimensions should both be bools.")

        radius = size/2

        if filled:
            fill = (255, 255, 255)
            outline = None
            width = 0
        else:
            fill = None
            outline = (255, 255, 255)
            width = self.line_w_small

        x, y = center_xy
        bounding_box = [(x - radius, y - radius), (x + radius, y + radius)]

        self.draw.ellipse(bounding_box, fill=fill, outline=outline, width=width)



