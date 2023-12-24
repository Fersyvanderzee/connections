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

for j in range(10):
    for i in range(3):

        x1, x2 = random.randint(margin, img_height - margin), random.randint(margin, img_height - margin)
        y1, y2 = random.randint(margin, img_height - margin), random.randint(margin, img_height - margin)

        spawn_area = [(min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))]

        Entity(image, spawn_area=spawn_area, is_up=random.choice([True, False]))

image.show()
