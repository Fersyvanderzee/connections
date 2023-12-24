"""
All possible shapes
"""
from PIL import ImageDraw, Image


class Shape:
    """
    Class for drawing various shapes on an image.

    """

    COLOR = (220, 220, 220)
    BG_COLOR = (185, 32, 39)
    SMALL_LINE_WIDTH = 1
    BIG_LINE_WIDTH = 2
    BOUNDING_BOX = ()

    def __init__(self, image: Image.Image):
        """
        Initialize the Shape class.

        Parameters:
        - image (PIL.Image): The image on which shapes will be drawn.

        """

        self.draw = ImageDraw.Draw(image)

    @classmethod
    def set_color(cls, color: tuple):
        cls.COLOR = color

    @classmethod
    def set_small_line_width(cls, line_width: int):
        cls.SMALL_LINE_WIDTH = line_width

    @classmethod
    def set_big_line_width(cls, line_width: int):
        cls.BIG_LINE_WIDTH = line_width

    def draw_bounding_box(self, center_xy: tuple, size: int | tuple):

        x, y = center_xy

        if isinstance(size, tuple):
            size_l = size[0]
            size_h = size[1]

            self.BOUNDING_BOX = (
                (x - size_h, y - size_l),
                (x + size_h, y + size_l)
            )

        elif isinstance(size, int):
            self.BOUNDING_BOX = (
                (x - size, y - size),
                (x + size, y + size)
            )

        else:
            raise ValueError("size should be either int or tuple.")

        # self.draw.rectangle(xy=self.BOUNDING_BOX, fill=None, outline=(255, 0, 0), width=2)


class Rectangle(Shape):
    """
    Class for drawing rectangles on an image.

    """

    def __init__(self, image: Image.Image, filled: bool, center_xy: tuple, size: tuple):
        """
        Initialize the Rectangle class.

        Parameters:
        - big_line_width (int): The line width for main lines.
        - small_line_width (int): The line width for secondary lines.
        - image (PIL.Image): The image on which rectangles will be drawn.
        - filled (bool): Determines if the rectangle is filled or only an outline.
        - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the rectangle.
        - size (tuple): A tuple containing the width and height of the rectangle.

        """

        super().__init__(image)
        self.filled = filled
        self.size = size
        self.dimensions = (
            center_xy[0] - (size[0] / 2),
            center_xy[1] - (size[1] / 2),
            center_xy[0] + (size[0] / 2),
            center_xy[1] + (size[1] / 2)
        )
        self.draw_rectangle()


    def draw_rectangle(self):
        """
        Draw the rectangle on the image.

        """

        if self.filled:
            fill = self.COLOR
            outline = None
            width = 0
        else:
            fill = self.BG_COLOR
            outline = self.COLOR
            width = self.SMALL_LINE_WIDTH

        self.draw.rectangle(xy=self.dimensions, fill=fill, outline=outline, width=width)


class Circle(Shape):
    """
    Class for drawing circles on an image.
    """

    def __init__(self, image: Image.Image, filled: bool, center_xy: tuple, size: int):
        """
        Initialize the Circle class.

        Parameters:
        - big_line_width (int): The line width for main lines.
        - small_line_width (int): The line width for secondary lines.
        - image (PIL.Image): The image on which circles will be drawn.
        - filled (bool): Determines if the circle is filled or only an outline.
        - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the circle.
        - size (int): The diameter of the circle.

        """

        super().__init__(image)
        self.filled = filled
        self.radius = int(size / 2)
        self.center_xy = center_xy
        self.draw_circle()
        super().draw_bounding_box(center_xy=center_xy, size=self.radius)

    def draw_circle(self):
        """
        Draw the circle on the image.

        """

        if self.filled:
            fill = self.COLOR
            outline = None
            width = 0
        else:
            fill = self.BG_COLOR
            outline = self.COLOR
            width = self.SMALL_LINE_WIDTH

        x, y = self.center_xy
        bounding_box = [(x - self.radius, y - self.radius), (x + self.radius, y + self.radius)]

        self.draw.ellipse(bounding_box, fill=fill, outline=outline, width=width)


class Diamond(Shape):
    """
    Class for drawing a diamond on an image.

    """

    def __init__(self, image: Image.Image, filled: bool, center_xy: tuple, size: int):
        """
        Initialize the Diamond class.

        Parameters:
        - image (PIL.Image): The image on which the diamond will be drawn.
        - filled (bool): Determines if the diamond is filled or only an outline.
        - center_xy (tuple): A tuple containing the (x, y) coordinates of the center of the diamond.
        - size (int): The size of the diamond (distance from the center to each vertex).

        """

        super().__init__(image)
        self.filled = filled
        self.size = size / 2
        self.center_xy = center_xy
        self.draw_diamond()

    def draw_diamond(self):
        """
        Draw a diamond on the image using the specified center coordinates and size.

        """

        if self.filled:
            fill = self.COLOR
            outline = None
            width = 0
        else:
            fill = self.BG_COLOR
            outline = self.COLOR
            width = self.SMALL_LINE_WIDTH

        x, y = self.center_xy
        points = [
            (x, y - self.size),  # Top vertex
            (x + self.size, y),  # Right vertex
            (x, y + self.size),  # Bottom vertex
            (x - self.size, y),  # Left vertex
        ]

        self.draw.polygon(points, fill=fill, outline=outline, width=width)


class Line(Shape):
    def __init__(self, image, start_xy: tuple, end_xy: tuple, main_line: bool = False):
        super().__init__(image)
        self.start_xy = start_xy
        self.end_xy = end_xy
        self.main_line = main_line
        self.draw_line()

    def draw_line(self):
        """
        Draw a line on the image.

        Parameters:
        - start_xy (tuple): A tuple containing the (x, y) coordinates of the start point.
        - end_xy (tuple): A tuple containing the (x, y) coordinates of the end point.
        - main_line (bool): Indicates whether it's a main line or not.

        """
        width = self.BIG_LINE_WIDTH if self.main_line else self.SMALL_LINE_WIDTH

        self.draw.line(xy=(self.start_xy, self.end_xy), fill=self.COLOR, width=width)
