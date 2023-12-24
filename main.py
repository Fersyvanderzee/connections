from shape import *
from PIL import Image
from base_line import BaseLine
import random
from entity import Entity

"""
ONLY FOR TESTING PURPOSES.
"""

img_width, img_height = 3000, 3000
margin = 100

bg_color = (185, 32, 39)

image = Image.new(mode='RGB', size=(img_width, img_height), color=bg_color)

Entity(image, start_xy=(500, 500), is_up=False)

image.show()
