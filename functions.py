"""
All helper functions
"""


import random


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
    def continue_endpoint(endpoint_xy: tuple, size: tuple, orientation: str):
        """
            Calculate the new endpoint coordinates based on the provided endpoint, size, and orientation.

            Parameters:
            - endpoint_xy (tuple): A tuple containing the (x, y) coordinates of the original endpoint.
            - size (tuple): A tuple containing the width and height of the extension from the original endpoint.
            - orientation (str): A string indicating the direction of extension. Should be one of ['top', 'bottom', 'left', 'right'].

            Returns:
            - tuple: A tuple containing the new (x, y) coordinates of the extended endpoint.

            Raises:
            - ValueError: If 'orientation' is not one of ['top', 'bottom', 'left', 'right'].

        """

        if orientation.lower() not in ['top', 'bottom', 'left', 'right']:
            raise ValueError("Orientation should be top, bottom, left or right.")

        match orientation:
            case 'top':
                new_endpoint_xy = endpoint_xy[0] + size[1]
            case 'bottom':
                new_endpoint_xy = endpoint_xy[0] - size[1]
            case 'left':
                new_endpoint_xy = endpoint_xy[1] + size[0]
            case 'right':
                new_endpoint_xy = endpoint_xy[1] - size[0]
            case _:
                new_endpoint_xy = endpoint_xy

        return new_endpoint_xy

