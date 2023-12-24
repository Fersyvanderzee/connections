"""
All helper functions
"""


class Functions:


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


