"""
All helper functions
"""

import random
from enum import Enum


class Orientation(Enum):
    TOP = 'top'
    BOTTOM = 'bottom'
    LEFT = 'left'
    RIGHT = 'right'


class Functions:

    @staticmethod
    def probability(probability: int = 4):
        """
        Determine the probability of an event based on a randomly generated integer.

        Parameters:
        - end_point_xy (tuple): A tuple containing the (x, y) coordinates of a point.
        - probability (int): An integer between 1 and 10 representing the likelihood of the event (default is 4).

        Returns:
        - bool: True if the event occurs based on the probability, False otherwise.

        """

        if probability < 1 or probability > 10:
            raise ValueError("probability should be between 1 and 10.")

        if not isinstance(probability, int):
            raise ValueError("probability should be an int.")

        random_int = random.randint(1, 10)

        if random_int < probability:
            return True


    @staticmethod
    def continue_endpoint(endpoint: tuple, dimensions: tuple, orientation: Orientation):
        """
        Calculate the new endpoint coordinates based on the provided endpoint, dimensions, and orientation.

        Parameters:
        - endpoint (tuple): A tuple containing the (x, y) coordinates of the original endpoint.
        - dimensions (tuple): A tuple containing the width and height of the extension from the original endpoint.
        - orientation (Orientation): An enumeration indicating the direction of extension.

        Returns:
        - tuple: A tuple containing the new (x, y) coordinates of the extended endpoint.

        Raises:
        - ValueError: If orientation is not one of Orientation enum values.

        """

        if orientation not in Orientation:
            raise ValueError("Invalid orientation. Should be one of Orientation.TOP, Orientation.BOTTOM, Orientation.LEFT, Orientation.RIGHT.")

        x, y = endpoint

        match orientation:
            case Orientation.TOP:
                new_x, new_y = x, y + dimensions[1]
            case Orientation.BOTTOM:
                new_x, new_y = x, y - dimensions[1]
            case Orientation.LEFT:
                new_x, new_y = x + dimensions[0], y
            case Orientation.RIGHT:
                new_x, new_y = x - dimensions[0], y
            case _:
                new_x, new_y = x, y

        return new_x, new_y


    @staticmethod
    def is_collision(object1, object2):
        """
        Check for collision between two objects based on their bounding boxes.

        Parameters:
        - object1 (object): The first object with a bounding box defined as BOUNDING_BOX.
        - object2 (object): The second object with a bounding box defined as BOUNDING_BOX.

        Returns:
        - bool: True if a collision is detected, False otherwise.

        """

        x1, y1, w1, h1 = object1.BOUNDING_BOX
        x2, y2, w2, h2 = object2.BOUNDING_BOX

        if x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
            return True
        else:
            return False


